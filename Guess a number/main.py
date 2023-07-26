import random

# ## The user guess the compute's Secret number
# def guess(x):
#     random_number = random.randint(1,x)
#     print(random_number)
#     guess =0
    
#     while guess!=random_number:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess<=x: 
#             if guess < random_number:
#                 print("It is TOO LOw 📉📉")
#             elif guess > random_number:
#                 print("It is TOO HIGH 📈📈")
#         else:
#             print(f" ⛔⛔Out of Guess range, It must be between 1 and {x}")
#     print(f"🪘🪘🪘 Yaa!! You guess the {random_number} Correctly!!")

# your_range = int(input("Your Guess range From 1 to ??: "))
# guess(your_range)

## The computer guess my secret number

print("The Computer guess my number 🧑‍💻")

def computer_gues(x):
    print("LET ASSUME MY NUMBER IS 5")
    low =1
    high =x
    my_feedback = ''
    computer_guess=0
    while my_feedback !='c':
        if low!=high:
            computer_guess = random.randint(low,high)
        else:
            computer_guess = low # It could be High b/c low == high
        my_feedback = input(f' Is {computer_guess} Press\n H.If it is too High: \n L.If it is to Low:  \n C.If it is Correct: ')
        if my_feedback.lower() =='h':
            high = computer_guess-1
        elif my_feedback.lower() == 'l':
            low = computer_guess+1
    print(f'The Computer Guess your number, {computer_guess} Correctly!!')
computer_gues(10)  
 