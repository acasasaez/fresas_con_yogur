from colorama import *
print(Fore.LIGHTYELLOW_EX + "M de ")
print(Fore.MAGENTA+"Motomami "+ Fore.LIGHTCYAN_EX + "Motomami" )

import re

movimientos = {
        'arr': 0,
        'aba': 2,
        'izq': 0,
        'der': 0
    }


def main():
        entrie = None
        while entrie != '*FIN*':
            print('Ingrese el movimiento, *FIN* para terminar\n')
            entrie = input('DIRECCION, DISTANCIA [m]: ')
            matchs = re.match(
                          pattern=r'^(arr|aba|izq|der)\s([0-9])+', 
                          string=entrie, 
                          flags=re.IGNORECASE
                     )
            if entrie != '*FIN*':
               if matchs:
                    movimientos[matchs.group(1)] += int(matchs.group(2))
               else:
                    print('Opción no valida')

        print(movimientos)