import os
import re
import urllib
import urllib2
import sys

if len(sys.argv) != 4:
           print "Usage: python github_crawl.py <language> <query> <pages>"
           sys.exit()

language = sys.argv[1]
query = sys.argv[2]
pages = sys.argv[3]

for page in list(range(1, int(pages))):
           url = 'https://api.github.com/search/repositories'
           values = {'q' : query + '+language:' + language,\
                     'sort' : 'stars',\
                     'order' : 'desc',\
                     'page' :  str(page),\
                     'per_page' : '100'}
           print values
           data = urllib.urlencode(values)
           response = urllib2.urlopen(url + '?' + data)

           html = response.read()
          
           matches = {e for e in set(re.findall('\"full\_name\"\:\"([^"]*)"', html))}
           for match in matches:
                      nameList = match.split('/')
                      user = nameList[0]
                      app = nameList[1]
                      print user + " : " + app
                      
