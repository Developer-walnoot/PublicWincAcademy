__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'
import os
import shutil
from zipfile import ZipFile

cache = "cache"
data = "data.zip"
current = os.getcwd()
def clean_cache():
    if os.path.isdir('cache') == True:
        shutil.rmtree(os.path.join(os.getcwd(), cache))
    os.mkdir("cache")
    return 0

def cache_zip(zip_path, cache_path):
    clean_cache()
    with ZipFile('data.zip', 'r') as zipObj:
        zipObj.extractall('cache')
    return 0

def cached_files(): 
    x = os.listdir(os.path.join(current, cache))
    abs_path = []
    for i in x:
        abs_path.append(os.path.join(current, cache, i))
    return abs_path

def find_password(abs_path):
    check_for = "password"
    for i in abs_path:
        x = open(i)
        all_x = x.readlines()
        for i in all_x:
            check = i[:-1]
            if check_for in str(check):
                new = check
    new = new[len(check_for) + 2:]
    return new




