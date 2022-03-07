import os


def check_and_fix_directory(dir_name):
    """This function is using for creating given directpry, if it is not exists."""
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
