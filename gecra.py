import urllib.request, urllib.parse, urllib.error
import re
import ssl
from bs4 import BeautifulSoup
# Ignore SSL certificate errors
b =''
lists = []
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#soup = BeautifulSoup(html, 'html5lib')
#soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all('a'):
    lists.append(link.get('href'))
#print(lists)
fout = open('output.txt','w', encoding='utf-8')
rewhatrufinding = input('Enter RE-')
rewhatsurcontent = input('Enter content-')
for list in lists:
    link = re.findall(rewhatrufinding ,list)
    if len(link) > 0:
        print(link)

#"""

    if len(link) > 0:
        site = link[0]
        html = urllib.request.urlopen(site, context = ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        txtcon = soup.find('div',{"id":rewhatsurcontent})
        print(txtcon)
        fout = open('output.txt','w')
        fout.write(str(txtcon.decode()))
        fout.close()
#"""
