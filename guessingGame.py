import random
print("Number guessing game")


x = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:    
    numberGuessed = int(input("Enter your guess: "))

    if numberGuessed == x:
        print("Congratulations YOU WIN!!")
        break

    elif numberGuessed < x:
        print("Your guess was too low: Guess a number higher than", numberGuessed)

    else:
        print("Your guess was too high: Guess a number lower than",numberGuessed)

    
    chances += 1



if not chances < 5:
    print("YOU LOSE!!! The number is", x)