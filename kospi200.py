#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

if __name__ == "__main__":
    codes = []
    for i in range(1, 21):
        url = 'https://finance.naver.com/sise/entryJongmok.nhn?&page=' + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup.find_all("td", class_="ctg")
        for tag in tags:
            code_str = tag.a.get('href')
            code = code_str[code_str.rfind('=') + 1:]
            codes.append(code)

    with open('kospi200.txt', 'w') as f:
        for code in codes:
            f.write(code + '\n')
