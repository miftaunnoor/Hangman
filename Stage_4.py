import random
print("H A N G M A N")

types= ['python', 'java', 'kotlin', 'javascript']
print("Guess the word:")

print(random.choice(types))
r= random.choice(types)

first= r [0:3]
last= '-'*(len(r)-3)
print (first+last)
word_guess= str(input())
if word_guess== r:
    print ("You survived!")
else:
    print("You lost!")
