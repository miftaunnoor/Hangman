import random

print("H A N G M A N")

types= ['python', 'java', 'kotlin', 'javascript']
r= random.choice(types)

guess = len(r)*["-"]
lives= 8
correct_letters = []
incorrect_letters = []
alphabets= "abcdefghijklmnopqrstuvwxyz"

while lives>0:
    print("")
    print("".join(guess))
    letter=  input("Input a letter: ") 
    idx = 0
    if len(letter)>1 or len(letter)== 0:
        print ("You should input a single letter")
        continue
    elif (letter in correct_letters):
        print("You've already guessed this letter")
        continue
    elif letter not in alphabets:
        print ("Please enter a lowercase English letter")
    elif  letter.isupper():
        print("Please enter a lowercase English letter")
    elif letter in incorrect_letters:
        print("You've already guessed this letter")
    elif letter in r:
        correct_letters.append(letter)
        for i in r:
            if i == letter:
                guess[idx] = letter
            idx+=1  
        print()
        if r == "".join(guess):
            print(r)
            print(f"You guessed the word, {r}!")
            print("You survived!")
            break
    else:
        lives=lives-1
        incorrect_letters.append(letter)
        print("That letter doesn't appear in the word")
if r != "".join(guess):
    print("You lost!")
