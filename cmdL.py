import os
import math
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)
bob = ''
bob1 = ''
comand = "cmdL>>comand>>:"
while(1==1):
    print(Fore.RED + comand,end=" ")
    comm = input()
    if(comm == 'HELP'):
        print(Back.YELLOW + Fore.BLACK +'\Commands cmdL\n')
        print(Back.YELLOW +Fore.BLACK +"HELP - all comands in cmdL")
        print(Back.YELLOW +Fore.BLACK +"GO <the path to the file> - open file")
        print(Back.YELLOW +Fore.BLACK +"TREE - view device tree")
        print(Back.YELLOW +Fore.BLACK +"RENL <new value> - rename cmdL")
        print(Back.YELLOW +Fore.BLACK +'RENCMD <new value> - changes cmd')
        print(Back.YELLOW +Fore.BLACK +'RENF <new value> <the path to the file> - rename file')
        print(Back.YELLOW +Fore.BLACK +'NOTE - quick notepad opening')
        print(Back.YELLOW +Fore.BLACK +'SAVE <name> <new value> - save something')
        print(Back.YELLOW +Fore.BLACK +"OUTS <name> - issue a save")
        print(Back.YELLOW +Fore.BLACK +'CLEAR - clear cmdL')
        print(Back.YELLOW +Fore.BLACK +'COL <new value> <new value> - change color cmdL')
        print(Back.YELLOW +Fore.BLACK +'WATCH <the path to the file> - view content txt file')
        print(Back.YELLOW +Fore.BLACK +'DEL <the path to the file> - delete файл')
        print(Back.YELLOW +Fore.BLACK +'EXIT <Y/N> - exit from the program')
    elif(comm == 'HELPMATH'):
        print(Back.YELLOW +Fore.BLACK +'M+ <1 value> <2 value> - add 2 numbers')
        print(Back.YELLOW +Fore.BLACK +'M++ <1 value> <examination> - add numbers')
        print(Back.YELLOW +Fore.BLACK +'M- <1 value> <2 value> - subtract 2 numbers')
        print(Back.YELLOW +Fore.BLACK +'M-- <1 value> <examination> - subtract numbers')
        print(Back.YELLOW +Fore.BLACK +'M* <1 value> <2 value> - multiply 2 numbers')
        print(Back.YELLOW +Fore.BLACK +'M** <1 value> <examination> - multiply numbers')
        print(Back.YELLOW +Fore.BLACK +'PI <circle radius> - find the area of ​​a circle')
        print(Back.YELLOW +Fore.BLACK +'ST <triangle height> <side to which the height is built> - area of ​​a triangle')
        print(Back.YELLOW +Fore.BLACK +'M! <1 value> - factorial')
        print(Back.YELLOW +Fore.BLACK +'MNOD <1 value> <2 value> - greatest common divisor')
        print(Back.YELLOW +Fore.BLACK +'MISQRT <1 value> - integer square root of the argument, rounded down')
        print(Back.YELLOW +Fore.BLACK +'MSQRT <1 value> - square root')
        print(Back.YELLOW +Fore.BLACK +'MPERM <1 value> <2 value> - to find all the ways')
        print(Back.YELLOW +Fore.BLACK +'M^ <1 value> <2 value> - exponentiation 1 -> 2')
        print(Back.YELLOW +Fore.BLACK +'CC2 <1 value> - conversion to number system 2')
    elif(comm == 'GO'):
        GO = input()
        os.system('START'+" "+GO)
    elif(comm == 'TREE'):
       os.system('TREE')
    elif(comm == "RENL"):
        GO = input()
        os.system('TITLE'+" "+ GO)
    elif(comm == 'NOTE'):
        os.system('START notepad.exe')
    elif(comm == 'SAVE'):
        bob = input()
        bob1 = input()
    elif(comm == 'OUTS'):
        GO = input()
        if(GO == bob):
            print(bob1)
    elif(comm == 'CLEAR'):
        os.system('cls')
    elif(comm == 'COL'):
        GO = input()
        GO1 = input()
        os.system('COLOR'+" "+GO+GO1)
    elif(comm == 'WATCH'):
        GO = input()
        os.system('TYPE'+" "+GO)
        print('')
    elif(comm == 'DEL'):
        GO = input()
        os.system('DEL'+' '+GO)
    elif(comm == 'EXIT'):
        print('Exit?Y/N:',end=' ')
        GO = input()
        if(GO == "Y"):
            break;  
        elif(GO == "N"):
            print('ok')
    elif(comm == 'RENCMD'):
        GO = input()
        comand = GO
    elif(comm == 'RENF'):
        GO = input()
        GO1 = input()
        os.system('REN'+" "+GO1+" "+GO)
    elif(comm == 'M+'):
        GO = float(input())
        GO1 = float(input())
        print(Back.GREEN + "M+:", str(GO + GO1))
    elif(comm == 'M++'):
        otv = 0
        GO = 0
        stp = ''
        while(stp != 'STOP'):
            print('Введите число:',end='')
            GO = float(input())
            print('STOP?')
            stp = input()
            otv += GO
        print(Back.GREEN + 'M++:',str(otv))
    elif(comm == 'M-'):
        GO = float(input())
        GO1 = float(input())
        print(Back.GREEN + "M-:", str(GO - GO1))
    elif(comm == 'M--'):
        print('введите 1 число:')
        otv = int(input())
        GO = 0
        stp = ''
        while(stp != 'STOP'):
            print('Введите число:',end='')
            GO = float(input())
            print('STOP?')
            stp = input()
            otv -= GO
        print(Back.GREEN + 'M--:',str(otv))
    elif(comm == 'M*'):
        GO = float(input())
        GO1 = float(input())
        print(Back.GREEN + "M*:", str(GO * GO1))
    elif(comm == 'M**'):
        otv = 1
        GO = 0
        stp = ''
        while(stp != 'STOP'):
            print('Введите число:',end='')
            GO = float(input())
            print('STOP?')
            stp = input()
            otv *= GO
        print(Back.GREEN + 'M**:',str(otv))
    elif(comm == 'PI'):
        GO = int(input())
        print(Back.GREEN + str(math.pi * (GO * GO)))
    elif(comm == "M!"):
        GO = int(input())
        print(Back.GREEN + str(math.factorial(GO)))
    elif(comm == 'MNOD'):
        GO = int(input())
        GO1 = int(input())
        print(Back.GREEN+str(math.gcd(GO, GO1)))
    elif(comm == 'MISQRT'):
        GO = int(input())
        print(Back.GREEN + str(math.isqrt(GO)))
    elif(comm == 'MPERM'):
        GO = int(input())
        GO1 = int(input())
        print(Back.GREEN + str(math.perm(GO, GO1)))
    elif(comm == 'MSQRT'):
        GO = float(input())
        print(Back.GREEN + str(math.sqrt(GO)))
    elif(comm == 'M^'):
        GO = int(input())
        GO1 = int(input())
        print(Back.GREEN + str(math.pow(GO, GO1)))
    elif(comm == 'ST'):
        GO = float(input())
        GO1 = float(input())
        print(Back.GREEN + str(1/2 * GO * GO1))
    elif(comm == "CC2"):
        GO = int(input())
        p = 1
        p1 = 1
        otv = ''
        while(p*2 <= GO):
            p *= 2
        while(p):
            d = GO//p
            otv += str(d)
            GO %= p
            p = p // 2
        print(Back.GREEN + otv)
