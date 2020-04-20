""" Remove '-git-ir from the filename """
import os
from typing import List


def tidy_names(filenames: List[str]) -> List:
    """
  Clean the file name by removing -git.ir at the end.

  Args:
    filenames: List of file names to split.
  """
    name_store = []

    for name in filenames:
        _, ext = os.path.splitext(name)
        split = name.split("-")[:-1]
        name_store.append("-".join(split) + ext)

    return name_store
