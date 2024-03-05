def guesstarget(target, guess):
    if target == guess:
        return 0 
        
    elif target < guess:
        return -1 
    else:
        return 1 
    
def gentarget():
    import random
    return random.randint(1, 20)

print("Welcome to **Guess My Number!**\nI'm thinking of a number between 1 and 20.\nYou have to guess it in as 10 attempts possible.")
target = gentarget()
for i in  range(11):
    print("Attempt %s" % (i+1))
    guess = int(input("Enter your guess:"))
    result = guesstarget(target,guess)
    if  result == 0:
        print("Congratulations! You guessed the number.")
        break
    elif  result == -1:
        print("Your guess is too high. Try again.")
    elif  result == 1:
        print("Your guess is too low. Try again.")


