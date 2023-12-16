import pygame

import utils

class Button:
	def __init__(self, name, buttons):
		self.name = name
		
		if(isinstance(buttons, list)):
			self.buttons = buttons
		else:
			try:
				self.buttons = list(buttons)
			except:
				self.buttons = [buttons]


class EventHandler(metaclass=utils.SingletonMeta):
	def __init__(self):
		self.is_active = pygame.get_init()

		self.keys_pressed = None
		self.mouse_position = [-1,-1]
		self.is_right_mouse_clicked = False
		self.is_left_mouse_clicked = False

		self.events = {pygame.KEYDOWN: None, pygame.QUIT: None, pygame.MOUSEMOTION: None, pygame.MOUSEBUTTONDOWN:None, pygame.MOUSEBUTTONUP:None,pygame.VIDEORESIZE:None}
		self.event_types = {"Key down": pygame.KEYDOWN, "Key up" : pygame.KEYUP, "Quit": pygame.QUIT, "Mouse motion": pygame.MOUSEMOTION,
					  "Mouse button down": pygame.MOUSEBUTTONDOWN, "Mouse button up": pygame.MOUSEBUTTONUP,
					  "Video resize" : pygame.VIDEORESIZE}
		
		self.buttons = [Button("up",[pygame.K_UP, pygame.K_w]),Button("down",[pygame.K_DOWN, pygame.K_s]),
				  		Button("left",[pygame.K_LEFT, pygame.K_a]),Button("right",[pygame.K_RIGHT, pygame.K_d])]

		self.is_control_key_pressed = False
		self.is_alt_key_pressed = False

	def add_button(self, button: Button):
		self.buttons.append(button)

	def del_button(self, name):
		for i in self.buttons:
			if(i.name == name):
				self.buttons.remove(i)

	def get_event_key(self, name: str) -> int:
		try:
			value = self.event_types[name]
			return value
		except KeyError:
			return None

	def return_event_types(self) -> dict:
		return self.event_types

	def create_event(self, name: str) -> None:
		self.add_event(name, pygame.event.custom_type())

	def add_event(self, name: str, event_key: int) -> None:
		self.event_types.update({name: event_key})

	def is_button_pressed(self, name):
		for i in self.buttons:
			if(i.name == name):
				if(button := self.check_events("Key down")):
					if(button.key in i.buttons):
						return True
		return False

	def update(self) -> None:
		if(not self.is_active):
			return

		self.keys_pressed = pygame.key.get_pressed()

		for i in self.event_types.values():
			self.events[i] = pygame.event.get(i)

		#check mouse events
		if(mouse := self.check_events("Mouse motion")):
			self.mouse_position = mouse.pos		

		if(mouse_clicked := self.check_events("Mouse button down")):
			#if it clicked on the left
			if(mouse_clicked.button == 1):
				self.is_left_mouse_clicked = True
				self.is_right_mouse_clicked = False
			#if it clicked on the right
			elif(mouse_clicked.button == 3):
				self.is_right_mouse_clicked = True
				self.is_left_mouse_clicked = False
		else:
			self.is_left_mouse_clicked = False
			self.is_right_mouse_clicked = False

		if(key := self.check_events("Key down")):
			# Control
			if(key.scancode == 224):
				self.is_control_key_pressed = True
			# Alt left
			elif(key.scancode == 226):
				self.is_alt_key_pressed = True
		else:
			self.is_control_key_pressed = False
			self.is_alt_key_pressed = False

	def check_keys_pressed(self, keycode: int) -> bool:
		return self.keys_pressed[keycode]

	def check_events(self, type_event: str) -> pygame.event:
		try:
			events = self.events[self.event_types[type_event]]
			if(events == []):
				return None
			return events[0]
		except KeyError:
			return None

if(__name__=="__main__"):
	pass
