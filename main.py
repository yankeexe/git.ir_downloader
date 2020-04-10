import re
import os
import requests
from bs4 import BeautifulSoup

from constants import PACKAGE_MANAGERS


def identify_system():
    """
    Identify the package manager for the system.
    """
    for name in PACKAGE_MANAGERS:
        console_out = os.popen(f'which {name}').read()

        if '/usr/bin' in console_out:
            return name


def parse_url(url):
    """
    Prase url and extract links
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    split_url = url.split("/")[-2:]
    folder_title = split_url[0]

    with open('.links.txt', 'r+') as f:
        if len(f.read()):
            f.truncate(0)

    for link in soup.findAll('a', attrs={'href': re.compile("^https://cdn9.git.ir/")}):
        with open(".links.txt", "a") as f:
            f.write(link.get('href') + '\n')

    return folder_title


def download_files(folder_title):
    """
    Download files when the given URL is parsed
    """
    os.system('echo Creating folder')
    os.system(f'mkdir {folder_title}')
    os.system('echo Initiating download...')
    os.system(f"cd {folder_title} && wget -i ../.links.txt")


def start():
    """
    entrypoint for the app
    """
    url = input("Input git.ir URL: ")
    folder_title = parse_url(url)
    download_files(folder_title)


start()
