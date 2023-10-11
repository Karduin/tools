"""
Extract text from srt files and make text files
"""

import pathlib
from pathlib import Path
import argparse


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

"""try:
    with open('course1.srt', 'r', encoding='utf-8') as input:
        srt_file = input.read()

except IOError:
    print(f'file error')

content = get_content(srt_file)
print(content)
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()