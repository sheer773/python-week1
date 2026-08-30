import random

n = random.randint(1, 100)
guesses = 0

while(True):
    guesses += 1
    user = int(input("Guess the number (1-100): "))
    
    if(user > n):
        print("Lower number please")
    elif(user < n):
        print("Higher number please")
    else:
        print(f"Correct! You guessed in {guesses} attempts")
        break