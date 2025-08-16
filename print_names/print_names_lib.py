# use a loop and random library to print 3 names after 2 seconds
# using random library
import random


import time 

# generating names in the list
names = ['louis', 'jana','serena','leah','alex','miguel','ruby','bella','gordon','jonah','mary','charlotte','rose','andre','tori']

for name in random.choices(names, k=3):
    wait = time.sleep(2)
    print(name)
