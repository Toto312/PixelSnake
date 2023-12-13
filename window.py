import pygame
import os

import font
import sprite
import event_handler
import scene_manager

class Widget:
    def __init__(self, position = [0,0]):
        self.position = position
        self.is_active = True

    def resize(self, size):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass


class Button(Widget):
    def __init__(self, sprites, position, font=None, command=None, image_front=None):
        self.font = font
        self.sprites = sprites
        if(isinstance(self.sprites,sprite.Sprite)):
            self.sprites = [sprites]
        self.command = command
        self.position = position
        self.image_front = image_front

        # only if len(sprites) == 2
        self.mode = 0

    def update(self):
        # since you cant check the rect of the sprite because its on the 0,0 coordenades,
        # we create another
        rect_button = pygame.Rect(self.position[0],self.position[1],
                                  self.sprites[self.mode].image.get_rect().width,
                                  self.sprites[self.mode].image.get_rect().height)
        if(button := event_handler.EventHandler().check_events("Mouse button down")):
            if((self.font and self.font.rect.collidepoint(button.pos)) or
               (not self.font and rect_button.collidepoint(button.pos))):
                self.command()
                if(len(self.sprites)>1):
                    self.mode = (self.mode+1) % len(self.sprites)
            else:
                self.mode = 0

    def draw(self, window):
        if(isinstance(self.sprites,list) and self.mode <= 2):
            window.blit(self.sprites[self.mode].image,self.position)
        else:
            window.blit(self.sprites.image,self.position)

        if(self.image_front):
            window.blit(self.image_front.image,self.position)

        if(self.font):
            self.font.draw(window)


class Label(Widget):
    def __init__(self, text, font_name, size, position):
        super().__init__(position)

        self.text = text
        self.font_name = font_name
        self.size = size

        self.font = font.Font(self.font_name,self.text,self.position,self.size)

    def draw(self, window):
        self.font.draw(window)


class Options(Widget):
    def __init__(self, size, position, options):
        super().__init__(position)

        self.options = options
        self.size = size
        self.is_active = False

        self.image_selected = sprite.Sprite("Resources/gui/options_waterfall.png")
        self.image_selected.scale(size)

        self.image = sprite.Sprite("Resources/gui/options_waterfall_unselected.png")
        self.image.scale(size)

        self.image_middle_option = sprite.Sprite("Resources/gui/options_waterfall_middle_option.png")
        self.image_middle_option.scale(size)

        self.image_final_option = sprite.Sprite("Resources/gui/options_waterfall_final_option.png")
        self.image_final_option.scale(size)

        self.fonts = []
        self.ui = []

        for i in range(len(options)):
            ui = None
            if(i==0):
                pos = [self.position[0]+size[0]/2,self.position[1]+size[1]/2]
                ui = sprite.Sprite(self.image_selected.image_filename)
            elif(i==1):
                pos = [self.position[0]+size[0]/2,self.fonts[i-1].font.rect[1]+size[1]+10]
                ui = sprite.Sprite(self.image_middle_option.image_filename)
                ui.scale(size)
            else:
                pos = [self.position[0]+size[0]/2,self.fonts[i-1].font.rect[1]+size[1]]
                if(i==len(options)-1):  
                    ui = sprite.Sprite(self.image_final_option.image_filename)
                    ui.scale(size)
                else:
                    ui = sprite.Sprite(self.image_middle_option.image_filename)
                    ui.scale(size)
            b = Button(ui,[self.position[0],pos[1]-size[1]/2],font.Font("Resources/PixeloidSans.ttf",options[i],pos,30,True), lambda i=i: self.change_resolution(i))
            self.fonts.append(b)

        self.is_selected = False
        self.is_opened = False

    def change_resolution(self,index):
        resolution_str = self.options[index]
        resolution = [int(resolution_str[0:resolution_str.index("x")]),int(resolution_str[resolution_str.index("x")+1:])]
        
        if(resolution != list(pygame.display.get_surface().get_size())):
            print(resolution,pygame.display.get_surface().get_size())
            pygame.display.set_mode(resolution)
            scene_manager.SceneManager().curr_scene.resize(resolution)

    def update(self):
        if(self.is_selected):
            self.fonts[0].update()
        elif(self.is_opened):
            for i in range(len(self.fonts)-1):
                i+=1
                self.fonts[i].update()

        if(event := event_handler.EventHandler().check_events("Mouse motion")):
            if(self.image.rect.collidepoint([event.pos[0]-self.position[0],event.pos[1]-self.position[1]])):
                self.is_selected = True
            else:
                self.is_selected = False
        elif(event := event_handler.EventHandler().check_events("Mouse button down")):
            if(self.is_selected and not self.is_opened):
                self.is_opened = True
            elif(self.is_selected and self.is_opened):
                self.is_opened = False
            elif(not self.is_selected and self.is_opened):
                self.is_opened = False

    def draw(self, window):
        window.blit(self.image.image,self.position)
        
        self.fonts[0].draw(window)
        if(self.is_opened):
            for i in self.fonts:
                if(i == self.fonts[0]):
                    continue
                i.draw(window)

        if(self.is_selected):
            window.blit(self.image_selected.image,self.position)


class Window:
    def __init__(self, size, position, color):
        self.size = size
        self.color = color
        self.position = position
        self.is_active = True

        self.window = pygame.Surface(self.size)
        self.window.get_rect().move_ip(self.position)
        self.window.fill(self.color)

        self.widgets = []

    def update(self):
        pass

    def resize(self, size):
        pass

    def add_widget(self, widget):
        self.widgets.append(widget)

    def draw(self, window):
        if(not self.is_active):
            return

        window.blit(self.window,self.position)

        for i in self.widgets:
            i.draw(window)


class OptionsGUI(Window):
    def __init__(self):
        image = sprite.Sprite("Resources/gui/options.png")
        image.scale([image.image.get_size()[0]*5,image.image.get_size()[1]*5])

        super().__init__(image.image.get_size(),[100,100],(102,102,102))
        self.window = image.image

        self.display_title = Label("Display","Resources/PixeloidSans.ttf",20,
                                   [self.position[0]+self.size[0]*0.2,self.position[0]+self.size[0]*0.1])

        self.resolution = Label("Resolution: ","Resources/PixeloidSans.ttf",30,
                                [self.position[0]+self.size[0]*0.45,self.position[0]+self.size[0]*0.3])

        #current size
        resolutions = [str(pygame.display.get_surface().get_size()[0])+"x"+str(pygame.display.get_surface().get_size()[1])]
        #other sizes
        resolutions.extend([str(i[0])+"x"+str(i[1]) for i in pygame.display.list_modes() if i[0]>700 and i[1]>700])
        self.resolutions = Options([42*5,14*5],[self.position[0]+self.size[0]*0.5,self.position[0]+self.size[0]*0.19],resolutions[0:5])

        full_screen_sprite = [sprite.Sprite("Resources/gui/button_release.png"),
                              sprite.Sprite("Resources/gui/button_pressed.png")]
        for i in full_screen_sprite:
            i.scale([i.image.get_size()[0]*4,i.image.get_size()[1]*4])

        self.fullscreen = Button(full_screen_sprite,
                                 [self.position[0]+self.size[0]*0.1,
                                  self.position[0]+self.size[0]*0.4],
                                  font.Font("Resources/PixeloidSans.ttf","Fullscreen",
                                            [self.position[0]+self.size[0]*0.28,self.position[0]+self.size[0]*0.46],
                                            25, is_centered=True),
                                  command=self.change_fullscreen)

        self.add_widget(self.display_title)
        self.add_widget(self.resolution)
        self.add_widget(self.resolutions)
        self.add_widget(self.fullscreen)

    def change_fullscreen(self):
        # it ocurrs an error when calling toggle_fullscreen() when the size of the screen isnt in the list_modes()
        if(pygame.display.get_window_size() in pygame.display.list_modes()):
            pygame.display.toggle_fullscreen()

    def update(self):
        if(button := event_handler.EventHandler().check_events("Mouse button down")):
            
            pos_of_window = [button.pos[0]-self.position[0],button.pos[1]-self.position[1]]
            if(button.button == 1 and not self.window.get_rect().collidepoint(pos_of_window)):
                self.is_active = False

        self.fullscreen.update()
        self.resolutions.update()