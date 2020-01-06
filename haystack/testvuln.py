import httplib
conn = httplib.HTTPConnection("10.10.10.115", "9200", True, 5)
conn.request("GET", '/_cat/master')
resp = conn.getresponse()
if resp.status == 200:
    print "exist vul"
