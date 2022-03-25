import requests, json
from bs4 import BeautifulSoup
from tools import get

class MagnetRetrieval():

    def __init__(self):
        self.headers = {
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45",
              "Accept-Encoding": "*"
        }

    def passLink(self):
        with open('torrents.json', 'r') as f:
            torrents = json.load(f)
            for link in torrents['4K']:
                if link.startswith("https://1337xx.to"):
                    data = self.get1337xMagnet(link)
                    #print(data)
                    return data
                # if link.startswith("https://www1.thepiratebay3.to"):
                #     data = self.getPirateBayMagnet(link)
                #     return data
                # if link.startswith("https://torrentgalaxy.to"):
                #     data = self.getTorrentGalaxyMagnet(link)
                #     return data
        return None

    # def retrieveURLs(self, name):
    #     one337xx_links = []
    #     piratebay_links = []
    #     torrentgalaxy_links = []
    #     with open('torrents.json') as f:
    #         torrents = json.load(f)
    #         for link in torrents['4K']:
    #             if name == "1337xx":
    #                 if link.startswith('https://1337xx.to'):
    #                     one337xx_links.append(link)
    #                     return one337xx_links
    #             if name == "piratebay":
    #                 if link.startswith("https://www1.thepiratebay3.to"):
    #                     piratebay_links.append(link)
    #                     return piratebay_links
    #             if name == "torrentgalaxy":
    #                 if link.startswith("https://torrentgalaxy.to"):
    #                     torrentgalaxy_links.append(link)
    #                     return torrentgalaxy_links

    def get1337xMagnet(self, link):
        # TODO: Optimise this function.
        data = {}
        try:
            source = get(link).text
            soup = BeautifulSoup(source, 'lxml')
            data["magnet"] = soup.select('ul.dropdown-menu > li')[-1].find('a')['href']
            files = []
            for li in soup.select('div.file-content > ul > li'):
                files.append(li.text.replace("\n", ""))
            data["files"] = files
        except Exception as e:
            print(e)
            pass
        return data

    def getPirateBayMagnet(self, link):
        pass

    def getTorrentGalaxyMagnet(self, link):
        pass