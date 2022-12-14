import random

with open("word.txt") as f:
    dictionary = f.read().splitlines()

answer = random.choice(dictionary)

print(answer)

count = 5
while count > 0:

    guess = (input("Type your guess :"))

    result = ""

    for i in range(5):
        if guess[i] == answer[i]:
            result = result + 'A'
        elif guess[i] in answer:
            result = result + 'B'
        else:
            result = result + 'X'

    if result == "AAAAA":
        print("Correct!")
        break
    
    print(result)

count = count - 1
