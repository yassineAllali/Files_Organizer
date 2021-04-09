from pathlib import Path
import datetime
from os import path
import shutil


def convert_date(timestamp):
    value = datetime.datetime.fromtimestamp(timestamp)
    return value.strftime('%Y-%m-%d')


selected_directory_path = 'C:\\Users\\PREDATOR\\Downloads'
base_path = Path(selected_directory_path)
files_in_base_path = base_path.iterdir()

# loop through the items of the selected directory
for item in files_in_base_path:
    # moving just files
    if item.is_file():
        info = item.stat()
        date = convert_date(info.st_ctime)
        # the absolute path to the file
        file_path = selected_directory_path + '\\' + item.name
        print(file_path + 'created at : ' + date)

        # the absolute path to the destination directory
        abs_dir_path = selected_directory_path + '\\' + date

        # if the destination directory doesn't exist we should create it first
        if not path.isdir(abs_dir_path):
            directory_path = Path(abs_dir_path)
            directory_path.mkdir()
            print('directory created')

        # move the file to the destination directory
        shutil.move(file_path, abs_dir_path)
