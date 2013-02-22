'''
Created on Nov 22, 2012

@author: flavio
'''
import sys,xbmcplugin,xbmcgui,urllib

def createModeUrl(mode, paramDict):
    urlParams = 'mode=' + str(mode)
    
    for dictItem in paramDict.items():
        param = ''
        try:
            param = urllib.quote_plus(dictItem[1].encode('utf-8', 'ignore'))
        except:
            param = dictItem[1].encode('utf-8', 'ignore')
        urlParams += '&' + dictItem[0] + '=' + param
        
    # url = "plugin://" + self._pluginName + "?url=" + item[1]
    #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    url = sys.argv[0] + '?' + urlParams

    #print "xxxDEBUGxxx createModeUrl ---> Mode:" + str(mode) + " url: " + url

    return url

def addFolder(pluginId, mode, name, paramDict):
    url = createModeUrl(mode,paramDict)

    image="DefaultFolder.png"
    if 'image' in paramDict:
        image = paramDict['image']
        
    item=xbmcgui.ListItem(label=name, iconImage=image)
    # Add the item to xbmc
    xbmcplugin.addDirectoryItem(pluginId, url, item, isFolder = True)

def endOfContent(pluginId):
    xbmcplugin.endOfDirectory(pluginId)

def addVideoItem(pluginId, name, videoUrl, iconImage, thumbnailImage):
    item=xbmcgui.ListItem(name, iconImage=str(iconImage), thumbnailImage=str(thumbnailImage))
    item.setInfo(type="Video", infoLabels={ "Title": name })
    xbmcplugin.addDirectoryItem(pluginId, videoUrl, item)

def addVideoItemWithMode(pluginId, mode, name, videoUrl, iconImage, thumbnailImage):
    url = createModeUrl(mode, {'title':name, 'videoUrl':str(videoUrl), 'iconImage':str(iconImage), 'thumbnailImage':str(thumbnailImage)})
    item = xbmcgui.ListItem(name, iconImage=str(iconImage), thumbnailImage=str(thumbnailImage))
    item.setInfo( type="Video", infoLabels={ "Title": name } )
    xbmcplugin.addDirectoryItem(pluginId, url, item, isFolder = True)
