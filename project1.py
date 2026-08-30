import random

#s = Snake, w = Water, g = Gun
choices = ["s", "w", "g"]

computer = random.choice(choices)
you = input("Enter s for Snake, w for Water, g for Gun: ").lower()

print(f"Computer chose: {computer}")
print(f"You chose: {you}")

if(computer == you):
    print("Draw!")
elif(computer == "s" and you == "w"):
    print("You Lose! Snake drank Water")
elif(computer == "s" and you == "g"):
    print("You Win! Gun killed Snake")
elif(computer == "w" and you == "s"):
    print("You Win! Snake drank Water")
elif(computer == "w" and you == "g"):
    print("You Lose! Water drowned Gun")
elif(computer == "g" and you == "s"):
    print("You Lose! Gun killed Snake")
elif(computer == "g" and you == "w"):
    print("You Win! Water drowned Gun")