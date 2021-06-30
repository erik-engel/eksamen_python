import os
from contextlib import contextmanager

# cwd = os.getcwd()
# os.chdir('Sample-Dir-One')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)

#context manager med en generator funktion

#context mangager decorator
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield # so we are ready to do whatever we want in that destination
    finally:
        os.chdir(cwd)

with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())