# using slice method to print the first three names in the list after 1.5 seconds
import time

names = ['louis', 'jana','serena','leah','alex','miguel','ruby','bella','gordon','jonah','mary','charlotte','rose','andre','tori']

for name in names[:3]:
    wait = time.sleep(1.5)
    print(name)