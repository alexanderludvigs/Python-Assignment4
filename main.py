__author__ = 'Alexander'

import os
import re



def main():

    aviFiles = re.compile(r'.*\.avi$')

    l=[]
    for root, dirs, files in os.walk('downloads'):
        for name in files:
            if aviFiles.search(name):
                l.append(os.path.join(root, name))

    print(l)



    for i in l:
        if i != None:
            print(aviFiles.findall(i))





if __name__ == "__main__":
    main()
