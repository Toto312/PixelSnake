import font
import time_game
import utils

class DebugInfo(metaclass=utils.SingletonMeta):
    def __init__(self):
        self.is_active = False

    def change_state(self, state) -> None:
        self.is_active = state