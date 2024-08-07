import requests 
import xml.etree.ElementTree as ET 

RSS_FEED_URL = "http://feeds.bbci.co.uk/news/rss.xml"

def loadRSS():
    res = requests.get(RSS_FEED_URL)
    return res.content

def parseXML(rss):
    if rss is None:
        return []
    try:
        root = ET.fromstring(rss)
    except ET.ParseError as e:
        print(f"Error parsing XML : {e}")
        return []

    newsitems = []

    for item in root.findall(".//item"):
        news = {}
        for child in item:
            if child.tag == "{http://search.yahoo.com/mrss/}content":
                news['media'] = child.attrib.get('url')
            else:
                print(f"Tag = {child.tag}, Text = {child.text}")
                if child.text:
                    news[child.tag] = child.text.encode('utf-8')
                else:
                    news[child.tag] = b''
        newsitems.append(news)
    return newsitems

def topStories():
    rss = loadRSS()
    newsitems = parseXML(rss)
    return newsitems