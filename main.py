__author__ = 'Alexander'

import os
import re
import sys


def main():

    aviFiles = re.compile(r'.*\.avi$')


    l=[]
    for root, dirs, files in os.walk('downloads'):
        for name in files:
            if aviFiles.search(name):
                l.append(os.path.join(root, name))

    #prints all file.avi paths in downloads(root)
    for i in l:
        print(i)


    path = os.path.join('downloads', 'tmp')
    print(path)

    #creates downloads\tmp folder if it does not exist
    if not os.path.exists(path):
        os.mkdir(path)



if __name__ == "__main__":
    main()

