import keyboard

def delete():
  keyboard.press_and_release("ctrl+a")
  keyboard.press_and_release("backspace")

keyboard.add_hotkey('backspace', delete)

keyboard.wait("alt+`")