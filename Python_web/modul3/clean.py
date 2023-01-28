#!/usr/bin/python3
from threading import Thread
import logging
import os
import sys
from pathlib import Path
import re
from shutil import move, unpack_archive

START_FOLDER = ""
if len(sys.argv) > 1:
    START_FOLDER = sys.argv[1]
else:
    print("No arguments passed")
    exit(22)

if not Path(START_FOLDER).exists:
    print('Folder not exists')
    exit(20)

IMAGE_PATH = os.path.join(START_FOLDER, 'images')
DOCUMENT_PATH = os.path.join(START_FOLDER, 'documents')
AUDIO_PATH = os.path.join(START_FOLDER, 'audio')
VIDEO_PATH = os.path.join(START_FOLDER, 'video')
ARCHIVES_PATH = os.path.join(START_FOLDER, 'archives')
OTHER_PATH = os.path.join(START_FOLDER, 'other')

Path(IMAGE_PATH).mkdir(exist_ok=True)
Path(DOCUMENT_PATH).mkdir(exist_ok=True)
Path(AUDIO_PATH).mkdir(exist_ok=True)
Path(VIDEO_PATH).mkdir(exist_ok=True)
Path(ARCHIVES_PATH).mkdir(exist_ok=True)
Path(OTHER_PATH).mkdir(exist_ok=True)

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

image_list = []
document_list = []
audio_list = []
video_list = []
archives_list = []
other_list = []
suffixes_list = set()
other_suffixes_list = set()


def normalize_name(name):
    new_name = ''
    for char in name:
        if re.search(r'[0-9A-z]', char):
            char = char
        elif re.search(r'[А-Яа-яёєіїґ]', char):
            char = TRANS[ord(char)]
        else:
            char = '_'
        new_name += char
    return new_name


def sort(now_folder):
    for item in Path(now_folder).iterdir():
        threads = []
        if item.is_dir():
            if item.name not in ('images', 'documents', 'audio', 'video', 'archives', 'other'):
                th = Thread(target=sort, args=(item,))
                th.start()
                threads.append(th)

        if item.is_file():
            normalized_file_name = normalize_name(item.stem) + item.suffix
            if item.suffix.lower() in ('.jpeg', '.png', '.jpg', '.svg'):
                image_list.append(normalized_file_name)
                suffixes_list.add(item.suffix)
                move(item, os.path.join(IMAGE_PATH, normalized_file_name))

            elif item.suffix.lower() in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.ppt'):
                document_list.append(normalized_file_name)
                suffixes_list.add(item.suffix)
                move(item, os.path.join(DOCUMENT_PATH, normalized_file_name))

            elif item.suffix.lower() in ('.mp3', '.ogg', '.wav', '.amr'):
                audio_list.append(normalized_file_name)
                suffixes_list.add(item.suffix)
                move(item, os.path.join(AUDIO_PATH, normalized_file_name))

            elif item.suffix.lower() in ('.avi', '.mp4', '.mov', '.mkv'):
                video_list.append(normalized_file_name)
                suffixes_list.add(item.suffix)
                move(item, os.path.join(VIDEO_PATH, normalized_file_name))

            elif item.suffix.lower() in ('.zip', '.gz', '.tar'):
                archives_list.append(normalized_file_name)
                suffixes_list.add(item.suffix)
                unpack_archive(item, os.path.join(ARCHIVES_PATH, normalize_name(item.stem)))
                os.remove(item)

            else:
                other_list.append(item.name)
                other_suffixes_list.add(item.suffix)
                move(item, os.path.join(OTHER_PATH, item.name))

        # join
        [th.join() for th in threads]
        if item.is_dir():
            if item.name not in ('images', 'documents', 'audio', 'video', 'archives', 'other'):
                Path(item).rmdir()


if __name__ == "__main__":
    sort(START_FOLDER)

    print(f'''\n
            image_list={image_list}\n
            document_list={document_list}\n
            audio_list={audio_list}\n
            video_list={video_list}\n
            archives_list={archives_list}\n
            other_list={other_list}\n
            suffixes_list={suffixes_list}\n
            other_suffixes_list={other_suffixes_list}\n''')