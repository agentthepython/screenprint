#======================================
# Shuffle text
# RE-Written by Jan on 09/06/2022 16:53
#======================================

import random
import os

cont = True
os.system('clear')

while cont:
    list_raw = input("Enter your sentence or Q to quit) ") # raw_input() function
    
    if list_raw.upper() != 'Q':

        words = list_raw.split()
        random.shuffle(words)
        final_sentence = ' '.join(words)

        print(final_sentence)
    else:
        cont =False
        print("Goodbye")
