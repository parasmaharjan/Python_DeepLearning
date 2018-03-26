import random
print('Guess the number game...')
print('Please guess the number between 0 to 9')

random_number = random.randint(0,9)

print(random_number)

guess = int(input("Guess the number: "))

if guess > random_number:
    print("Your guess is greater")
elif guess < random_number:
    print("Your guess it less")
else:
    print("Hurray! You guessed it right")