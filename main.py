#!/usr/bin/env python
import matplotlibMethods, vpythonMethods

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
            vpythonMethods.cubo()
            exit()
        elif answer == 1:
            vpythonMethods.esfera()
            exit()
        elif answer == 2:
            vpythonMethods.flecha()
            exit()
        elif answer == 3:
            vpythonMethods.cono()
            exit()
        elif answer == 4:
            vpythonMethods.cilindro()
            exit()
        elif answer == 5:
            vpythonMethods.piramide()
            exit()
    elif answerOne == 2:
        printOptions(matplotlib)
        answer = int(input('¿Que desea mostrar? -> '))
        if answer == 0:
            matplotlibMethods.cubo()
            exit()
        elif answer == 1:
            matplotlibMethods.esfera()
            exit()
        elif answer == 2:
            matplotlibMethods.flecha()
            exit()
        elif answer == 3:
            matplotlibMethods.flecha3D()
            exit()
        elif answer == 4:
            matplotlibMethods.cono()
            exit()


if __name__ == '__main__':
    while True:
        try:
            mainProcess()
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()
