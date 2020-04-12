""" Parse URL and scrape relevant links. """
import re
import argparse
from typing import List

import requests
from bs4 import BeautifulSoup


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
    folder_title: str = split_url[0]

    LINKS_STORE: List[str] = []

    for link in soup.findAll(
        "a", attrs={"href": re.compile("^https://cdn[0-9]+.git.ir/")}
    ):
        LINKS_STORE.append(link.get("href"))

    return folder_title, LINKS_STORE
