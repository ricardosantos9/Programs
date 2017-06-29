#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys

args = sys.argv

def label():
    print('')
    print('################################################################################')
    print('#\t\t\t       Pythagoras Theoreme\t\t\t       #')
    print('#\t\t-----------------------------------------------\t\t       #')
    print('#\t\tX\t   Developer - Ricardo Santos\t      X\t\t       #')
    print('#\t\t-----------------------------------------------\t\t       #')
    print('#\t\t\t\t\t\t\t\t\t       #')
    print('################################################################################')

    print('\nUse "python pi_theoreme.py [h or hypotenuse][cathet] [cathet]" to calculate the hypotenuse value of a triangle(Only retangle).')
    print('Use "python pi_theoreme.py [c or cathet][hypotenuse] [cathet]" to calculate the cathet value of a triangle(Only retangle).')

try:
    h_c = args[1]
except Exception:
    label()
    sys.exit(1)

def help_pi():
    print('\nUsage:\n')
    print('Use "python pi_theoreme.py [h or hypotenuse][cathet] [cathet]" to calculate the hypotenuse value of a triangle(Only retangle).')
    print('Use "python pi_theoreme.py [c or cathet][hypotenuse] [cathet]" to calculate the cathet value of a triangle(Only retangle).')
    
def hypotenuse_pi():
    try:
        c1 = args[2]
        c2 = args[3]
    except Exception:
        print('\nThere are missing cathets of the triangle to calculate the Hypotenuse.')
        sys.exit(1)

    try:
        # (h2 ** 2) = ((c1 ** 2) + (c2 ** 2))
        h_sqr = (math.pow(float(c1), 2) + math.pow(float(c2), 2))
        
        # h = (square_root(h_sqr)
        h = math.sqrt(float(h_sqr))
        
        print('\nThe Hypotenuse of the triangle is ' + '√' + str(float(h_sqr)) + ' (=) ' + str(h))
        #
    except Exception:
        print('\nError while calculating the hypotenuse of triangle')
        sys.exit(1)

def cathet_pi():
    try:
        h2 = args[2]
        c3 = args[3]
    except Exception:
        print('\nThere are missing Hypotenuse/Cathet of the triangule to calculate the Cathet')
        sys.exit(1)

    try:
        # c_x = (h ** 2) - (c_y ** 2)
        c_x = (math.pow(float(h2), 2) - math.pow(float(c3), 2))
        # c_c = (square_root(c_x))
        c_cathet = math.sqrt(float(c_x))

        print('\nThe Cathet of the triangule is √' + str(float(c_x)) + ' (=) ' + str(c_cathet))
                        
    except Exception:
        print('\nError while calculating the cathet of triangle')
        sys.exit(1)
             
def hipotenuse_cateto():
    if args[1] == 'h' or args[1] == 'hypotenuse':
        hypotenuse_pi()
    elif args[1] == 'c' or args[1] == 'cathet':
        cathet_pi()
    elif args[1] == '-h' or args[1] == '--help' or args[1] == 'help':
        help_pi()
    else:
        print('\nIts only possible to calculate the hypotenuse or the cathets of a triangule. Use -h or --help to learn how program works.')
        sys.exit()
def main():
    hipotenuse_cateto()
    
if __name__ == '__main__':
    main()
