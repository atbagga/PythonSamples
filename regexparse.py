try:
    from urllib.parse import urlparse, quote
except ImportError:
    from urllib import quote
    from urlparse import urlparse

import re 

def uri_parse(url):
    return urlparse(url)

url1 = 'https://baggaatul24@dev.azure.com/baggaatul24/WikiMigrationScript/_git/abc123'
url = 'https://baggaatul24.visualstudio.com/DefaultCollection/WikiMigrationScript/_git/abc123'
print(re.search('https?://(\\w+).visualstudio.com/(\\w+)', url))
print(re.search('https://dev.azure.com/(\\w+)/(\\w+)', url1))


import pdb
pdb.set_trace()