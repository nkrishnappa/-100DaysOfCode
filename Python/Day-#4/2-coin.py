'''
write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

'''

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

toss_it = random.randint(0,1)
if toss_it == 1 :
    print("Heads")
else:
    print("Tails")