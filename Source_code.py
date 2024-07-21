from os import system
from random import randint
from time import sleep

number = randint(1, 100)
count = 1

system("color 0f")
print('Guess the number! (from 1 to 100).')
sleep(1.3)

while True:
    system("color 07")
    enter = input('Please enter the number you want to guess...')
    try:
        enter = int(enter)
        if enter == number:
            system("cls")
            system("color 0a")
            print('Congrats! you have guessed the right number!\nYou have guessed the number for', count, 'times!')
            break

        else:
            count = count + 1
            if enter < number:
                system("cls")
                system("color 0b")
                print('Try again!\nThe number is bigger than you guessed!')
                sleep(1)

            elif enter > number:
                system("cls")
                system("color 0e")
                print('Try again!\nThe number is smaller than you guessed!')
                sleep(1)

    except:
        system("cls")
        system("color 0c")
        print('Something went wrong...\nMaybe you type a wrong thing instead of number?')
        sleep(2)
        system("cls")

system("pause")