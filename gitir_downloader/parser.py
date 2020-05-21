""" Parse URL and scrape relevant links. """
import re
import argparse
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup

from gitir_downloader.utils.tidy_names import tidy_names


def parse_url(args: argparse.Namespace) -> Tuple[str, List]:
    """
    Parse url and extract links
    """
    url = args.link

    try:
        page = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    soup = BeautifulSoup(page.content, "html.parser")

    split_url = url.split("/")[-2:]
    folder_title: str = split_url[0]

    LINKS_STORE: List[str] = []

    for link in soup.findAll(
        "a", attrs={"href": re.compile("^https://cdn(\d?)+.git.ir/")}
    ):
        LINKS_STORE.append(link.get("href"))

    # names = tidy_names(LINKS_STORE)

    return folder_title, LINKS_STORE
