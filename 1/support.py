from unittest import skip


from os import walk


def import_folder(path):
    for information in walk(path):
        print(information)
