import socket
import os
import random

#OWN the control
os.chdir("/root")
os.system("chmod 777 king.txt") #give all perm
os.system("rm -f -r king.txt") #remove the file
os.system("touch king.txt") # make the file again
os.system("echo 'cultholmes'>king.txt")  #write kings name
os.system("chmod 000 king.txt") #perm 000 file
os.system("chattr +i -V king.txt") #own the file
l = ["wnnacary","ma1lwafre","imaima","stuxnet","v1g1lant3"]
#Kick them out
for i in range(1000000):
    r = random.randint(0,4)
    god = input("Check >")
    if god == 'y':
        os.system("who -u")
        wannacry = input("Kill >" )
        if wannacry == 'y':
            d = int(input("PID >"))
            os.system("kill -HUP "+d)

        else:
            os.chdir("/root")
            os.system("touch "+l[r]+".txt")
            os.system("touch wa?nn?abekin?g.txt")
            os.system("echo 'lol fuckoff'> wa?nn?abekin?g.txt")
            continue
    else:
        os.chdir("/root")
        os.system("touch "+l[r]+".txt")
        os.system("touch wa?nn?abekin?g.txt")
        os.system("echo 'lol fuckoff'> wa?nn?abekin?g.txt")
        continue
