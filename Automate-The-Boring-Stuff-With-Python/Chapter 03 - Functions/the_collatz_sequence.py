#! python3
# the_collatz_sequence.py - Take user input num and prints collatz sequence


def collatz(num):
    print(num)
    while num != 1:
        if int(num) % 2:
            num = 3 * num + 1
        else:
            num = num // 2
        print(num)


user_num = input('Enter a number ')
collatz(user_num)
