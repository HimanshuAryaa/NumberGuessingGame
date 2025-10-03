import random

def start_game():
    print('🎯 Welcome to Number Guessing Game!')
    first_user = input('What is your  name? ').title()
    print(f'Welcome {first_user}')
    print(f'You have 3 chances to guess a number.')
    print(f'If you Guess right even once you win.')
    user_win = 0

    for i in range(3):
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue
        computer_guess = random.randrange(1, 101)
        print(f'Computer guess is {computer_guess}')
        if user_guess == computer_guess:
            print('🎉 You guessed right!')
            user_win += 1
        elif user_guess > computer_guess:
            print('You guessed higher!')
        elif user_guess < computer_guess:
            print('You guessed lower!')
    if user_win > 0:
        print(f'✅ You win! You guessed right {user_win} times!')
    else:
        print(f'❌ You lose! Better luck next time!')

start_game()
