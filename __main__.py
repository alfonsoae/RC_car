from curses import wrapper
from components import HardServo
from time import sleep


def main(stdscr):
    try:
        stdscr.nodelay(True)
        
        servo = HardServo(12, 50, 3.4, 13)
        pressedKeys = set()
        
        run = True
        while run: 

            while stdscr.getch() != -1 :
                pressedKeys.add(stdscr.getch())
            

            if ord('a') in pressedKeys:
                servo.update(1)    

            if ord('d') in pressedKeys:
                servo.update(-1)
            
            print(pressedKeys)
            pressedKeys = set()
            sleep(5)
    finally:
        servo.clean()

wrapper(main)
