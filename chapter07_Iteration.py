# while
for i in range(1,7):
    print(2*i,end = "   ")
print()

# page101
import random

rng = random.Random()
number = rng.randrange(1,1000)

guesses = 0
msg = ''

#while True:
#    guess = int(input(msg + '\nGuess my number between 1 and 1000: '))
#    guesses += 1
#    if guess > number:
#        msg += str(guess) + ' is too high.\n'
#    elif guess < number:
#        msg += str(guess) + ' is too low.\n'
#    else:
#        break

#input('\n\nYou got it in {0} guesses!\n\n'.format(guesses))

# continue 
for i in [12,16,17,24,29,30]:
    if i % 2 == 1:
        continue
    print(i)
print("done")

# 7.21
celebs = [("Brad Pitt",  1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]
print(celebs)
print(len(celebs))

for (name,year) in celebs:
    if year < 1980:
        print(name)

# 7.22
students = [
    ("John", ['CompSci', 'Physics']),
    ("Vusi", ['Maths', 'CompSci', 'Stats']),
    ("Jess", ['CompSci', 'Accounting', 'Economics', 'Management']),
    ("Zuki", ['Maths', 'Economics', 'Management']),
]

for (name, subs) in students:
    print(name, ' takes ', len(subs), ' courses.')

counter = 0
namelist = ''
for (name, subs) in students:
    for s in subs:
        if s == 'CompSci':
            counter += 1
            namelist += str(name) + ', '

print(namelist, 'take computerscience, in total ', counter)