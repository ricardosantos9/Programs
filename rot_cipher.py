#!/usr/bin/python3
#-*- coding: utf-8 -*-

from sys import argv
from string import maketrans
from sys import platform

if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
    class colors:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        cyan = '\033[96m'
        blue = '\033[94m'
        purple = '\033[95m'
        normal = '\033[0m'
    
    import os, stat
    st = os.stat('rot_cipher.py')
    os.chmod('rot_cipher.py', st.st_mode | stat.S_IEXEC)

elif platform == 'win32':
    from termcolor import colored
    class colors:
        red = colored('red')
        green = colored('green')
        yellow = colored('yellow')
        cyan = colored('cyan')
        blue = colored('blue')
        purple = colored('purple')
        normal = colored('white')
else:
    class colors:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        cyan = '\033[96m'
        blue = '\033[94m'
        purple = '\033[95m'
        normal = '\033[0m'


def label():
    print(colors.green + '\n################################################################################' + colors.normal)
    print(colors.red + '#\t\t\t        ROT CIPHER v1.0\t\t                 #' + colors.normal)
    print(colors.blue + '#\t\t-----------------------------------------------\t\t       #' + colors.normal)
    print(colors.yellow + '#\t\tX\t   Developer - Ricardo Santos\t      X\t\t       #' + colors.normal)
    print(colors.blue+ '#\t\t-----------------------------------------------\t\t       #' + colors.normal)
    print(colors.red + '#\t\t\t\t\t\t\t\t\t       #' + colors.normal)
    print(colors.green + '################################################################################' + colors.normal)
    print('\nUsage: python rot_cipher.py [ROT_TYPE] [String_To_ROT]')
    print('Available ROT Algorithms: [[ROT1] - [ROT25]]\n')

args = argv

try:
    rot_type = args[1]
    string = args[2]
except:
    label()
    exit(1)

def rot1():
    try:
        rot1trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza')
        return string.translate(rot1trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot2():
    try:
        rot2trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab')
        return string.translate(rot2trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot3():
    try:
        rot3trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc')
        return string.translate(rot3trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot4():
    try:
        rot4trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','EFGHIJKLMNOPQRSTUVWXYZABCDefghijklmnopqrstuvwxyzabcd')
        return string.translate(rot4trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot5():
    try:
        rot5trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','FGHIJKLMNOPQRSTUVWXYZABCDEfghijklmnopqrstuvwxyzabcde')
        return string.translate(rot5trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot6():
    try:
        rot6trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','GHIJKLMNOPQRSTUVWXYZABCDEFghijklmnopqrstuvwxyzabcdef')
        return string.translate(rot6trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot7():
    try:
        rot7trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','HIJKLMNOPQRSTUVWXYZABCDEFGhijklmnopqrstuvwxyzabcdefg')
        return string.translate(rot7trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot8():
    try:
        rot8trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','IJKLMNOPQRSTUVWXYZABCDEFGHijklmnopqrstuvwxyzabcdefgh')
        return string.translate(rot8trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot9():
    try:
        rot9trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','JKLMNOPQRSTUVWXYZABCDEFGHIjklmnopqrstuvwxyzabcdefghi')
        return string.translate(rot9trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot10():
    try:
        rot10trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','KLMNOPQRSTUVWXYZABCDEFGHIJklmnopqrstuvwxyzabcdefghij')
        return string.translate(rot10trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot11():
    try:
        rot11trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','LMNOPQRSTUVWXYZABCDEFGHIJKlmnopqrstuvwxyzabcdefghijk')
        return string.translate(rot11trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)
    
def rot12():
    try:
        rot12trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','MNOPQRSTUVWXYZABCDEFGHIJKLmnopqrstuvwxyzabcdefghijkl')
        return string.translate(rot12trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot13():
    try:
        rot13trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
        return string.translate(rot13trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot14():
    try:
        rot14trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','OPQRSTUVWXYZABCDEFGHIJKLMNopqrstuvwxyzabcdefghijklmn')
        return string.translate(rot14trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot15():
    try:
        rot15trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','PQRSTUVWXYZABCDEFGHIJKLMNOpqrstuvwxyzabcdefghijklmno')
        return string.translate(rot15trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot16():
    try:
        rot16trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','QRSTUVWXYZABCDEFGHIJKLMNOPqrstuvwxyzabcdefghijklmnop')
        return string.translate(rot16trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot17():
    try:
        rot17trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','RSTUVWXYZABCDEFGHIJKLMNOPQrstuvwxyzabcdefghijklmnopq')
        return string.translate(rot17trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot18():
    try:
        rot18trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','STUVWXYZABCDEFGHIJKLMNOPQRstuvwxyzabcdefghijklmnopqr')
        return string.translate(rot18trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot19():
    try:
        rot19trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','TUVWXYZABCDEFGHIJKLMNOPQRStuvwxyzabcdefghijklmnopqrs')
        return string.translate(rot19trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot20():
    try:
        rot20trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','UVWXYZABCDEFGHIJKLMNOPQRSTuvwxyzabcdefghijklmnopqrst')
        return string.translate(rot20trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot21():
    try:
        rot21trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','VWXYZABCDEFGHIJKLMNOPQRSTUvwxyzabcdefghijklmnopqrstu')
        return string.translate(rot21trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot22():
    try:
        rot22trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','WXYZABCDEFGHIJKLMNOPQRSTUVwxyzabcdefghijklmnopqrstuv')
        return string.translate(rot22trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot23():
    try:
        rot23trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw')
        return string.translate(rot23trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot24():
    try:
        rot24trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','YZABCDEFGHIJKLMNOPQRSTUVWXyzabcdefghijklmnopqrstuvwx')
        return string.translate(rot24trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def rot25():
    try:
        rot25trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy')
        return string.translate(rot25trans)
    except:
        print('\n' + colors.red + '[-] Error while Rotating the String' + colors.normal + '\n')
        exit(1)

def main():
    if rot_type == 'rot1' or rot_type == 'ROT1':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot1 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot1() + colors.normal + '\n'
    elif rot_type == 'rot2' or rot_type == 'ROT2':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot2 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot2() + colors.normal + '\n'
    elif rot_type == 'rot3' or rot_type == 'ROT3':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot3 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot3() + colors.normal + '\n'
    elif rot_type == 'rot4' or rot_type == 'ROT4':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot4 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot4() + colors.normal + '\n'
    elif rot_type == 'rot5' or rot_type == 'ROT5':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot5 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot5() + colors.normal + '\n'
    elif rot_type == 'rot6' or rot_type == 'ROT6':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot6 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot6() + colors.normal + '\n'
    elif rot_type == 'rot7' or rot_type == 'ROT7':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot7 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot7() + colors.normal + '\n'
    elif rot_type == 'rot8' or rot_type == 'ROT8':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot8 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot8() + colors.normal + '\n'
    elif rot_type == 'rot9' or rot_type == 'ROT9':
        print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot9 String ' + colors.normal + colors.cyan + '- ' + colors.       normal + colors.yellow + rot9() + colors.normal + '\n'
    elif rot_type == 'rot10' or rot_type == 'ROT10':
        print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot10 String ' + colors.normal + colors.cyan + '- ' + colors.      normal + colors.yellow + rot10() + colors.normal + '\n'
    elif rot_type == 'rot11' or rot_type == 'ROT12':
        print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot11 String ' + colors.normal + colors.cyan + '- ' + colors. normal + colors.yellow + rot11() + colors.normal + '\n'
    elif rot_type == 'rot12' or rot_type == 'ROT12':
        print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot12 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot12() + colors.normal + '\n'
    elif rot_type == 'rot13' or rot_type == 'ROT13':
        print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot13 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot13() + colors.normal + '\n'
    elif rot_type == 'rot14' or rot_type == 'ROT14':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot14 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot14() + colors.normal + '\n'
    elif rot_type == 'rot15' or rot_type == 'ROT15':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot15 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot15() + colors.normal + '\n'
    elif rot_type == 'rot16' or rot_type == 'ROT16':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot16 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot16() + colors.normal + '\n'
    elif rot_type == 'rot17' or rot_type == 'ROT17':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot17 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot17() + colors.normal + '\n'
    elif rot_type == 'rot18' or rot_type == 'ROT18':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot18 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot18() + colors.normal + '\n'
    elif rot_type == 'rot19' or rot_type == 'ROT19':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot19 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot19() + colors.normal + '\n'
    elif rot_type == 'rot20' or rot_type == 'ROT20':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot20 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot20() + colors.normal + '\n'
    elif rot_type == 'rot21' or rot_type == 'ROT21':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot21 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot21() + colors.normal + '\n'
    elif rot_type == 'rot22' or rot_type == 'ROT22':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot22 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot22() + colors.normal + '\n'
    elif rot_type == 'rot23' or rot_type == 'ROT23':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot23 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot23() + colors.normal + '\n'
    elif rot_type == 'rot24' or rot_type == 'ROT24':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot24 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot24() + colors.normal + '\n'
    elif rot_type == 'rot25' or rot_type == 'ROT25':
	print '\n' + colors.red + '[+] ' + colors.normal + colors.green + 'Rot25 String ' + colors.normal + colors.cyan + '- ' + colors.normal + colors.yellow + rot25() + colors.normal + '\n'
    else:
        label()

if __name__ == "__main__":
    main()
