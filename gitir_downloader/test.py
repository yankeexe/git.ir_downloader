import os
import argparse

import re
import argparse
from pathlib import Path

import requests
from tqdm import tqdm
from pyfiglet import Figlet
from bs4 import BeautifulSoup


ROOT_PATH = Path(__file__).resolve().parents[1]


links_path = ROOT_PATH/".links.txt"


def init_argparse():
    """
    Initialize argparse module for commandline argument parsing.
    """
    parser = argparse.ArgumentParser(description='Process git.ir links.', epilog = "Enjoy the program :)")

    # parser.add_argument('link', type = str, help = "git.ir URL")
    parser.add_argument('-n', '--name', help = "Folder name to store the downloaded files")
    parser.add_argument('-e', '--extract', help = "Used in case of a zipped file", default = True)

    return parser.parse_args()


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

    # if links_path.is_file():
    #     with open('.links.txt', 'r+') as f:
    #         if len(f.read()):
    #             f.truncate(0)
    # else:
    #     links_path.touch()

    LINKS_STORE = []

    for link in soup.findAll('a', attrs={'href': re.compile("^https://cdn[0-9]+.git.ir/")}):
        LINKS_STORE.append(link.get('href'))
        # with open(links_path, "a") as f:
        #     f.write(link.get('href') + '\n')

    return folder_title, LINKS_STORE


def download_files(args: str = ''):
    """
    Download files when the given URL is parsed
    """
    if args:
        name = args.name
    # name = folder_title

    # dir_path = ROOT_PATH/name

    os.system('echo Creating folder')
    # dir_path.mkdir()
    f = Figlet(font='slant')
    print(f.renderText('Downloading...'))
    # print(f"wget -i {links_path} -P {dir_path}/")

    url = 'https://cdn8.git.ir/1397/10/Packtpub%20Angular%20Full%20App%20with%20Angular%20Material%20Angularfire%20and%20NgRx%20%5BVideo%5D_git.ir.part3.rar'
    r = requests.get(url, stream = True)
    total_size = int(r.headers.get('content-length'))

    file = url.split('/')[-1]
    with open(file, 'wb') as f:
        with tqdm(total = total_size, desc = file, unit = "B", unit_scale = True,
                    bar_format='{l_bar: 20.0}{bar:10}{r_bar}{bar:-10b}') as pbar:
            for chunk in r.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))


def start():
    """
    entrypoint for the app
    """
    args = init_argparse()

    # folder_title, LINKS = parse_url(args)
    download_files(args)

start()

['https://cdn8.git.ir/1397/10/Packtpub%20Angular%20Full%20App%20with%20Angular%20Material%20Angularfire%20and%20NgRx%20%5BVideo%5D_git.ir.part1.rar\n',
 'https://cdn8.git.ir/1397/10/Packtpub%20Angular%20Full%20App%20with%20Angular%20Material%20Angularfire%20and%20NgRx%20%5BVideo%5D_git.ir.part2.rar\n',
 'https://cdn8.git.ir/1397/10/Packtpub%20Angular%20Full%20App%20with%20Angular%20Material%20Angularfire%20and%20NgRx%20%5BVideo%5D_git.ir.part3.rar']
