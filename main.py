#!C:\Python34\python

__author__ = 'Alexander'

import os
import re


def main():

    #for user.
    #path, show = map(str, input("Enter path and TV show. format = path,show: ").split(','))
    #print('Entered path: ', path)
    #print('Entered show ', show)

    aviFiles = re.compile(r'.*\.avi$')
    #for fixing input:
    splitter = re.compile(r'[.-]+')

    #for programmer.
    path = 'downloads'
    show = 'tmp'

    show = ' '.join(splitter.split(show))


    l=[]
    for root, dirs, files in os.walk(path):
        for name in files:
            if aviFiles.search(name):
                l.append(os.path.join(root, name))

    #prints all file.avi paths in downloads(root)
    #for i in l:
        #print(i)


    #creates folder if it does not exist
    folder = os.path.join(path, show)
    if not os.path.exists(folder):
        os.mkdir(folder)
        print('%s was created' % folder)



if __name__ == "__main__":
    main()

