import urllib
from http.client import *
from xml.dom.minidom import parse

conn = HTTPConnection('site.com')

conn.request('GET', '/store/api/categories')
resp = conn.getresponse()

dom = parse(resp.read())

categories = [c.data.strip() for c in dom.getElementsByTagName('name')]]

files = []
for category in categories:
    conn.request('GET', 'store/api/category/%s/1-10' % category)
    resp = conn.getresponse()
    dom = parse(resp.read())
    files.append([c.data.trim() for c in dom.getElementsByTagName('name')])

for file in files:
    conn.request('GET', 'store/api/file/%s/1-10' % file)
    resp = conn.getresponse()
    dom = parse(resp.read())
    fname = dom.getElementsbyTagName('name')[0].data.trim()
    conn.request('GET', 'store/%' % filename)
    resp = conn.getresponse
    file = open(filename, 'w+')
    file.write(resp.read)
    file.close()
