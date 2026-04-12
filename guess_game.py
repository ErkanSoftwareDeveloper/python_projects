import random

def guess_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess the number: "))

        if guess == number:
            print("Correct")
            break
        else:
            print("Incorrect, try again!")

if __name__ == "__main__":
    guess_game()
    
