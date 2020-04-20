""" Downloader for git.ir links """
import argparse
import time
from pathlib import Path
from typing import List

import requests
from halo import Halo
from tqdm import tqdm


def download_files(folder_title: str, LINKS: List[str], args: argparse.Namespace):
    """
    Download files when the given URL is parsed
    """

    ROOT_PATH = Path.cwd()
    links_len = len(LINKS)

    if args.name:
        dir_path = ROOT_PATH / args.name
    else:
        dir_path = ROOT_PATH / folder_title

    # Create folder
    spinner = Halo(text="Creating folder", spinner="dots")
    spinner.start()
    try:
        dir_path.mkdir()
    except FileExistsError as _:
        pass
    spinner.stop_and_persist(symbol="✅".encode("utf-8"), text="Folder Created")

    print(f"Total files: {links_len}")
    print(f"Download Path: {dir_path}")

    # Start download
    for index, url in enumerate(LINKS):
        r = requests.get(url, stream=True, headers={"Accept-Encoding": None})
        total_size = int(r.headers.get("Content-Length"))

        spinner.text = f"Downloading {index + 1}/{links_len} file"
        spinner.spinner = "arrow3"
        spinner.start()
        time.sleep(1)
        spinner.stop()

        file = url.split("/")[-1]
        file = (file[:50] + "...") if len(file) > 50 else file
        with open(dir_path / file, "wb") as f:
            with tqdm(
                total=total_size,
                desc=f"{file:<53}",
                unit="B",
                unit_scale=True,
                bar_format="{l_bar}{bar:20}{r_bar}{bar:-10b}",
            ) as pbar:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))

    spinner.spinner = "monkey"
    spinner.start()
    time.sleep(2)
    spinner.stop_and_persist(symbol="🔥".encode("utf-8"), text="All files downloaded.")
