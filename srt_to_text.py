"""Extract text from srt files and make text files.

Text only, without id, blank lines and time code.
"""

import pathlib
from pathlib import Path
import argparse

def get_srt_file(srt_file):
    """Load file in string.

    Check if file exist then return string if so.
    """
    try:
        with open(srt_file, 'r', encoding='utf-8') as input:
            in_file = input.read()
    except FileNotFoundError:
        print(f'File not found : {srt_file}')
    else:
        return in_file

def get_content(srt_string):
    """Get content from srt string and extract text.

    Make list from srt string then a sublist with text only.
    Return final string.
    """
    srt_list = srt_string.splitlines()
    srt_text_list = [item for item in srt_list if not item.isnumeric()
                     and item != '' and '-->' not in item]
    content = ' '.join(srt_text_list)
    return content

def process_file(file):
    """args.file != None"""
    path = pathlib.PurePath(file)
    if path.suffix != '.srt':
        print(f'Did you mean : {path.name}.srt ?')
    else:
        srt_string = get_srt_file(file)
        output = get_content(srt_string)
        path = path.with_name(path.stem + '.txt')
        write_file(path, output)
    return None

def process_directory(directory):
    """Process all srt files in the directory.

    If directory is not curret working directory make path object.
    Then process list of files.
    """
    if not isinstance(directory, pathlib.PurePath):
        directory = Path(directory)

    srt_list = [file for file in directory.rglob('*.srt') if file.is_file()]
    if not srt_list:
        print('No srt file in this directory.')
        return None
    else:
        for item in srt_list:
            process_file(item)
    return None

def write_file(path, output):
    """Write text file at the same path.
    """
    try:
        with open(path, 'w', encoding='utf-8') as output_txt:
            output_txt.write(output)
    except IOError:
        print('IO Error')
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='srt_to_text',
                                    description='Parse srt files')

    parser.add_argument('-f', '--file', required=False, help='Filename to process.')
    parser.add_argument('-d', '--directory', required=False, default=Path.cwd(), help='Directory to process.')

    args = parser.parse_args()

    if args.file:
        process_file(args.file)
    else:
        process_directory(args.directory)

