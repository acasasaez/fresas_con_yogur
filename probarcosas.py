from colorama import *
print(Fore.LIGHTYELLOW_EX + "M de ")
print(Fore.MAGENTA+"Motomami "+ Fore.LIGHTCYAN_EX + "Motomami" )

import re


def conversiones (dat_1, dat_2): 
    conversiones =[]
    for i in dat_1:
        if i in dat_2:
            conversiones.append(1)
        else: 
            conversiones.append(0)
    return conversiones 

print(conversiones ([1,2,3,5,7], [1,6,7,2,4]))