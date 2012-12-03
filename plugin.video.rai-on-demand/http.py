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
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link