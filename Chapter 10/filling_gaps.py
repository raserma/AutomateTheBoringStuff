#!/usr/bin/env python3
# filling_gaps.py - it finds all files with a given prefix, locates any
# gaps in the numbering and rename them to close the gap

#   THIS EXERCISE IS NOT WORKING CORRECTLY YET

# Example:
#   - input: example002.txt, example003.txt, example007.txt
#   - output: example001.txt, example002.txt, example003.txt


# Note:
#   - generate_random_files() and remove_random_files() functions are not required by the exercise.
#   They were added to automate the creation / removal of the test examples
#   needed to run the program.
#   - To keep it simple, the program renames all the files into a sorted
#   list.

import pyinputplus as pyip
from pathlib import Path
import os, random, shutil, re


def create_new_folder(path):
    """Creates a new folder. Skipped if folder already exists"""
    try:
        os.makedirs(path)
        print('New folder created at:', path.absolute())
    except FileExistsError as err:
        print(f'Folder {path} already exists. Continuing')


def generate_random_files(source, num_files, ext):
    """Creates a new folder with N files and 'ext' extension"""

    # Checks user's input
    path = Path(source).absolute()
    print('Source path selected:', path)
    if not path.exists():
        raise Exception('Path introduced doesn\'t exist. Aborting.')
    if not path.is_dir():
        raise Exception('Path introduced is not a directory. Aborting.')

    # Creates a new folder
    new_folder = 'source_examples'
    new_path = Path(source) / new_folder
    create_new_folder(new_path)

    # Generates 'num_files' with extension 'ext' in the new folder
    random_list = []
    for i in range(num_files):
        r = random.randint(0, num_files*10)
        if r not in random_list:
            random_list.append(r)
            filename = f'example{str(r).zfill(3)}.{ext}'
            with open(new_path / filename, 'w'):
                print(f'New filename created: {new_path}/{filename}')

    print('Examples successfully created under:', new_path.absolute())
    return new_path


def remove_folder(path):
    """Removes a folder"""
    shutil.rmtree(path.absolute())
    print(f'Folder \'{path.absolute()}\' was removed.')


def fill_gaps(path, ext):
    """Close the gaps in the numbered filenames"""

    count = 1
    # Note: Couldn't make it work using f-strings inside the regex
    file_regex = re.compile(r'(.*)(\d{3})(\.' + ext + ')$')
    print(file_regex)
    for filename in path.glob(f'*.{ext}'):

        path_name = os.path.abspath(path)
        print(path_name)
        file_name = os.path.basename(filename)
        abs_filename = os.path.join(os.path.abspath(path), os.path.basename(filename))
        print(abs_filename)
        match = file_regex.search(file_name)
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
        if match:
            old_name = file_name
            old_filename = os.path.join(path_name, old_name)
            new_name = match.group(1) + str(count).zfill(3) + match.group(3)
            new_filename = os.path.join(path_name, new_name)
            if
            print(f'Renaming {old_filename} to {new_filename}')
            shutil.move(old_filename, new_filename)
            count += 1


def main():
    # Example data - to change as desired
    ext = 'txt'
    num_files = 10

    # Gets user's input and generates the example extensions
    print('Please, introduce an existing source path. Press . for current directory')
    source_path = pyip.inputFilepath()

    # Generates 10 files with random numbered names
    source_path = generate_random_files(source_path, num_files, ext)

    fill_gaps(source_path, ext)


    # Removes the examples created
    #remove_folder(source_path)

main()