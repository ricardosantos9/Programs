#!usr/bin/python
import hashlib
import sys

# Creating arguments
args = sys.argv

def label_func():
    print('')
    print('################################################################################')
    print('#\t\t\t\tHashCrypter v.1.0\t\t\t       #')
    print('#\t\t-----------------------------------------------\t\t       #')
    print('#\t\tX\t   Developer - Ricardo Santos\t      X\t\t       #')
    print('#\t\t-----------------------------------------------\t\t       #')
    print('#\t\t\t\t\t\t\t\t\t       #')
    print('################################################################################')

    print('\nUse "python hashcrypter.py [hash type] [string]" to hash a string.\nUse "python hashcrypter.py -h/--help" to learn how script works.\nUse "python hashcrypter.py --hash" to see hash algoritms that can be use.\n')

try:
    hash_type = args[1]
except Exception:
    label_func()

    sys.exit(1)

# Hash Algoritms functions
def md5_hash():
    string = args[2]
    string_bytes = string.encode('utf-8')

    md5_data = hashlib.md5(string_bytes).hexdigest()
    print('\n[+] Hash: ' + str(md5_data) + '\n')

def sha256_hash():
    string = args[2]
    string_bytes = string.encode('utf-8')

    sha256_data = hashlib.sha256(string_bytes).hexdigest()
    print('\n[+] Hash: ' + str(sha256_data) + '\n')

def sha1_hash():
    string = args[2]
    string_bytes = string.encode('utf-8')

    sha1_data = hashlib.sha1(string_bytes).hexdigest()
    print('\n[+] Hash: ' + str(sha1_data) + '\n')

def sha224_hash():
    string = args[2]
    string_bytes = string.encode('utf-8')

    sha224_data = hashlib.sha224(string_bytes).hexdigest()
    print('\n[+] Hash: ' + str(sha224_data + '\n'))

def sha512_hash():
    string = args[2]
    string_bytes = string.encode('utf-8')

    sha512_data = hashlib.sha512(string_bytes).hexdigest()
    print('\n[+] Hash: ' + str(sha512_data + '\n'))

def sha384_hash():
    string = args[2]
    string_bytes = string.encode('utf-8')

    sha384_data = hashlib.sha384(string_bytes).hexdigest()
    print('\n[+] Hash: ' + str(sha384_data + '\n'))

def help():
    print('\npython hashcrypter.py [hash type] [string to hash]\n')

def hash_table():
    print('\nHash that can be used:')
    hash_list = ['- MD5', '- SHA256', '- SHA1', '- SHA224', '- SHA512', '- SHA384']

    for hash in hash_list:
        print(hash)

    print('')
    sys.exit(1)

# Reading Arguments and Hashing Strings
try:
    if hash_type == 'md5' or hash_type == 'MD5':
        md5_hash()
    elif hash_type == 'sha256' or hash_type == 'SHA256':
        sha256_hash()
    elif hash_type == 'sha1' or hash_type == 'SHA1':
        sha1_hash()
    elif hash_type == 'sha224' or hash_type == 'SHA224':
        sha224_hash()
    elif hash_type == 'sha512' or hash_type == 'SHA512':
        sha512_hash()
    elif hash_type == 'sha384' or hash_type == 'SHA384':
        sha384_hash()
    elif (hash_type == '-h' or hash_type == '--help'):
        help()
    elif (hash_type == '--hash' or hash_type == '--HASH'):
        hash_table()
    elif args[0]:
        label_func()
    elif args[1]:
        help()
    else:
        hash_table()
except Exception:
    print('Error while hashing the string (No String passed).' )
    sys.exit(1)