#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from sys import argv

args = argv

try:
    domain = args[1]
    f_wordlist = args[2]
except:
    print('Domain and Wordlist are needed.')
    exit(0)

def read_file(wordlist):
    try:
        wordlist = open(f_wordlist, 'r')
        lines = wordlist.readlines()
        return lines
    except Exception as open_file:
        print('Error while opening or reading the file. Error:', open_file)
        exit(1)

def bruteforce(url):
    status_code = 404
    try:
        read_file(f_wordlist)
        url = domain.strip()
        url += '/'

        for line in lines:
            req = requests.get(url + line)
            status_code = req.status

            if status_code != 404:
                print(url + line + ' --> ' + status_code)

    except Exception as bruteforcing:
        print('Error while directorie bruteforcing. Error:', bruteforcing)
        exit(1)

def main():
    bruteforce(domain)

if __name__ == '__main__':
    main()
