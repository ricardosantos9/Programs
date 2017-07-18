import requests
import re
import sys
import random

class colors:
    yellow = '\033[93m'
    red = '\033[91m'
    green = '\033[91m'
    cyan = '\033[96m'
    normal = '\033[0m'

args = sys.argv

try:
    url_args = args[1]
except:
    print('URL needed, -u/--url')
    exit()

def email_find(url):
    reqs_nmb = random.randint(1, 10)
    for i in range(reqs_nmb):
        emails_found = set()
        req = requests.get(url)
        html = req.text

        emails = re.findall(r'[\w\._-]+@+[\w_-]+\.[\w\._-]+\w', html)

        for email in emails:
            if email not in emails_found:
                emails_found.add(email)
            else:
                pass

    for email_found in emails_found:
        print(colors.green + '\n[+]' + colors.normal + colors.yellow + 'Email Founded:' + str(email_found) + colors.normal)

def main():
    if url_args == '-h' or url_args == '--url':
        email_find(args[2])
    else:
        print('Url needed to email crawl. -u/--url')
        exit()

if __name__ == '__main__':
    main()