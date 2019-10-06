import shutil


def move_files(source_files, destination_folder):
    for file in source_files:
        shutil.move(file, destination_folder)