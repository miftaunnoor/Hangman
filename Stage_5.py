import random

print("H A N G M A N")
print()

types= ['python', 'java', 'kotlin', 'javascript']
r= random.choice(types)

print("-"*len(r))
guess = len(r)*["-"]

for i in range(0,8):
    letter=  input("Input a letter: ") 
    idx = 0
    if letter in r:
        for i in r:
            if i == letter:
                guess[idx] = letter
            idx+=1  
        print("")  
        print("".join(guess))
    else:
        print("That letter doesn't appear in the word")
        print("")     
        print("".join(guess))
print ('''Thanks for playing!
We'll see how well you did in the next stage''')