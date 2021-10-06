import random

print("H A N G M A N")
print()

types= ['python', 'java', 'kotlin', 'javascript']
r= random.choice(types)

guess = len(r)*["-"]
lives= 8
correct_letters = []

while lives!=0:
    print("".join(guess))
    letter=  input("Input a letter: ") 
    idx = 0
    if (letter in correct_letters):
        if lives == 1:
            print("No improvements")
        else:
            print("No improvements")
            print("")
        lives = lives - 1

    elif letter in r:
        correct_letters.append(letter)
        for i in r:
            if i == letter:
                guess[idx] = letter
            idx+=1  
        print()
        if r == "".join(guess):
            print(r)
            print("You guessed the word!")
            print("You survived!")
            break
    else:
        lives = lives - 1
        if lives == 0:
            print("That letter doesn't appear in the word")
        else:
            print("That letter doesn't appear in the word")
            print()
if r != "".join(guess):
    print("You lost!")