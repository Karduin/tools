import pathlib
from pathlib import Path

folder = Path.cwd()
liste = [file for file in folder.iterdir()]
for item in liste:
    print(item.name)