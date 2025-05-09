import random

def get_hint(number):
    hints = []
    
    if number % 2 == 0:
        hints.append("The number is even.")

    else:
        hints.append("The number is odd")

    if number % 5 == 0:
        hints.append("The number is divisible by 5")

    if number > 25:
        hints.append("The number is greater than 25")

    else:
        hints.append("The number is less than 25")
    
    return random.sample(hints, k=min(2, len(hints)))

def number_guessing_game():
    print("🎯 Welcome to an advanced number guessing game!")
    print("As this is bit advanced, so go on now, choose a difficulity level")
    print("1.Easy(10 tries)\n 2.Medium(7 tries)\n 3.Hard(5 tries)")

    level_tries = {"1": 10,"2": 7,"3": 5}

    while True:
        difficulty = input("Enter difficulty(1,2,3): ")

        if difficulty in level_tries:
            tries_left = level_tries[difficulty]
            break
        else:
            print("Insert a valid input please!")
    number_to_guess = random.randint(1, 50)
    attempts = 0

    while tries_left > 0:
        try:
            guess = int(input(f"\nYou have {tries_left} tries left. Make a guess!: "))
            attempts += 1

            if guess < 0 or guess > 50:
                print("🚫 Please choose a valid number between 1 and 50")
                continue
            
            if guess == number_to_guess:
                print(f"✅ Congratulation, You beat the game in {attempts} attempts!")
                return
            
            elif guess < number_to_guess:
                print("📈 Try a higher number")
            else:
                print("📉 Try a lower number!")

            tries_left -= 1

            if attempts == 3:
                print(f"💡 Hint: {' | '.join(get_hint(number_to_guess))}")
            
        except ValueError:
            print("Enter a valid number")
        
    else:
            print(f"❌ You ran out of attemots! SAD!\nThe number was {number_to_guess}")
    
    while True:
        replay = input("\n🔁 Do you wanna try again? (y/n): ").strip().lower()

        if replay == "y":
            number_guessing_game()
            return
        elif replay == "n":
            break
        else:
            print("❓ please enter 'y' for continue playing the game and 'n' for exiting the game")

    while True:
        if input("\n🚪 Please press enter to exit") == "":
                break

if __name__ == "__main__":
    number_guessing_game()
        

