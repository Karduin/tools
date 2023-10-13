"""
Extract text from srt files and make text files
"""

import pathlib
from pathlib import Path
import argparse

def get_srt_file(srt_file):
    try:
        with open(srt_file, 'r', encoding='utf-8') as input:
            in_file = input.read()
            return in_file
    except FileNotFoundError:
        print(f'File not found : {srt_file}')

"""folder = Path.cwd()
liste = [file for file in folder.iterdir()]
for item in liste:
    print(item.name)
"""
def get_content(srt_file):
    """
    Get content from srt file and extract text
    """
    srt_file = srt_file.splitlines()
    srt_to_list = [item for item in srt_file if not item.isnumeric()
                   and item != '' and '-->' not in item]
    content = ' '.join(srt_to_list)
    return content

"""

content = get_content(srt_file)
print(content)
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='srt_to_text',
                                    description='Parse srt files',
                                    epilog='bottom text')

    parser.add_argument('-f', '--file', required=False, help='Filename to process.')
    parser.add_argument('-d', '--directory', required=False, default=Path.cwd(), help='Directory to process.')

    args = parser.parse_args()

    if args.file:
        """args.file != None"""
        if pathlib.PurePosixPath(args.file).suffix != '.srt':
            print(f'Did you mean : {args.file}.srt ?')
        else:
            print(args.file)
            result = get_srt_file(args.file)
            result2 = get_content(result)

            print(result2)
