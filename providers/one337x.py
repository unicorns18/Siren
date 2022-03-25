import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'Z:\\Siren\\')))
from tools import get
from bs4 import BeautifulSoup

def get1337xTorrentData(link):
    """
    Gets the magnet link from the 1337x site.
    """
    data = {}
    try:
        source = get(link).text
        soup = BeautifulSoup(source, "lxml")
        data["magnet"] = soup.select('ul.dropdown-menu > li')[-1].find('a')['href']
        files = []
        for li in soup.select('div.file-content > ul > li'):
            files.append(li.text.replace("\n", ""))
        data["files"] = files
    except Exception as e:
        print(e)
        pass
    return data['magnet']