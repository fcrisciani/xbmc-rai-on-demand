'''
Created on Nov 21, 2012

@author: flavio
'''
import request,sys

request.indexReq()
print request.indexShowList('/dl/RaiTV/programmi/page/Page-86e553b7-5d8c-4375-809c-1bf1c879c1c3.html', 0)

def getParams():
    print "ARGUMENTS: "
    print sys.argv
    
    resultDict = {}
    
    if len(sys.argv) > 1 and len(sys.argv[3]) > 1:
        paramList = sys.argv[3][1:].split('&')
        for elem in paramList:
            token = elem.split('=')
            if len(token) == 2:
                resultDict[token[0]] = token[1]
    
    return resultDict

print getParams()