import requests, random, importlib
from bs4 import BeautifulSoup
from colorama import Fore, Style
from magnet_retrieval import MagnetRetrieval
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'Z:\\Siren\\providers\\')))

torrent_proxies_list = {
  "1337x": ["https://1337xx.to"],
  "ThePirateBay": ["https://www1.thepiratebay3.to"],
  "torrentgalaxy": ["https://torrentgalaxy.to"],
  "Rarbg": []
}

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45",
  "Accept-Encoding": "*"
}

magnet_names = []

def get(url):
    """
    Send a GET request to the given url.

    @params
    url: The url to send the request to.
    """
    return requests.get(url, headers=headers)

def get_quality(magnet_names):
    magnet_names = magnet_names.lower()
    quality = 'SD'
    if ' 4k' in magnet_names:
        quality = '4K'
    if '2160p' in magnet_names:
        quality = '4K'
    if '1080p' in magnet_names:
        quality = '1080p'
    if ' 1080 ' in magnet_names:
        quality = '1080p'
    if ' 720 ' in magnet_names:
        quality = '720p'
    if ' hd ' in magnet_names:
        quality = '720p'
    if '720p' in magnet_names:
        quality = '720p'
    if 'cam' in magnet_names:
        quality = 'CAM'

    return quality

def sortByQuality(magnet_names):
    """
    Sorts the magnet names by quality.
    """
    quality_dict = {}
    for magnet in magnet_names:
        quality = get_quality(magnet)
        if quality in quality_dict:
            quality_dict[quality].append(magnet)
        else:
            quality_dict[quality] = [magnet]
    return quality_dict

def search1337x(query):
    """
    Scrapes the site 1337x.to for the movie and prioritises highest quality and seeds.

    @params
    query: The movie title.
    """
    for proxy in torrent_proxies_list["1337x"]:
        try:
            source = get(f"{proxy}/search/{query}/1").text
            soup = BeautifulSoup(source, "lxml")
            for tr in soup.select("tbody > tr"):
                a = tr.select("td.coll-1 > a")[1]
                magnet_names.append(f"{proxy}{a['href']}")
        except Exception as e:
            print(e)
            continue
    return magnet_names

def searchPirateBay(query):
    """
    Scrapes the site thepiratebay.org for the query.
    """
    for proxy in torrent_proxies_list["ThePirateBay"]:
        try:
            source = get(f"{proxy}/s/page/1/?q={query}&category=0").text
            soup = BeautifulSoup(source, "lxml")
            for tr in soup.select("table#searchResult > tbody > tr:not(:last-child)"):
                a = tr.select("td:nth-of-type(2) > a")[0]
                name = a.text
                magnet_names.append(f"{proxy}{a['href']}")

        except Exception as e:
            print(e)
            continue
    return magnet_names

def searchTorrentGalaxy(query):
    """
    Scrapes the site torrentgalaxy.to for the query.
    """
    for proxy in torrent_proxies_list["torrentgalaxy"]:
        try:
            source = get(f"{proxy}/torrents.php?search={query}#results").text
            soup = BeautifulSoup(source, "lxml")
            for idx, divs in enumerate(soup.find_all('div', class_='tgxtablerow')):
                div = divs.find_all("div")
                magnet_names.append(f"{proxy}{div[4].find('a')['href']}")
        except Exception as e:
            print(e)
            continue
    return magnet_names

def parse_magnets(link):
    """
    Parses the magnets from the link.
    """
    magnets = []
    MagnetRetrieval = MagnetRetrieval()
    if link.startswith("https://1337x.to"):
        magnets = MagnetRetrieval.get1337xMagnet(link)
    elif link.startswith("https://www1.thepiratebay3.to"):
        magnets = MagnetRetrieval.getPirateBayMagnet(link)
    elif link.startswith("https://torrentgalaxy.to"):
        magnets = MagnetRetrieval.getTorrentGalaxyMagnet(link)
    return magnets

query = "Captain Marvel"
searchPirateBay(query)
search1337x(query)
searchTorrentGalaxy(query)
sortByQuality(magnet_names)
with open("torrents.json", "w") as file:
    import json
    file.write(json.dumps(sortByQuality(magnet_names), indent=4))
mr = MagnetRetrieval()
print(Fore.GREEN + "[INFO] TorrentEngine: " +  mr.passLink()['magnet'])