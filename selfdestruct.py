import keyboard
import mouse


keyboard.add_hotkey("ctrl+up",mouse.move(9,-10))
keyboard.add_hotkey("ctrl+down",mouse.move(9,10))
keyboard.add_hotkey("ctrl+right",mouse.move(19,0))
keyboard.add_hotkey("ctrl+left",mouse.move(-10,0))
keyboard.add_hotkey("ctrl+z",mouse.click(mouse.LEFT))
keyboard.add_hotkey("ctrl+x",mouse.click(mouse.RIGTHT))


keyboard.wait("ctrl+esc")
input()
