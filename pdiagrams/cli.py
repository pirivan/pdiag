import os
import argparse
from pathlib import Path

from pdiagrams import __version__ as version

VERSION = f'Print Diagrams v{version}'


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


def print_diagrams(diagrams):
    working_dir = Path.cwd()
    for d in diagrams:
        fig = d.read_text()
        os.chdir(d.parent)
        print(d)
        exec(fig)
        os.chdir(working_dir)


def find_diagrams(roots):
    print(VERSION)
    diagrams = []
    for root in roots:
        p = Path(root)
        diagrams += list(p.glob('**/*.diag.py'))
    print_diagrams(diagrams)


def main():
    args = parse_arguments()
    find_diagrams(args.root)


if __name__ == "__main__":
    main()
