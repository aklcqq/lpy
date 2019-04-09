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
for list in lists:
    link = re.findall('^[0-9]{6}[0-9].html',list)
#    print(link)

    if len(link) > 0:
        site = link[0]
        html = urllib.request.urlopen(url+site, context = ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        for txtcon in soup.find('div',{'id':'content'}):
            print(txtcon) # to print content from novel websites
