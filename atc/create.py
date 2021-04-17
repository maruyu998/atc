from .contest import get_levels
import sys, os, shutil

BASEPATH = f'{os.path.dirname(__file__)}/_base.py'
UTILSPATH = f'{os.path.dirname(__file__)}/utils'

def _create_file(level):
    filename = f"{os.getcwd()}/{level}.py"
    if os.path.exists(filename):
        inp = input(f"{filename} is already exist. Override? [y/N] ")
        if inp != "y": print('keep the file:', filename); return

    with open(BASEPATH) as fr, open(filename, 'w') as fw:
        for line in fr:
            fw.write(line)
    print(f"created {filename}")

def _create_utils():
    dirname = f"{os.getcwd()}/utils/"
    if os.path.exists(dirname): return
    shutil.copytree(UTILSPATH, dirname)
    print(f"copied {dirname}")

def create(contest_name=None):
    for level in get_levels(contest_name):
        _create_file(level)
    _create_utils()