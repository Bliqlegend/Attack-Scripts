#usr/bin/python

import os

#process killer
while 1:
    os.system("who -a")
    os.system("man ps")
    b = list(map(int, input("Kill>").split()))
    for i in b:
        os.system("kill -9 "+i)
        os.system("pkill "+i)⏎
