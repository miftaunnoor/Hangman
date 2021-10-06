import random
print('''H A N G M A N
The game will be available soon.''')

word= str(input())

types= ['python', 'java', 'kotlin', 'javascript']
print("Guess the word:")

print(random.choice(types))
r= random.choice(types)
if  word==r:
    print("You survived!")
else:
    print("You lost!")
