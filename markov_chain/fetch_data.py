"""
fetch_data module
15 November 2018
"""


#extract data from website
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

import urllib2
from bs4 import BeautifulSoup

def get_data(source):

	req = urllib2.Request(source)
	response = urllib2.urlopen(req)

	text = response.read()

	response.close()

	text = BeautifulSoup(text, "html.parser").get_text(strip=True)

	return text


