'''
Write out a program that recursively crawls a target directory
and prints out all the subdirectories, files, and folders.

Once the program is done executing, it should be in the same
directory from which the python program was run. You do not have
to change directories to solve this problem.
'''
from util import *

def crawl_directory(path):
    for fname in os.listdir(path):
        print(fname)
        if os.path.isdir(os.path.join(path, fname)) == True:
            crawl_directory(os.path.join(path, fname))
    return None


if __name__ == "__main__":
  crawl_directory('example_dir')
