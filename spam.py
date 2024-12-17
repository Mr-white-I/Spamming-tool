import pyautogui as py

message = "sorry"

counter = 1
while True:
    numbered_message = f"{counter}. {message}"
    py.typewrite(numbered_message)
    py.press("enter")
    counter += 1

