import os
import binascii

def odd(num):
    if num%2==0:
        return True
    else:
        return False

for i in range(200):
	tokenno=binascii.b2a_hex(os.urandom(15))
	if(odd(i)):
		tokensalt="systemd-private-proc-"
		tokenend="-systemd-timesyncd.service-"
		tokenendsalt= binascii.b2a_hex(os.urandom(9))
		os.system("mkdir "+tokensalt+tokenno+tokenend+tokenendsalt)
	else:
		tokensalt="vmlinuxold_"
		tokenend="_systemd-resolved.service-JaNT_systemd-resolved.service-"
		tokenendsalt= binascii.b2a_hex(os.urandom(10))
		os.system("mkdir "+tokensalt+tokenno+tokenend+tokenendsalt)
