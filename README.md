# Data Platform Diagrams

This project uses the [Diagrams](https://diagrams.mingrammer.com/) Python library to
generate image files.

Usage:

```bash
pdiag --root=some_dir --root=some_other_dir
```

`pdiag` visits each of the directories specified in the `--root` arguments and recursively
scans them looking for files with the `.diag.py` suffix in the file name. These files are
assumed to be "Diagrams" files which can be rendered into image files such as PNG and JPEG.

`pdiag` then executes the code in each of the diagram files to generate the corresponding
image output file. The latter is placed in the same directory where the source file is
located.
