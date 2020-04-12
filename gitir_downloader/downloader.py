""" Downloader for git.ir links """
import time
import argparse
from pathlib import Path

import requests
from tqdm import tqdm
from halo import Halo


ROOT_PATH = Path(__file__).resolve().parents[1]

links_path = ROOT_PATH / ".links.txt"


def download_files(folder_title, LINKS, args: argparse.Namespace):
    """
    Download files when the given URL is parsed
    """

    links_len = len(LINKS)

    if args.name:
        dir_path = ROOT_PATH / args.name
    else:
        dir_path = ROOT_PATH / folder_title

    # Create folder
    spinner = Halo(text="Creating folder", spinner="dots")
    spinner.start()

    dir_path.mkdir()
    spinner.stop_and_persist(symbol="✅".encode("utf-8"), text="Folder Created")

    print(f"Total files: {links_len}")

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

        with open(dir_path / file, "wb") as f:
            with tqdm(
                total=total_size,
                desc=file,
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
