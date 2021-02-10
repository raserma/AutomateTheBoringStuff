#!/usr/bin/env python3
# search_large_files.py - walks through a folder tree and
# searches for exceptionally large files or folders.

import pyinputplus as pyip
from pathlib import Path
import os, shutil


def search(path, min_size):
    """Walks through a path tree and prints all files larger than 'min_size'"""

    # Walks through a path tree
    for folder_name, subfolders, filenames in os.walk(path):
        for filename in filenames:
            # Gets size filename and converts it to MBs
            try:
                abs_path = os.path.abspath(os.path.join(folder_name, filename))
                size = os.path.getsize(abs_path) / (1024*1024)
            # Some files format break
            except OSError as err:
                continue

            # Searches for files larger than size
            if size > min_size:
                print(f'File {abs_path}, size: {int(size)} MBs')


def main():
    size = 1000 #  MB
    # Gets user's input
    print('Please, introduce an existing directory to search')
    search_path = pyip.inputFilepath()
    path = Path(search_path)

    # Checks user's input
    print('Path selected:', path)
    if not path.exists():
        raise Exception('Path introduced doesn\'t exist. Aborting.')
    if not path.is_dir():
        raise Exception('Path introduced is not a directory. Aborting.')

    search(path, size)


main()
