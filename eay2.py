

import compileall



import sys

import pathlib

compileall.compile_dir(pathlib.Path('formEAY/'), force=True)


print(sys.version)

x=input('terminar')
