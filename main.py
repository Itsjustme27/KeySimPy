import pyautogui
import time

def simulate_key_press():
    pyautogui.press('ctrl')

def main():
    try:
        while True:
            simulate_key_press()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Script terminated by user")

if __name__ == "__main__":
    print("Starting key press simulation. Press CTRL + C to stop")
    time.sleep(5)
    main()

