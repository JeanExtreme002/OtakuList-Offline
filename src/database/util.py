from shutil import rmtree
import os

def create_dir(path):
    return os.mkdir(path)

def join_path(*paths):
    return os.path.join(*paths)

def path_exists(path):
    return os.path.exists(path)

def remove_dir(path):
    return rmtree(path, ignore_errors = True)

def split_dir(path):
    return os.path.split(path)

def text_to_ascii_code(text):
    return ",".join([str(ord(char)) for char in text])
