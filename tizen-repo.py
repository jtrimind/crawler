#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import subprocess

toplink = 'https://git.tizen.org/cgit/'

def getRepoListFromLink(link):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')
    repos = soup.select('#cgit > div.content > table > tr > td.toplevel-repo > a')
    for repo in repos:
        reponame = repo.get('href')
        url = 'https://git.tizen.org' + reponame
        dirname = reponame[6:]
        try:
            subprocess.check_call(['git', 'clone', url, dirname])
        except:
            pass

if __name__ == "__main__":
    req = requests.get(toplink)
    soup = BeautifulSoup(req.text, 'html.parser')
    pager = soup.select('#cgit > div.content > ul > li > a')
    for page in pager:
        link = 'https://git.tizen.org' + page.get('href')
        getRepoListFromLink(link)
    else:
        getRepoListFromLink(toplink)