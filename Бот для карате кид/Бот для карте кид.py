import pyautogui
import time

import keyboard

pixsel1 = (893, 660)
pixsel2 = (1031, 660)
color = (167, 92, 42)

arr = []
arr.append(0)
def start_execution():
    flag = True
    print("Клавиша 's' была нажата. Начало выполнения кода.")
    i = 0

    while flag:
        if keyboard.is_pressed('a'):
            flag = False
            print("Остановлен")

        time.sleep(0.14)
        pix = pyautogui.pixel(908, 491)


        if pix[0] > 250:
            arr.append(1)
        else:
            arr.append(0)

        if arr[i] == 1:
            key_pressed = 'left'
        else:
            key_pressed = 'right'
        i += 1
        print(i)
        print(pix)
        keyboard.send(key_pressed)
        time.sleep(0.14)
        keyboard.send(key_pressed)
        print(f"Нажата клавиша: {key_pressed}")






keyboard.add_hotkey('s', start_execution)
keyboard.wait('q')


