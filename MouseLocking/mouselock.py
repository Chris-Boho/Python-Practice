#! python3
import pyautogui
import sys

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        fin_x = str(x).rjust(4)
        fin_y = str(y).rjust(4)
        positionStr = 'X: ' + fin_x + ' Y: ' + fin_y
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

        if int(fin_x) > 2559 and int(fin_y) > 1079:
            print('Moving...\n')
            pyautogui.moveTo(2559, 1079)

except KeyboardInterrupt:
    print('\n')
