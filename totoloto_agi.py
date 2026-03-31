#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup

def get_last_totoloto_key():
    url = 'https://www.jogossantacasa.pt/web/SCCartazResult/totolotoNew'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    bet_div = soup.find('div', class_='betMiddle twocol regPad')
    if not bet_div:
        sys.stderr.write('Error: Could not find the bet results div.\n')
        sys.exit(1)

    numbers_list = bet_div.find('ul', class_='colums')
    if numbers_list:
        try:
            last_key = numbers_list.find_all('li')[0].get_text()
            return last_key.strip()
        except IndexError:
            sys.stderr.write('Error: Could not find any numbers in the list.\n')
            sys.exit(1)
    else:
        sys.stderr.write('Error: Could not find the numbers list.\n')
        sys.exit(1)

if __name__ == '__main__':
    try:
        TOTOTOLO_KEY = get_last_totoloto_key()
        print(f'SET VARIABLE last_key "{TOTOTOLO_KEY}"')
    except Exception as e:
        sys.stderr.write(str(e) + '\n')
        sys.exit(1)

