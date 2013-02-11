'''
Created on Nov 20, 2012
This module handle request to URLs and use file for caching response 

@author: flavio
'''

import http,re,cache,json
from config import base_url

def letterIndexReq():
    ''' Returns the list of initial letter for shows available'''
    resultList = ['0/9']
    for letter in range(ord('A'), ord('Z')+1):
        resultList.append(chr(letter))
    
    return resultList

def showsWithLetterReq(letter):
    ''' Returns the list of shows starting with the letter passed in JSON format'''
    index = cache.getFileCache('showsIndex.txt',56700)  # 56700 means that the cache file must be younger than 12 hours
    if index == None:
        index = http.getPage('http://www.rai.tv/dl/RaiTV/programmi/ricerca/ContentSet-6445de64-d321-476c-a890-ae4ed32c729e-darivedere.html')
        cache.saveFileCache('showsIndex.txt',index)

    indexList = json.loads(index)
    
    filteredList = []
    for elem in indexList:
        if elem['title'].startswith(letter) or (letter[0].isdigit() and elem['title'][0].isdigit()):
            filteredList.append(elem)
    
    return filteredList

def showVideoCategories(showUrl):
    ''' Returns the list of video categories as tuple, with their contentSet, available for the show chosen'''
    global base_url
    
    showPage = http.getPage(base_url + showUrl)
    
    match=re.compile('<li class="Video ">\n(.+?)\n</li>').findall(showPage)
    
    result = []
    for line in match:
        category = re.compile('<a.+?id="(.+?)".+?>(.+?)</a>').findall(line)
        if category:
            result += category

    return result

def showsEpisodeList(contentId,page):
    ''' Returns the list of episodes of the chosen show'''
    
    videoPage = cache.getFileCache(contentId + '-' + str(page) + '.txt', 56700)
    
    if videoPage == None:
        videoPage = http.getPage('http://www.rai.tv/dl/RaiTV/programmi/json/liste/' + contentId + '-json-V-' + str(page) + '.html')
        cache.saveFileCache(contentId + '-' + str(page) + '.txt',videoPage)

    videoJSON = json.loads(videoPage)
    
    return videoJSON
    
    