from pynput import keyboard
import keyboard
import re
import pyautogui
import pyperclip
import time


'''
filter the string():



'''

# keyboard listener

def on_press(key):
    if key == keyboard.KeyCode.from_char('²'):
        search_item("solomonk")


keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()




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
    pyautogui.press('enter')
    time.sleep(.8)
    pyautogui.click(first_item_found)

def search_mult(items):
    for item in items:
        search_item(item)
        keyboard.wait("²")
    
    
    


while True:
    pass










