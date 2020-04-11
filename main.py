import os
import argparse

from gitir_downloader.constants import PACKAGE_MANAGERS
from gitir_downloader.downloader import parse_url, download_files


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def init_argparse():
    """
    Initialize argparse module for commandline argument parsing.
    """
    parser = argparse.ArgumentParser(description='Process git.ir links.', epilog = "Enjoy the program :)")

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


def start():
    """
    entrypoint for the app
    """
    args = init_argparse()

    folder_title = parse_url(args)
    download_files(folder_title, args)


start()
