#! python3
# the_collatz_sequence_input_validation.py - Take user input num and prints collatz sequence, with input validation


def collatz(num):
    try:
        print(num)
        while num != 1:
            if int(num) % 2:
                num = 3 * num + 1
            else:
                num = num // 2
            print(num)
    except ValueError:
        print('Must enter an integer!')


user_num = input('Enter a number ')
collatz(user_num)
