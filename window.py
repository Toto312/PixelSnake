import pygame

import font
import sprite
import event_handler

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
    def __init__(self, size, position):
        super().__init__(position)

        self.size = size

        self.image_selected = sprite.Sprite("Resources/gui/option_waterfall.png")
        self.image_selected.scale(size)

        self.image_unselected = sprite.Sprite("Resources/gui/option_waterfall_unselected.png")
        self.image_unselected.scale(size)

        self.image_middle_option = sprite.Sprite("Resources/gui/option_waterfall_middle_option.png")
        self.image_middle_option.scale(size)

        self.image_final_option = sprite.Sprite("Resources/gui/option_waterfall_final_option.png")
        self.image_final_option.scale(size)

        self.is_selected = False

    def draw(self, window):
        window.blit(self.image,self.image_unselected)

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
        if(button := event_handler.EventHandler().check_events("Mouse button down")):
            pos_of_window = [button.pos[0]-self.position[0],button.pos[1]-self.position[1]]
            if(button.button == 1 and not self.window.get_rect().collidepoint(pos_of_window)):
                self.is_active = False

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
        image.scale([image.image.get_size()[0]*10,image.image.get_size()[1]*10])

        super().__init__(image.image.get_size(),[100,100],(102,102,102))
        self.window = image.image

        self.display_title = Label("Display","Resources/PixeloidSans.ttf",20,
                                   [self.position[0]+self.size[0]*0.2,self.position[0]+self.size[0]*0.1])

        self.resolution = Label("Resolution: ","Resources/PixeloidSans.ttf",30,
                                [self.position[0]+self.size[0]*0.45,self.position[0]+self.size[0]*0.3])

        self.add_widget(self.display_title)
        self.add_widget(self.resolution)

        print(self.widgets)