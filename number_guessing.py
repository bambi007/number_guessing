import random

random_number = random.randint(1, 99)
print(random_number)


guess = int(input("Enter a number from 1 to 99: "))

while random_number != guess:
    if guess < random_number:
        print("The number is higher")
        guess = int(input("Enter a number from 1 to 99: "))
    elif guess > random_number:
        print("The number is lower")
        guess = int(input("Enter a number from 1 to 99: "))
    else:
        break

print("You guessed it!")
