
# coding: utf-8

# In[12]:

from random import randint
import numpy as np

f = 0

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

rounds = []
round = []

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
        round.append(step)
    rounds.append(round)

np_round = np.array(round)
np_rounds = np.array(rounds)

print(np_rounds)

# In[ ]:




# In[ ]:
