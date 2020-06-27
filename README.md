# Data Platform Diagrams
This project uses the [Diagrams](https://diagrams.mingrammer.com/) Python library to
generate image files.

## Installing the software
Download the wheel file of the [latest release](https://github.com/pirivan/pdiag/releases)
and run the following commands (adjust the release number as required):

```bash
pip install diagrams pdiagrams-0.1.0-py3-none-any.whl
```

## Usage
The name of the executable is `pdiag`. Use it as follows:

```bash
pdiag --root=some_dir --root=some_other_dir
```

`pdiag` visits each of the directories specified in the `--root` arguments (there can be as
many --root arguments as you may need), and recursively scans them looking for files with
the `.diag.py` suffix in the file name. These files are assumed to be "Diagrams" files which
can be rendered into image files such as PNG and JPEG.

`pdiag` then executes the code in each of the diagram files to generate the corresponding
image output files. The latter are placed in the same directory where the source files are
located.

## Development
You need to install [Poetry](https://python-poetry.org/) which this project uses to manage
the development environment.

Once you clone the repository run the following command to update the development dependencies:

```bash
poetry update
```

Other commands to use include:

```bash
poetry run pdiag --root tests  # run the code
poetry run pytest  # run the test suite
poetry build  # build distribution binaries
```
