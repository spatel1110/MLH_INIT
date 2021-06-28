import random

number = random.randint(1, 20)

player_name1 = input("Hello, What's your name?\n")
player_name2 = input("Hello, What's your name?\n")

number_of_guesses = 0
guess_left = 5

while number_of_guesses < 5:
    print(f'okay {player_name1}!!\nyou can guess number between 1 and 20:')
    guess1 = int(input())
    print(f'okay {player_name2}!!\nyou can guess number between 1 and 20:')
    guess2 = int(input())
    number_of_guesses += 1
    if (guess1 == number):
        print(f"We have a winner! {player_name1} got the answer")
        print(f"{player_name1} you did it in {number_of_guesses} times")
        break
    elif (guess2 == number):
        print(f"We have a winner! {player_name2} got the answer")
        print(f"{player_name2} you did it in {number_of_guesses} times")
        break
    else:
        if (number_of_guesses == 5):
            print("sorry Game Is Over !")
            break
        print("Please try again you entered the wrong number")
        print(f"You have only {guess_left} chance left !!")
        guess_left -= 1


