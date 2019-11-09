#! python 3
# stopwatch.py - A simple stopwatch program
# usage: start and press enter to do laps, ctrl-c to exit

import time, pyperclip

# display instructions
input('Press any key to begin. Afterwards, press ENTER to click stopwatch.')
print('Started. Press Ctrl-C to quit.')
# get first lap start time
start_time = time.time()
last_time = start_time
lap_num = 1
output = ''
try:
    # start tracking the lap times
    while True:
        # waits for input
        input()
        # round to nearest 2 decimal places precision
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        # print(f'Lap # {str(lap_num).rjust(width=2, fillchar=" ")}: {str(total_time).rjust(width=6, fillchar=" ")} ({str(lap_time).rjust(width=6, fillchar=" ")})', end='')
        print(f'Lap # {str(lap_num).rjust(2, " ")}: {str(total_time).rjust(6, " ")} ({str(lap_time).rjust(6, " ")})', end='')
        output = output + f'Lap # {str(lap_num).rjust(2, " ")}: {str(total_time).rjust(6, " ")} ({str(lap_time).rjust(6, " ")})\r\n'
        # reset lap time
        last_time = time.time()
        lap_num += 1
# handle CTRL-C
except KeyboardInterrupt:
    # copy to clipboard
    if output != '':
        pyperclip.copy(output)
        print('\nInformation copied to clipboard.')
    else:
        print('\nExited before full lap.')




