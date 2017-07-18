#!/usr/bin/python
#-*- coding: utf-8 -*-
#Begin

#Importing Libraries
import math
import sys
import os

os.chmod('solid_area.py', 777)

#Creating Colors For Using In The Program
class bcolors:
    OKPURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    OKRED  = '\033[91m'
    OKCYAN = '\033[96m'
    UNDERLINE = '\033[04m'
    ENDC = '\033[0m' 

#Creating Functions to display help and label screen
def label():
    print(bcolors.OKGREEN + '\n################################################################################' + bcolors.ENDC)
    print(bcolors.OKRED + '#\t\t\t         Solid Area´s\t\t\t               #' + bcolors.ENDC)
    print(bcolors.OKBLUE + '#\t\t-----------------------------------------------\t\t       #' + bcolors.ENDC)
    print(bcolors.OKYELLOW + '#\t\tX\t   Developer - Ricardo Santos\t      X\t\t       #' + bcolors.ENDC)
    print(bcolors.OKBLUE + '#\t\t-----------------------------------------------\t\t       #' + bcolors.ENDC)
    print(bcolors.OKRED + '#\t\t\t\t\t\t\t\t\t       #' + bcolors.ENDC)
    print(bcolors.OKGREEN + '################################################################################' + bcolors.ENDC)
    
    print(bcolors.OKCYAN + '\nUse "./solid_area.py [solid] [solid_options] [...]" to use the program.')
    print('Use "./solid_area.py [-h/--help/help]" to learn how program work´s.\n' + bcolors.ENDC)

def help():
    print('\n'+ bcolors.OKYELLOW + 'U' + bcolors.ENDC
              + bcolors.OKRED + 'S' + bcolors.ENDC 
              + bcolors.OKGREEN + 'A' + bcolors.ENDC 
              + bcolors.OKCYAN + 'G' + bcolors.ENDC 
              + bcolors.OKPURPLE + 'E' + bcolors.ENDC 
              + bcolors.OKBLUE + ':' + bcolors.ENDC)

    print(bcolors.OKYELLOW + '\nSquare: ./solid_area.py [sqr/square] [side_one] [side_two]' + bcolors.ENDC)
    print(bcolors.OKPURPLE + '---------------------------------------------------------------------------' + bcolors.ENDC)
    print(bcolors.OKRED + '\nTriangle: ./solid_area.py [trg/triangle] [base] [height]' + bcolors.ENDC)
    print(bcolors.OKPURPLE + '---------------------------------------------------------------------------' + bcolors.ENDC)    
    print(bcolors.OKGREEN + '\nCircle: ./solyd_area.py [crc/circle] [radius]' + bcolors.ENDC)
    print(bcolors.OKPURPLE + '---------------------------------------------------------------------------' + bcolors.ENDC)
    print(bcolors.OKCYAN + '\nTrapezoid: ./solid_area.py [trp/trapezoid] [side_one] [side_two] [heigth]' + bcolors.ENDC)
    print(bcolors.OKPURPLE + '---------------------------------------------------------------------------\n' + bcolors.ENDC)

#Creating Functions To Calculate the area´s
def area_sqr(s1, s2):
    #Calculating the area of a square
    a_sqr = float(s1) * float(s2)
    print(bcolors.OKYELLOW + '\nThe area of the square is {:.1f}cm².\n'.format(a_sqr) + bcolors.ENDC)

def area_trg(b, h):
    #Calculating the area of the triangle
    a_trg = float(((float(b) * float(h)) / float(2)))
    print(bcolors.OKYELLOW + '\nThe area of the triangle is {:.1f}cm².\n'.format(a_trg) + bcolors.ENDC)

def area_crc(r):
    #Calculating the area of the circle
    a_crc_square = float(math.pow(float(r), 2))
    a_crc_c = float(math.pi * math.pow(float(r), 2))
    print(bcolors.OKYELLOW + '\nThe area of the circle is {:.2f}π ≈ {:.2f}cm².\n'.format(a_crc_square ,a_crc_c) + bcolors.ENDC)

def area_trp(s1, s2, h):
    #Calculating the area of the trapezoid
    a_trp = float(((float(s1) + float(s2)) * float((h))) / float(2))
    print(bcolors.OKYELLOW + '\nThe area of the circle is {:.2f}cm².\n'.format(a_trp) + bcolors.ENDC)

#Creating Arguments
args = sys.argv

try:
    solid = args[1]
except Exception:
    label()
    sys.exit(1)

#Reading User Arguments
if solid == 'sqr' or solid == 'square':
    area_sqr(args[2], args[3])
elif solid == 'trg' or solid == 'triangle':
    area_trg(args[2], args[3])
elif solid == 'crc' or solid == 'circle':
    area_crc(args[2])
elif solid == 'trp' or solid == 'trapezoid':
    area_trp(args[2], args[3], args[4])
elif solid == '-h' or solid == '--help' or solid == 'help':
    help()
else:
    label()
    sys.exit(1)
#End
