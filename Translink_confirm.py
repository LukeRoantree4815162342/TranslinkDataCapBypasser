#!/usr/bin/python
# coding: utf-8

import sys
import requests

if (sys.version_info < (3, 0)):
    from __future__ import print_function

headers = {
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Content-Length':'29',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'192.168.200.1',
'Referer':'http://192.168.200.1/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

data = 'action=connect&acceptTerms=on'
r = requests.Request('POST',url='http://192.168.200.1/index.php',headers=headers, data=data).prepare()
s = requests.Session()
print('\naccepting TOCs etc...')
print(s.send(r))



