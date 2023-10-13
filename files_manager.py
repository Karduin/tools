import pathlib
from pathlib import Path
import argparse


"""folder = Path.cwd()
liste = [file for file in folder.iterdir()]
for item in liste:
    print(item.name)
"""

parser = argparse.ArgumentParser(prog='srt_to_text',
                                 description='Parse srt files',
                                 epilog='bottom text')

parser.add_argument('-f', '--file', required=False, help='Filename to process.')
parser.add_argument('-d', '--directory', required=False, default=Path.cwd(), help='Directory to process.')

args = parser.parse_args()

print(args.file, args.directory)