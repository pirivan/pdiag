import os
from pathlib import Path
from typing import List

from pdiagrams import __version__ as version


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
    return dir_walk([Path(root)])


def print_diagrams(diags: List):
    working_dir = Path.cwd()
    for d in diags:
        fig = d.read_text()
        os.chdir(d.parent)
        exec(fig)
        os.chdir(working_dir)


def main():
    print(f'Print Diagrams v{version}')
    dirs = find_directories('pdiagrams')
    diags = find_diagrams_files(dirs)
    print_diagrams(diags)


if __name__ == "__main__":
    main()
