#!/usr/bin/env python
import metodos, metdosdos

matplotlib  = ["Cubo","Esfera","Flecha simple", "Flecha 3D", "Cono"]
vpython = ["Cubo", "Esfera", "Flecha", "Cono", "Cilindro", "Piramide"]
good = '\033[92m[+]\033[0m'

def printOptions(options):
    for index, option in enumerate(options):
        good = f'\033[92m{index}\033[0m'
        square = f'\033[91m[{good}]\033[0m'
        print (f'%s {option}' % square)
    print ('\n')

def mainProcess():
    print ('\n')
    answerOne = int(input('Vpython o Matplotlib? (1/2) -> '))
    print ('\n')
    if answerOne == 1:
        printOptions(vpython)
        answer = int(input('¿Que desea mostrar? -> '))
        if answer == 0:
            metdosdos.cubo()
            exit()
        elif answer == 1:
            metdosdos.esfera()
            exit()
        elif answer == 2:
            metdosdos.flecha()
            exit()
        elif answer == 3:
            metdosdos.cono()
            exit()
        elif answer == 4:
            metdosdos.cilindo()
            exit()
        elif answer == 5:
            metdosdos.piramide()
            exit()
    else:
        printOptions(matplotlib)
        answer = int(input('¿Que desea mostrar? -> '))
        if answer == 0:
            metdosdos.cubo()
            exit()
        elif answer == 1:
            metodos.esfera()
            exit()
        elif answer == 2:
            metodos.flecha()
            exit()
        elif answer == 3:
            metodos.flecha3D()
            exit()
        elif answer == 4:
            metodos.cono()
            exit()


if __name__ == '__main__':
    while True:
        try:
            mainProcess()
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()
