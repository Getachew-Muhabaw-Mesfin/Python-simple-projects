import random

def guess(x):
    random_number = random.randint(1,x)
    print(random_number)
    guess =0
    
    while guess!=random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess<=x: 
            if guess < random_number:
                print("It is TOO LOw 📉📉")
            elif guess > random_number:
                print("It is TOO HIGH 📈📈")
        else:
            print(f" ⛔⛔Out of Guess range, It must be between 1 and {x}")
    print(f"🪘🪘🪘 Yaa!! You guess the {random_number} Correctly!!")

your_range = int(input("Your Guess range From 1 to ??: "))
guess(your_range)