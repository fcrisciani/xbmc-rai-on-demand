'''
Created on Nov 21, 2012

@author: flavio
'''
import xbmc,os,sys,time

tempPath = xbmc.translatePath('special://temp/')


def getFileCache(name,freshnessSec):
    ''' Get a file from cache if exists and checks that is enough fresh '''
    result = None
    try:
        f = open(tempPath + name)
        # get the timestamp to understand if the file is still valid
        try:
            t = f.readline().rstrip()
            print 'localtime: ' +str(time.time())
            print 'savedTime: ' + t
            print 'difference: ' + str(time.time()-float(t))
            if (time.time()-float(t)) < freshnessSec:
                result = f.read()
                f.close()
                print 'getShowsWithLetterCache - RESULT CACHED'
        except:
            os.remove(tempPath + 'showIndex.txt')
    except:
        pass
    return result

def saveFileCache(name,file):
    try:
        os.remove(tempPath + "XBMC_RAI_" + name)
    except:
        pass
    f = open(tempPath + "XBMC_RAI_" + name,'w')
    f.write(str(time.time())+'\n')
    f.write(file)
    f.close()

def clearFileCache():
    for f in os.listdir(tempPath):
        if "XBMC_RAI_" in f:
            os.remove(tempPath+f) 
        