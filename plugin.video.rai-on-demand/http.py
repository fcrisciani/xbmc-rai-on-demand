'''
Created on Nov 21, 2012

@author: flavio
'''
import urllib2

def getPage(url):
    """
    Makes an HTTP request and return the result of the url requested
    """
    print "HTTP - get url: " + url
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link