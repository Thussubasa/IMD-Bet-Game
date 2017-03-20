
# coding: utf-8

# In[ ]:

from random import randint

f = 0;
step = max(0,f)

def rollDice():
    dice = randint(1,6)
    return dice;


def badLuck():
    dice = randint(1,1000)
    if dice == 1:
        return True
    else: 
        return False

for i in range(1, 500):
    for j in range(1, 100):
        dice = rollDice()
        if dice == 1 or dice == 2:
            if badLuck() == False:
                step = step - 1
            else:
                step = 0
        elif dice == 3 or dice == 4 or dice == 5:
            if badLuck() == False:
                step = step + 1
        else:
            step = 0
            if badLuck() == False:
                step = step + rollDice()
            else: 
                step = 0         

rounds.append(step)
print(step)
print(rounds)
print(rollDice())

