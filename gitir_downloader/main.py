import os
import sys
import argparse

from gitir_downloader.parser import parse_url
from gitir_downloader.downloader import download_files

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def init_argparse():
    """
    Initialize argparse module for commandline argument parsing.
    """
    parser = argparse.ArgumentParser(
        description="Download video files from git.ir links.",
        epilog="Enjoy the program :)",
    )

    parser.add_argument("link", type=str, help="git.ir URL")
    parser.add_argument(
        "-n", "--name", help="Folder name to store the downloaded files"
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def start():
    """
    entry-point for the app
    """
    try:
        args: argparse.Namespace = init_argparse()

        folder_title, LINKS = parse_url(args)
        download_files(folder_title, LINKS, args)
    except KeyboardInterrupt:
        print("Stopped Downloading!" + " \N{cross mark}")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(os.EX_OK)
