import random

number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Вгадайте число від 1 до 10: "))
    if guess == number:
        print("Вітаю! Ви вгадали!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")
    attempts -= 1

if attempts == 0:
    print(f"Ви програли. Загадане число було {number}.")