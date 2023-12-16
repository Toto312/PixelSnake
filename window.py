import pygame
import os

import font
import sprite
import event_handler
import scene_manager
import debug
import math
import volume
import save

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
        super().__init__(position)
        
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
                if(self.command):
                    self.command()
                if(len(self.sprites)>1):
                    self.change_next_image()

    def change_next_image(self):
        self.mode = (self.mode+1) % len(self.sprites)

    def change_image_index(self, i):
        self.mode = i

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
        self.is_active = True

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
        
        if(resolution != list(pygame.display.get_surface().get_size()) and not pygame.display.is_fullscreen()):
            pygame.display.set_mode(resolution,pygame.RESIZABLE)
            scene_manager.SceneManager().curr_scene.resize(resolution)
            save.SaveFile().change_value("resolution",f"{resolution[0]}x{resolution[1]}")

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


class Volume(Widget):
    def __init__(self, position):
        super().__init__()
        
        volume = sprite.Sprite("Resources/gui/volume.png")
        volume.scale([volume.image.get_size()[0]*5,volume.image.get_size()[1]*5])
        
        volume1 = sprite.Sprite("Resources/gui/volume1.png")
        volume1.scale([volume1.image.get_size()[0]*5,volume1.image.get_size()[1]*5])
        
        volume2 = sprite.Sprite("Resources/gui/volume2.png")
        volume2.scale([volume2.image.get_size()[0]*5,volume2.image.get_size()[1]*5])
        
        volume3 = sprite.Sprite("Resources/gui/volume3.png")
        volume3.scale([volume3.image.get_size()[0]*5,volume3.image.get_size()[1]*5])
        
        volume4 = sprite.Sprite("Resources/gui/volume4.png")
        volume4.scale([volume4.image.get_size()[0]*5,volume4.image.get_size()[1]*5])
        
        self.level = pygame.Rect((9-14)*5,0,14*5,13*5)
        self.level1 = pygame.Rect(9*5,0,14*5,13*5)
        self.level2 = pygame.Rect(23*5,0,14*5,13*5)
        self.level3 = pygame.Rect(37*5,0,14*5,13*5)
        self.level4 = pygame.Rect(51*5,0,14*5,13*5)
        
        self.level.move_ip(position[0],position[1])
        self.level1.move_ip(position[0],position[1])
        self.level2.move_ip(position[0],position[1])
        self.level3.move_ip(position[0],position[1])
        self.level4.move_ip(position[0],position[1])

        self.curr_image = 0
        self.get_curr_volume()
        self.images = [volume,volume1,volume2,volume3,volume4]
        self.position = position

    def get_curr_volume(self):
        vol = float(volume.Volume().volume)
        print(vol)
        dou = math.ceil(vol*4)
        self.curr_image = dou

    def update(self):
        if(key := event_handler.EventHandler().check_events("Mouse button down")):
            if(key.button == 1 and self.level.collidepoint(key.pos)):
                volume.Volume().volume = 0
                pygame.mixer.music.set_volume(0)
                self.curr_image = 0
            elif(key.button == 1 and self.level1.collidepoint(key.pos)):
                volume.Volume().volume = 0.25
                pygame.mixer.music.set_volume(0.25)
                self.curr_image = 1
            elif(key.button == 1 and self.level2.collidepoint(key.pos)):
                volume.Volume().volume = 0.5
                pygame.mixer.music.set_volume(0.5)
                self.curr_image = 2
            elif(key.button == 1 and self.level3.collidepoint(key.pos)):
                pygame.mixer.music.set_volume(0.75)
                volume.Volume().volume = 0.75
                self.curr_image = 3
            elif(key.button == 1 and self.level4.collidepoint(key.pos)):
                pygame.mixer.music.set_volume(1)
                volume.Volume().volume = 1
                self.curr_image = 4
            
            save.SaveFile().change_value("volume",f"{volume.Volume().volume}")

    def draw(self, window):
        window.blit(self.images[self.curr_image].image,self.position)

        if(debug.DebugInfo().is_active):
            pygame.draw.rect(window,(0,0,0),self.level)
            pygame.draw.rect(window,(255,0,0),self.level1)
            pygame.draw.rect(window,(0,255,0),self.level2)
            pygame.draw.rect(window,(0,0,255),self.level3)
            pygame.draw.rect(window,(124,124,124),self.level4)


class Entry(Widget):
    def __init__(self, id, position, font_position, max_len=10, text=""):
        super().__init__(position)
        
        self.id = id

        self.images = [sprite.Sprite("Resources/gui/entry.png"),sprite.Sprite("Resources/gui/entry_pressed.png")]
        for i in self.images:
            i.scale([i.image.get_size()[0]*2,i.image.get_size()[1]*2.5])
        self.mode = 1

        self.rect_image = self.images[self.mode].image.get_rect()
        self.rect_image.move_ip(self.position)

        self.entry_is_active = False
        self.initial_text = text
        self.text = self.initial_text
        self.time_last_backspace = 0 #[self.position[0]*1.125,self.position[1]*1.15]
        self.font = font.Font("Resources/PixeloidSans.ttf",self.text,font_position,20)
        self.max_len = max_len

    def update(self): 
        self.get_key()

        if(mouse := event_handler.EventHandler().check_events("Mouse button down")):
            if(self.rect_image.collidepoint(mouse.pos)):
                self.entry_is_active = True
                self.mode = 0
            else:
                self.entry_is_active = False
                self.mode = 1
                if(len(self.text)==0):
                    self.text = self.initial_text

        if(self.entry_is_active):
            if(button := event_handler.EventHandler().check_events("Key down")):
                if button.key == pygame.K_RETURN:
                    self.entry_is_active = False
                elif button.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.time_last_backspace = pygame.time.get_ticks()
                else:
                    if(len(self.text)>=self.max_len):
                        self.entry_is_active = False
                        self.mode = 1
                        self.text = button.unicode
                    elif(pygame.key.name(button.key) in ["up","down","left","right","escape","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12"]):
                        self.entry_is_active = False
                        self.mode = 1
                        if(pygame.key.name(button.key)=="escape"):
                            self.text = "escape"
                        else:
                            self.text = pygame.key.name(button.key)
                    elif(button.unicode in "abcdefghijklmnopqrstuvwxyz"):
                        self.entry_is_active = False
                        self.mode = 1
                        self.text = button.unicode
                if(pygame.key.key_code(self.text)==27):
                    self.text = "escape"
                self.font.change_text(self.text)

    def get_key(self):
        if(event_handler.EventHandler().check_keys_pressed(pygame.K_BACKSPACE) and 
           pygame.time.get_ticks()-self.time_last_backspace>500 and self.entry_is_active):
            self.text = self.text[:-1]
        self.font.change_text(self.text)

    def draw(self, window):
        window.blit(self.images[self.mode].image,self.position)
        self.font.draw(window)


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
        for i in self.widgets:
            if(i.is_active):
                i.update()

    def resize(self, size):
        pass

    def add_widget(self, widget):
        self.widgets.append(widget)

    def draw(self, window):
        if(not self.is_active):
            return

        window.blit(self.window,self.position)

        for i in self.widgets:
            if(i.is_active):
                i.draw(window)

class OptionsGUI(Window):
    def __init__(self):
        self.image = sprite.Sprite("Resources/gui/options.png")
        self.image.scale([self.image.image.get_size()[0]*5,self.image.image.get_size()[1]*5])
        
        self.image1 = sprite.Sprite("Resources/gui/options1.png")
        self.image1.scale([self.image1.image.get_size()[0]*5,self.image1.image.get_size()[1]*5])
        
        self.image2 = sprite.Sprite("Resources/gui/options2.png")
        self.image2.scale([self.image2.image.get_size()[0]*5,self.image2.image.get_size()[1]*5])
        
        self.display_button = pygame.Rect(0,0,20*5,13*5)
        self.sound_button = pygame.Rect(23*5,0,20*5,13*5)
        self.buttons_button = pygame.Rect(45*5,0,20*5,13*5)


        super().__init__(self.image.image.get_size(),[100,100],(102,102,102))
        self.window = self.image.image

        self.display_button.move_ip(100,100) 
        self.sound_button.move_ip(100,100)
        self.buttons_button.move_ip(100,100)

        self.display_title = Label("Display","Resources/PixeloidSans.ttf",20,
                                   [self.position[0]+self.size[0]*0.2,self.position[0]+self.size[0]*0.1])
        
        self.sound_title = Label("Sound","Resources/PixeloidSans.ttf",20,
                                [self.position[0]+self.size[0]*0.425,self.position[0]+self.size[0]*0.1])
        
        self.buttons_title = Label("Buttons","Resources/PixeloidSans.ttf",20,
                                [self.position[0]+self.size[0]*0.675,self.position[0]+self.size[0]*0.1])

        self.add_widget(self.display_title)
        self.add_widget(self.sound_title)
        self.add_widget(self.buttons_title)
        
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
        
        full_screen_sprite = [sprite.Sprite("Resources/gui/button_release.png"),
                              sprite.Sprite("Resources/gui/button_pressed.png")]
        for i in full_screen_sprite:
            i.scale([i.image.get_size()[0]*4,i.image.get_size()[1]*4])

        self.debug = Button(full_screen_sprite,
                            [self.position[0]+self.size[0]*0.1,
                             self.position[0]+self.size[0]*0.55],
                             font.Font("Resources/PixeloidSans.ttf","Debug",
                                       [self.position[0]+self.size[0]*0.28,self.position[0]+self.size[0]*0.61],
                                       25, is_centered=True),
                             command=self.change_debug_mode)

        self.add_widget(self.resolution)
        self.add_widget(self.debug)
        self.add_widget(self.resolutions)
        self.add_widget(self.fullscreen)


        self.volume = Label("Volume: ","Resources/PixeloidSans.ttf",30,
                            [self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.3])
        self.volume.is_active = False

        self.volume_vol = Volume([self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.2])
        self.volume_vol.is_active = False

        self.add_widget(self.volume)
        self.add_widget(self.volume_vol)

        self.up_label = Label("Up: ","Resources/PixeloidSans.ttf",30,
                            [self.position[0]+self.size[0]*0.32,self.position[0]+self.size[0]*0.3])
        self.up_label.is_active = False
        
        self.down_label = Label("Down: ","Resources/PixeloidSans.ttf",30,
                            [self.position[0]+self.size[0]*0.32,self.position[0]+self.size[0]*0.4])
        self.down_label.is_active = False

        self.left_label = Label("Left: ","Resources/PixeloidSans.ttf",30,
                            [self.position[0]+self.size[0]*0.32,self.position[0]+self.size[0]*0.5])
        self.left_label.is_active = False

        self.right_label = Label("Right: ","Resources/PixeloidSans.ttf",30,
                            [self.position[0]+self.size[0]*0.32,self.position[0]+self.size[0]*0.6])
        self.right_label.is_active = False

        self.menu_label = Label("Menu: ","Resources/PixeloidSans.ttf",30,
                            [self.position[0]+self.size[0]*0.32,self.position[0]+self.size[0]*0.7])
        self.menu_label.is_active = False
   
        self.debug_label = Label("Debug: ","Resources/PixeloidSans.ttf",30,
                            [self.position[0]+self.size[0]*0.32,self.position[0]+self.size[0]*0.8])
        self.debug_label.is_active = False

        
        full_screen_sprite = [sprite.Sprite("Resources/gui/litt_button_release.png"),
                              sprite.Sprite("Resources/gui/litt_button_pressed.png")]
        for i in full_screen_sprite:
            i.scale([i.image.get_size()[0]*3,i.image.get_size()[1]*3])

        up_key_names = "up"
        down_key_names = "down"
        left_key_names = "left"
        right_key_names = "right"
        menu_key_names = "escape"
        debug_key_names = "f1"
        if(up_key := save.SaveFile().read_value("up")):
            up_key_names = pygame.key.name(int(up_key))
        if(down_key := save.SaveFile().read_value("down")):
            down_key_names = pygame.key.name(int(down_key))
        if(left_key := save.SaveFile().read_value("left")):
            left_key_names = pygame.key.name(int(left_key))
        if(right_key := save.SaveFile().read_value("right")):
            right_key_names = pygame.key.name(int(right_key))
        if(menu_key := save.SaveFile().read_value("Menu")):
            menu_key_names = pygame.key.name(int(menu_key))
        if(debug_key := save.SaveFile().read_value("Debug")):
            debug_key_names = pygame.key.name(int(debug_key))


        self.entry_up_button = Entry("up_button",[self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.22],[(self.position[0]+self.size[0]*0.35)*1.125,(self.position[0]+self.size[0]*0.22)*1.15],6,"up")
        self.entry_up_button.is_active = False
        self.entry_up_button.text = up_key_names

        self.entry_down_button = Entry("down_button",[self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.32],[(self.entry_up_button.position[0])*1.09*1.125,(self.entry_up_button.position[1])*1.2*1.15],6,"down")
        self.entry_down_button.is_active = False
        self.entry_down_button.text = down_key_names

        self.entry_right_button = Entry("left_button",[self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.42],[(self.entry_up_button.position[0])*1.02*1.125,(self.entry_up_button.position[1])*1.4*1.15],6,"left")
        self.entry_right_button.is_active = False
        self.entry_right_button.text = left_key_names

        self.entry_left_button = Entry("right_button",[self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.52],[(self.entry_up_button.position[0])*1.07*1.125,(self.entry_up_button.position[1])*1.6*1.15],6,"right")
        self.entry_left_button.is_active = False
        self.entry_left_button.text = right_key_names
        
        self.entry_menu_button = Entry("menu",[self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.62],[(self.entry_up_button.position[0])*1.16*1.125,(self.entry_up_button.position[1])*1.8*1.15],6,"escape")
        self.entry_menu_button.is_active = False
        self.entry_menu_button.text = menu_key_names

        self.entry_debug_button = Entry("debug",[self.position[0]+self.size[0]*0.35,self.position[0]+self.size[0]*0.72],[(self.entry_up_button.position[0])*0.985*1.125,(self.entry_up_button.position[1])*2.01*1.15],6,"f1")
        self.entry_debug_button.is_active = False
        self.entry_debug_button.text = debug_key_names

        self.add_widget(self.up_label)
        self.add_widget(self.down_label)
        self.add_widget(self.left_label)
        self.add_widget(self.right_label)
        self.add_widget(self.menu_label)
        self.add_widget(self.debug_label)
        self.add_widget(self.entry_up_button)
        self.add_widget(self.entry_down_button)
        self.add_widget(self.entry_left_button)
        self.add_widget(self.entry_right_button)
        self.add_widget(self.entry_menu_button)
        self.add_widget(self.entry_debug_button)

    def change_button(self):
        list_buttons = {}
        for i in event_handler.EventHandler().buttons:
            list_buttons.update({i.name : [pygame.key.name(j) for j in i.buttons]})
        for i in self.widgets:
            if(isinstance(i,Entry) and i.text != ""):
                if(i.id == "up_button" and i.text not in list_buttons["up"]):
                    new_button = event_handler.Button("up",[pygame.key.key_code(i.text)])
                    event_handler.EventHandler().del_button("up")
                    event_handler.EventHandler().add_button(new_button)
                    save.SaveFile().change_value("up",pygame.key.key_code(i.text))
                elif(i.id == "down_button" and i.text not in list_buttons["down"]):
                    new_button = event_handler.Button("down",[pygame.key.key_code(i.text)])
                    event_handler.EventHandler().del_button("down")
                    event_handler.EventHandler().add_button(new_button)
                    save.SaveFile().change_value("down",pygame.key.key_code(i.text))
                elif(i.id == "left_button" and i.text not in list_buttons["left"]):
                    new_button = event_handler.Button("left",[pygame.key.key_code(i.text)])
                    event_handler.EventHandler().del_button("left")
                    event_handler.EventHandler().add_button(new_button)
                    save.SaveFile().change_value("left",pygame.key.key_code(i.text))
                elif(i.id == "right_button" and i.text not in list_buttons["right"]):
                    new_button = event_handler.Button("right",[pygame.key.key_code(i.text)])
                    event_handler.EventHandler().del_button("right")
                    event_handler.EventHandler().add_button(new_button)
                    save.SaveFile().change_value("right",pygame.key.key_code(i.text))
                elif(i.id == "menu" and i.text not in list_buttons["Menu"]):
                    new_button = event_handler.Button("menu",[pygame.key.key_code(i.text)])
                    event_handler.EventHandler().del_button("menu")
                    event_handler.EventHandler().add_button(new_button)
                    save.SaveFile().change_value("Menu",pygame.key.key_code(i.text))
                elif(i.id == "debug" and i.text not in list_buttons["Debug"]):
                    new_button = event_handler.Button("Debug",[pygame.key.key_code(i.text)])
                    event_handler.EventHandler().del_button("Debug")
                    event_handler.EventHandler().add_button(new_button)
                    save.SaveFile().change_value("Debug",pygame.key.key_code(i.text))


    def change_fullscreen(self):
        # it ocurrs an error when calling toggle_fullscreen() and the size of the screen isnt in the list_modes()
        # also for some reason if the size is 1920x1080
        if(pygame.display.get_window_size() in pygame.display.list_modes() and pygame.display.get_window_size() != (1920,1080)):
            if(pygame.display.is_fullscreen()):
                pygame.display.set_mode(pygame.display.get_window_size(),pygame.RESIZABLE)
                scene_manager.SceneManager().curr_scene.resize(pygame.display.get_window_size())
            else:
                pygame.display.set_mode(pygame.display.get_window_size(),pygame.FULLSCREEN)
                scene_manager.SceneManager().curr_scene.resize(pygame.display.get_window_size())
                

    def change_debug_mode(self):
        debug.DebugInfo().is_active = not debug.DebugInfo().is_active

    def activate_widgets(self,*widgets):
        for i in self.widgets:
            if(i in widgets):
                i.is_active = True
            elif(i not in widgets and i!=self.display_title and i != self.sound_title and i!=self.buttons_title):
                i.is_active = False

    def update(self):
        if(not self.is_active):
            return
        
        self.change_button()

        if(debug.DebugInfo().is_active):
            self.debug.mode = 1
        else:
            self.debug.mode = 0

        if(button := event_handler.EventHandler().check_events("Mouse button down")):
            pos_of_window = [button.pos[0]-self.position[0],button.pos[1]-self.position[1]]
            if(button.button == 1 and not self.window.get_rect().collidepoint(pos_of_window)):
                self.is_active = False
            
            elif(button.button == 1 and self.display_button.collidepoint(button.pos)):
                self.activate_widgets(self.resolution,self.resolutions,
                                      self.fullscreen,self.debug)
                self.window = self.image.image
            
            elif(button.button == 1 and self.sound_button.collidepoint(button.pos)):
                self.activate_widgets(self.volume,self.volume_vol)
                self.window = self.image1.image
            
            elif(button.button == 1 and self.buttons_button.collidepoint(button.pos)):
                self.activate_widgets(self.up_label,self.down_label,self.left_label,self.right_label,
                                      self.menu_label, self.debug_label,self.entry_up_button,
                                      self.entry_down_button,self.entry_left_button,self.entry_right_button,
                                      self.entry_menu_button,self.entry_debug_button)
                self.window = self.image2.image

        for i in self.widgets:
            if(i.is_active):
                i.update()

    def draw(self, window):
        if(not self.is_active):
            return

        window.blit(self.window,self.position)

        for i in self.widgets:
            if(i.is_active):
                i.draw(window)