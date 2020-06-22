import os
import argparse
from pathlib import Path
from typing import List

from pdiagrams import __version__ as version

VERSION = f'Print Diagrams v{version}'


def find_diagrams_files(paths: List) -> List:
    diags = []
    for p in paths:
        diags += [x for x in p.iterdir() if x.is_file() and x.suffixes == ['.diag', '.py']]
    return diags


def find_directories(root: str) -> List:
    def dir_walk(p: List) -> List:
        if not p:
            return p
        dirs = []
        for d in p:
            dirs += [x for x in d.iterdir() if x.is_dir()]
        return p + dir_walk(dirs)

    path = Path(root)
    if not path.is_dir():
        raise FileNotFoundError(f'no such directory "{root}"')
    return dir_walk([path])


def print_diagrams(diags: List):
    working_dir = Path.cwd()
    for d in diags:
        fig = d.read_text()
        os.chdir(d.parent)
        exec(fig)
        os.chdir(working_dir)


def parse_arguments():
    parser = argparse.ArgumentParser(prog='pdiagrams',
                                     description='generate diagram images from diagram source files')
    parser.add_argument('--version',
                        action='version',
                        version=VERSION)
    parser.add_argument('--root',
                        required=True,
                        action='append',
                        help='top folder to start searching for diagrams to print')
    return parser.parse_args()


def main():
    args = parse_arguments()
    print(VERSION)
    for root in args.root:
        try:
            dirs = find_directories(root)
        except FileNotFoundError as err:
            print(f'FileNotFoundError: {err}')
        else:
            diags = find_diagrams_files(dirs)
            print_diagrams(diags)


if __name__ == "__main__":
    main()
