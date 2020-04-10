import re
import os
import requests
import argparse

from bs4 import BeautifulSoup

from constants import PACKAGE_MANAGERS


def init_argparse():
    parser = argparse.ArgumentParser(description='Process git.ir links.')

    parser.add_argument('link', type = str, help = "git.ir URL")
    parser.add_argument('-n', '--name', help = "Folder name to store the downloaded files")
    parser.add_argument('-e', '--extract', help = "Used in case of a zipped file", default = True)

    return parser.parse_args()


def identify_system():
    """
    Identify the package manager for the system.
    """
    for name in PACKAGE_MANAGERS:
        console_out = os.popen(f'which {name}').read()

        if '/usr/bin' in console_out:
            return name


def parse_url(args):
    """
    Prase url and extract links
    """
    url = args.link
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


def download_files(folder_title, args = ''):
    """
    Download files when the given URL is parsed
    """
    if args:
        name = args.name
    name = folder_title

    os.system('echo Creating folder')
    os.system(f'mkdir {name}')
    os.system('echo Initiating download...')
    os.system(f"cd {name} && wget -i ../.links.txt")


def start():
    """
    entrypoint for the app
    """
    args = init_argparse()

    folder_title = parse_url(args)
    download_files(folder_title, args)


start()
