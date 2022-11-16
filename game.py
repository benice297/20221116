import random

upper = 100
under = 1

ans = random.randint(under,upper)

for i in range(5):

    guess = int(input("Please input a number:"))

    if guess < ans:
        under = guess 
    elif guess >ans :
        upper = guess
    else:
        print("Congrats")
        break


    print(under,upper)
