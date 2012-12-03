'''
Created on Nov 22, 2012

@author: flavio
'''
import sys,xbmcplugin,xbmcgui

def addFolder(pluginId, mode, name, paramDict):
    
    urlParams = '?mode=' + str(mode)
    
    for dictItem in paramDict.items():
        urlParams += '&' + dictItem[0] + '=' + dictItem[1]
        
    # url = "plugin://" + self._pluginName + "?url=" + item[1]
    #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    url = sys.argv[0] + urlParams
       
    iconImage="DefaultFolder.png"
    if 'iconImage' in paramDict:
        iconImage = paramDict['iconImage']
        
    item=xbmcgui.ListItem(label=name, iconImage=iconImage)
    # Add the item to xbmc
    xbmcplugin.addDirectoryItem(pluginId, url, item, isFolder = True)

def endOfContent(pluginId):
    xbmcplugin.endOfDirectory(pluginId)

def addVideoItem(pluginId,name,url,iconImage,thumbnailImage):
    item=xbmcgui.ListItem(name, iconImage=str(iconImage), thumbnailImage=str(thumbnailImage))
    item.setInfo( type="Video", infoLabels={ "Title": name } )
    xbmcplugin.addDirectoryItem(pluginId, url, item)
