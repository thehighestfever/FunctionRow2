# Function Row 2 designed by thehighestfever
# https://github.com/thehighestfever/FunctionRow2

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

keyboard.col_pins = (board.D9, board.D8, board.D7, board.D6, board.D5, board.A0, board.SCK, board.MISO, board.MOSI, board.D10, board.A1, board.A2, board.A3)
keyboard.row_pins = (board.D2,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.D3, board.D4, None, False),)


keyboard.keymap = [
    [KC.MUTE, KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19, KC.F20, KC.F21, KC.F22, KC.F23, KC.F24]
]


# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = [ ((KC.VOLU, KC.VOLD, KC.MUTE),), # Standard 
                        ]

if __name__ == '__main__':
    keyboard.go()