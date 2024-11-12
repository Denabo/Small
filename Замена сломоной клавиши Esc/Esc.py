from pynput import keyboard

def on_press(key):
    try:
        # Если нажата клавиша 'ё' или '1', нажать 'Esc'
        if key.char in ('1'):
            # Эмулировать нажатие 'Esc'
            keyboard.Controller().press(keyboard.Key.esc)
            keyboard.Controller().release(keyboard.Key.esc)
    except AttributeError:
        # Игнорировать любые другие клавиши
        pass

def main():
    # Создать слушателя клавиш
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()