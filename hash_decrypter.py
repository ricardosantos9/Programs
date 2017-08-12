#!/usr/bin/python3
#-*- coding: utf-8 -*-

#Begin

import hashlib
from datetime import datetime
from sys import argv
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
    st = os.stat('hash_decrypter.py')
    os.chmod('hash_decrypter.py', st.st_mode | stat.S_IEXEC)

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
    print(colors.red + '#\t\t\t       Hash Decrypter v1.0\t\t               #' + colors.normal)
    print(colors.blue + '#\t\t-----------------------------------------------\t\t       #' + colors.normal)
    print(colors.yellow + '#\t\tX\t   Developer - Ricardo Santos\t      X\t\t       #' + colors.normal)
    print(colors.blue+ '#\t\t-----------------------------------------------\t\t       #' + colors.normal)
    print(colors.red + '#\t\t\t\t\t\t\t\t\t       #' + colors.normal)
    print(colors.green + '################################################################################' + colors.normal)
    
    print('\nUsage: ./hash_decrypter [hash_type] [hash_to_decrypt] [wordlist_for_bruteforce_the_hash]')
    print('Available Hash Types: [MD5, SHA256, SHA1, SHA512]\n')


args = argv

try:
    hash_type = args[1]
    hash_string = args[2]
    file_decrypt = args[3]
except:
    label()
    exit(1)


def decrypt_md5():
    try:
        wordlist = open(file_decrypt)
        words = wordlist.readlines()
    except:
        print('\nError while opening the wordlist\n')
        exit(1)
    
    words_tried = set()
    passwords_cracked = set()

    t1 = datetime.now() 
    print('Staring BruteFoce...\n')

    for word in words:
        word_strip = word.strip()
        try:
            if word_strip not in words_tried:
                word_strip_encode = word_strip.encode('utf-8')
                hash_word_strip = hashlib.md5(word_strip_encode).hexdigest()
            
                hash_string_strip = hash_string.strip()

                if str(hash_word_strip) == str(hash_string_strip):
                    print(colors.red + '[+] ' + colors.normal + colors.green + 'Hash Decrypted - ' + colors.normal + colors.yellow + str(word_strip) + colors.normal)
                    
                    t2 = datetime.now()
                    tf = t2 - t1
                    passwords_cracked.add(word_strip)
                    print('\nHash Cracked in', tf)

                words_tried.add(word_strip)
            else:
                pass
        except:
            print('\nError while BruteForcing the Hash\n')
            exit(1)

    if len(passwords_cracked) == 0:
        t2 = datetime.now()
        tf = t2 - t1
        
        print(colors.red + '[-] Couldn\'t Crack the Hash, try to use an other Wordlist.' + colors.normal + '\n')
        print('Wordlist runned in', tf)

def decrypt_sha256():
    try:
        wordlist = open(file_decrypt)
        words = wordlist.readlines()
    except:
        print('\nError while opening the wordlist\n')
        exit(1)
    
    words_tried = set()
    passwords_cracked = set()

    t1 = datetime.now()
    print('Starting BruteForce...\n')

    for word in words:
        word_strip = word.strip()
        try:
            if word_strip not in words_tried:
                word_strip_encode = word_strip.encode('utf-8')
                hash_word_strip = hashlib.sha256(word_strip_encode).hexdigest()
            
                hash_string_strip = hash_string.strip()

                if str(hash_word_strip) == str(hash_string_strip):
                    print(colors.red + '[+] ' + colors.normal + colors.green + 'Hash Decrypted - ' + colors.normal + colors.yellow + str(word_strip) + colors.normal)
                    
                    t2 = datetime.now()
                    tf = t2 - t1
                    passwords_cracked.add(word_strip)
                    print('\nHash Cracked in', tf)

                words_tried.add(word_strip)
            else:
                pass
        except:
            print('\nError while BruteForcing the Hash\n')
            exit(1)
    if len(passwords_cracked) == 0:
        t2 = datetime.now()
        tf = t2 - t1
        
        print(colors.red + '[-] Couldn\'t Crack the Hash, try to use an other Wordlist.' + colors.normal + '\n')
        print('Wordlist runned in', tf)


def decrypt_sha1():
    try:
        wordlist = open(file_decrypt)
        words = wordlist.readlines()
    except:
        print('\nError while opening the wordlist\n')
        exit(1)
    
    words_tried = set()
    passwords_cracked = set()

    t1 = datetime.now()
    print('Starting BruteForce...\n')

    for word in words:
        word_strip = word.strip()
        try:
            if word_strip not in words_tried:
                word_strip_encode = word_strip.encode('utf-8')
                hash_word_strip = hashlib.sha1(word_strip_encode).hexdigest()
            
                hash_string_strip = hash_string.strip()

                if str(hash_word_strip) == str(hash_string_strip):
                    print(colors.red + '[+] ' + colors.normal + colors.green + 'Hash Decrypted - ' + colors.normal + colors.yellow + str(word_strip) + colors.normal)
                    
                    t2 = datetime.now()
                    tf = t2 - t1
                    passwords_cracked.add(word_strip)
                    print('\nHash Cracked in', tf)

                words_tried.add(word_strip)
            else:
                pass
        except:
            print('\nError while BruteForcing the Hash\n')
            exit(1)
    if len(passwords_cracked) == 0:
        t2 = datetime.now()
        tf = t2 - t1

        print(colors.red + '[-] Couldn\'t Crack the Hash, try to use an other Wordlist.' + colors.normal + '\n')
        print('Wordlist runned in', tf)


def decrypt_sha512():
    try:
        wordlist = open(file_decrypt)
        words = wordlist.readlines()
    except:
        print('\nError while opening the wordlist\n')
        exit(1)
    
    words_tried = set()
    passwords_cracked = set()

    t1 = datetime.now()
    print('Starting BruteForce...\n')

    for word in words:
        word_strip = word.strip()
        try:
            if word_strip not in words_tried:
                word_strip_encode = word_strip.encode('utf-8')
                hash_word_strip = hashlib.sha512(word_strip_encode).hexdigest()
            
                hash_string_strip = hash_string.strip()

                if str(hash_word_strip) == str(hash_string_strip):
                    print(colors.red + '[+] ' + colors.normal + colors.green + 'Hash Decrypted - ' + colors.normal + colors.yellow + str(word_strip) + colors.normal)
                    
                    t2 = datetime.now()
                    tf = t2 - t1
                    passwords_cracked.add(word_strip)
                    print('\nHash Cracked in', tf)

                words_tried.add(word_strip)
            else:
                pass
        except:
            print('\nError while BruteForcing the Hash\n')
            exit(1)
    if len(passwords_cracked) == 0:
        t2 = datetime.now()
        tf = t2 - t1

        print(colors.red + '[-] Couldn\'t Crack the Hash, try to use an other Wordlist.' + colors.normal + '\n')
        print('Wordlist runned in', tf)


def main():
    if hash_type == 'md5' or hash_type == 'MD5':
        decrypt_md5()
    elif hash_type == 'sha256' or hash_type == 'SHA256':
        decrypt_sha256()
    elif hash_type == 'sha1'  or hash_type == 'SHA1':
        decrypt_sha1()
    elif hash_type == 'sha512' or hash_type == 'SHA512':
        decrypt_sha512()
    else:
        print('\n' + colors.red + 'Use only the Hash Type supported.' + colors.normal + '\n')
        exit(1)


if __name__ == '__main__':
    main()

#End
