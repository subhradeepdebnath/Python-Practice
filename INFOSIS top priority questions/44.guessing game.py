# Write a program to  make a guessing game between 1 to 100;If guessing is lower than target value then print too low if value is greater than target the print too high if target is value then print Game over.
import random
target=random.randint(1,100)
for i in range(n):
    n=int(input())
    if i>target:
        print("too high")
        break
    elif i<target:
            print("too low")
            break
    else:
        print("game over")
        break


# import random

# target = random.randint(1, 100)

# while True:
#     guess = int(input("Enter your guess: "))

#     if guess == target:
#         print("🎉 Correct! You won.")
#         break   # Game over
#     elif guess < target:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")