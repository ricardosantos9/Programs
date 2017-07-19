#!/usr/bin/python
#-*- coding: utf-8 -*-

#Begin

import requests
import re
import sys

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    cyan = '\033[96m'
    blue = '\033[94m'
    purple = '\033[95m'
    normal = '\033[0m'

args = sys.argv

def label():
    print(colors.green + '\n################################################################################' + colors.normal)
    print(colors.red + '#\t\t\t           Web Finder\t\t\t               #' + colors.normal)
    print(colors.blue + '#\t\t-----------------------------------------------\t\t       #' + colors.normal)
    print(colors.yellow + '#\t\tX\t   Developer - Ricardo Santos\t      X\t\t       #' + colors.normal)
    print(colors.blue+ '#\t\t-----------------------------------------------\t\t       #' + colors.normal)
    print(colors.red + '#\t\t\t\t\t\t\t\t\t       #' + colors.normal)
    print(colors.green + '################################################################################' + colors.normal)

    print(colors.cyan + '\nUse "./web_finder.py [parameter] [http/s://url]" to crawl emails/links')
    print('Use "./web_finder.py [-h/--help]" to learn how program work´s.\n' + colors.normal)

def help():
    print('\n' + colors.yellow + 'U' + colors.normal
          + colors.red + 'S' + colors.normal
          + colors.green + 'A' + colors.normal
          + colors.cyan + 'G' + colors.normal
          + colors.purple + 'E' + colors.normal
          + colors.blue + ':' + colors.normal + ' ./web_finder.py -u https://www.google.com')

    print('-u/--url ' + colors.cyan + 'To enter an URL.'
          '-h/--help ' + colors.cyan + 'To see help.')

try:
    url_args = args[1]
except:
    print('')
    label()
    exit()

def email_find(url):
    for i in range(1):
        emails_found = set()
        req = requests.get(url)
        html = req.text

        emails = re.findall(r'[\w\._-]+@+[\w_-]+\.[\w\._-]+\w', html)

        for email in emails:
            if email not in emails_found:
                emails_found.add(email)
            else:
                pass
    print('')
    for email_found in emails_found:
        print(colors.red + '[+] ' + colors.normal + colors.green + 'Email Founded: ' + colors.normal + colors.yellow + str(email_found) + colors.normal)

    print('')

def links_find():
    to_crawl = [args[2]]
    crawled = set()

    link_crawl = input(colors.cyan + '\nDo you want to crawl links on this page? [y/n]: ' + colors.normal)
    print('')

    if link_crawl == 'y' or link_crawl == 'Y' or link_crawl == 'yes' or link_crawl == 'YES':
        try:
            while True:
                url_crawl = to_crawl[0]
                try:
                    req_links = requests.get(url_crawl)
                except Exception:
                    to_crawl.remove(url_crawl)
                    crawled.add(url_crawl)
                    continue
                except KeyboardInterrupt:
                    print('\nKeyboard Interreputed (CTRL+C) Exiting...')
                    quit()

                html_link = req_links.text
                links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html_link)
                print(colors.red + '[+] ' + colors.normal + colors.green + 'Crawling: ' + colors.normal + colors.yellow + str(url_crawl) + colors.normal)

                to_crawl.remove(url_crawl)
                crawled.add(url_crawl)

                for link in links:
                    if link not in crawled and link not in to_crawl:
                        to_crawl.append(link)
        except KeyboardInterrupt:
            print('\nKeyboard Interrupted (CTRL+C) Exiting...')
            quit()
    elif link_crawl == 'n' or link_crawl == 'N' or link_crawl == 'no' or link_crawl == 'NO':
        exit()
    else:
        exit()

def main():
    try:
        if url_args == '-u' or url_args == '--url':
            email_find(args[2])
            links_find()

        elif url_args == '-h' or url_args == '--help':
            help()
        elif url_args:
            print('')
            label()
            exit()
        else:
            print('')
            print(colors.red + 'URL needed to email crawl/link crawl. -u/--url + [domain].' + colors.normal)
            exit()
    except Exception:
        quit()
    except KeyboardInterrupt:
        print('\nKeyboard Interrupted (CTRL+C) Exiting...')
        quit()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        quit()
    except KeyboardInterrupt:
        print('\nKeyboard Interrupted (CTRL+C) Exiting...')
        quit()

#End