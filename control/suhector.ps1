$username = "CONTROL\hector" ; $pw = "l33th4x0rhector"
$password = $pw | ConvertTo-SecureString -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $username,$password
New-PSSession -Credential $cred | Enter-PSSession
