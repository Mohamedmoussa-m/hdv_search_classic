from pynput import keyboard
import keyboard as kb
import re
import pyautogui
import pyperclip
import time


'''
filter the string():



'''

# keyboard listener

def on_press(key):
    if key == keyboard.Key.f8:
        main()




# keyboard_listener = keyboard.Listener(on_press=on_press)
# keyboard_listener.start()




# CONSTANTS
clear_search = (566, 202)
search_bar = (400, 204)
first_item_found = (767, 231)





def extract_equipment_names(message):
    pattern = r"\[([^\]\d]+)\]"
    equipment_names = re.findall(pattern, message)
    return equipment_names

def copy_selection():
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste()
    return text

def gather_items():
    message = copy_selection()
    items = extract_equipment_names(message)
    return items

def search_item(item):
    pyperclip.copy(item)
    pyautogui.click(clear_search)
    time.sleep(.5)
    pyautogui.click(search_bar)
    time.sleep(.1)
    pyautogui.hotkey('ctrl', 'v') 
    kb.press('enter')
    time.sleep(.8)
    pyautogui.click(first_item_found)

def search_mult(items):
    for item in items:
        print(f"{item}")
        kb.wait("tab")
        search_item(item)
        

def main():
    items = gather_items()
    search_mult(items)


with keyboard.Listener(on_press=on_press) as keyboard_lisener:
    keyboard_lisener.join()





