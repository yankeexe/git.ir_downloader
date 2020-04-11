""" Downloader for git.ir links """
import os
import re
import argparse

import requests
from pyfiglet import Figlet
from bs4 import BeautifulSoup

from .constants import ROOT_PATH

links_path = ROOT_PATH/".links.txt"


def parse_url(args: argparse.Namespace) -> str:
    """
    Prase url and extract links
    """
    url = args.link

    try:
        page = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    soup = BeautifulSoup(page.content, "html.parser")

    split_url = url.split("/")[-2:]
    folder_title = split_url[0]

    if links_path.is_file():
        with open('.links.txt', 'r+') as f:
            if len(f.read()):
                f.truncate(0)
    else:
        links_path.touch()


    for link in soup.findAll('a', attrs={'href': re.compile("^https://cdn[0-9]+.git.ir/")}):
        with open(links_path, "a") as f:
            f.write(link.get('href') + '\n')

    return folder_title


def download_files(folder_title: str, args: str = ''):
    """
    Download files when the given URL is parsed
    """
    if args:
        name = args.name
    name = folder_title

    dir_path = ROOT_PATH/name

    os.system('echo Creating folder')
    dir_path.mkdir()
    f = Figlet(font='slant')
    print(f.renderText('Downloading...'))
    print(f"wget -i {links_path} -P {dir_path}/")
    os.system(f"wget -i {links_path} -P {dir_path}/")
