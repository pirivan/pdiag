from pathlib import Path
from pdiagrams import __version__
from pdiagrams.cli import find_diagrams as gen_images

ROOTS = [
    'tests/examples',
    'tests/architecture'
]

OUTPUT = """Print Diagrams v0.1.0
tests/examples/dir1/message_collecting.diag.py
tests/examples/dir1/dir2/three_replicas.diag.py
tests/architecture/platform.diag.py
tests/architecture/web_service.diag.py
"""


def _cleanup():
    p = Path('.')
    for f in list(p.glob('**/*.png')):
        f.unlink()


def test_version():
    assert __version__ == '0.1.0'


def test_gen_files(capsys):
    gen_images(ROOTS)
    captured = capsys.readouterr()
    assert captured.out == OUTPUT
    _cleanup()
