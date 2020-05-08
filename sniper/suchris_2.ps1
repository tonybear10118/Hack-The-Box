$username = "SNIPER\chris" ; $pw = "36mEAhz/B8xQ~2VM"
$password = $pw | ConvertTo-SecureString -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $username,$password
New-PSSession -Credential $cred | Enter-PSSession
