""" Constants for the script. """
from pathlib import Path

PACKAGE_MANAGERS = ['whatever', 'pacman', 'apt']

# ROOT_PATH = Path(__file__).parent / "../"
ROOT_PATH = Path(__file__).resolve().parents[1]
