'''
Created on Nov 23, 2012

@author: flavio
'''

import urllib,sys,request,xbmcWrapper,json

pluginId = 0

#addon id - name of addon directory
_id='plugin.video.rai-on-demand'
#resources directory
_resdir = "special://home/addons/" + _id + "/resources" #add our library to python search path
sys.path.append( _resdir + "/lib/")

def loggerMethod(top,log):
    print '#############################'
    print top + '-' + log

def addLetterIndex():
    ''' This method creates the list of initial letter of all shows '''
    global pluginId,base_url
    
    letterList = request.letterIndexReq()
    
    for letter in letterList:
        xbmcWrapper.addFolder(pluginId,1,letter,{'letter': letter})
    xbmcWrapper.endOfContent(pluginId)
    
def addTvShowsByLetter(paramDict):
    ''' This methods create the list of shows starting with letter '''        
    showList = request.showsWithLetterReq(paramDict['letter'])   
    
    for elem in showList:
        xbmcWrapper.addFolder(pluginId,2,elem.get('title'),{'title': elem.get('title'), 'iconImage': elem.get('image'), 'linkDemand': elem.get('linkDemand'), 'page': str(0)})
    xbmcWrapper.endOfContent(pluginId)    
        
def addTvShowEpisodes(paramDict):
    ''' This methods create the list of shows starting with letter '''  
    # LinkDemand is an URL that passed as a parameter form the command line and had been escaped so need to be recovered
    url = urllib.unquote_plus(paramDict['linkDemand'])         
    episodeList = request.showsEpisodeList(url, int(paramDict['page']))   
    
    for elem in episodeList['list']:
        xbmcWrapper.addVideoItem(pluginId, elem.get('name'), elem.get('h264'), elem.get('image'), elem.get('image_medium'))
    
    # Hanlde the next page indicator
    if int(paramDict['page'])+1 < int(episodeList['pages']):
        xbmcWrapper.addFolder(pluginId,3,'Prossima Pagina',{'title': paramDict['title'], 'linkDemand': paramDict['linkDemand'], 'page': str(int(paramDict['page'])+1)})
    
    xbmcWrapper.endOfContent(pluginId)    

def getParams():
    ''' Utility method that returns all params passed to xbmc as a dictionary'''
    print "ARGUMENTS: "
    print sys.argv
    
    resultDict = {}
    
    if len(sys.argv) > 1 and len(sys.argv[2]) > 1:
        paramList = sys.argv[2][1:].split('&')
        for elem in paramList:
            token = elem.split('=')
            if len(token) == 2:
                resultDict[token[0]] = token[1]
    
    return resultDict
        

paramsDict=getParams()
mode=None
try:
        mode=int(paramsDict['mode'])
except:
        pass
    
loggerMethod("Mode", str(mode))


# Mode = None - First start - List of letters
if mode == None: 
    print "Create groups"
    addLetterIndex()

# Mode = 1 - Letter chosen - List of TV shows starting with defined letter
elif mode == 1: 
    print "Create shows staring with " + paramsDict['letter']
    addTvShowsByLetter(paramsDict)

# Mode = 2 - Tv show chosen - List of episode available for that show      
elif mode == 2: 
    print "Create episode index for: " + paramsDict['title'] + ' page: ' + str(paramsDict['page'])
    addTvShowEpisodes(paramsDict)

# Mode = 3 - Tv show chosen - List of episode available for that show for next pages    
elif mode == 3: 
    print "Create episode index for: " + paramsDict['title'] + ' page: ' + str(paramsDict['page'])
    addTvShowEpisodes(paramsDict)
