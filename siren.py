from alldebrid import AllDebrid
from colorama import Fore, Style
from plexapi.server import PlexServer
from plex import PPlex
from torrent_engine import TorrentEngine
from siren_logging import siren_logging
import sys, os, time, json

def run(query):
    """
    Main function.

    @params
    query: The movie title.
    """
    uploaded = False

    # Plex settings
    baseurl = 'http://127.0.0.1:32400'
    token = 'QZ7rm9ZoZzRWtUDJASFz'
    plex = PlexServer(baseurl, token)
    # Initialisations
    torrent_engine = TorrentEngine()
    alldebrid = AllDebrid()
    logging = siren_logging()
    pplex = PPlex()
    # Everything else
    # link = torrent_engine.searchTPB(query)
    # magnet = torrent_engine.getTPBTorrentData(link[0]['link'])
    link = torrent_engine.search1337x(query)
    magnet = torrent_engine.get1337xTorrentData(link[0]['link'])
    logging.torrentengine_log("Magnet: " + str(magnet['magnet']), "info")
    upload = alldebrid.upload_magnet(magnet['magnet'])
    status = alldebrid.check_magnet_status()
    print(status)

    while uploaded != True:
        while status == 'True':
            status = alldebrid.check_magnet_status()
            time.sleep(0.5)
        else:
            uploaded = True

    logging.alldebrid_log("Uploaded and finished all actions.", "info")
    
    checking = pplex.check_if_in_library(query)
    checking1 = pplex.check_if_in_library_alt(query)

    while checking1 == False:
        checking = pplex.check_if_in_library_alt(query)
        logging.plex_log("Checking if in library...", "info")
    logging.plex_log("Movie found in library!", "info")

    while checking != True:
        checking = pplex.check_if_in_library(query)
        logging.plex_log("Checking if the movie exists in Plex...", "info")
        time.sleep(0.5)
    logging.plex_log("Movie found in Plex!", "info")

    time.sleep(0.5)
    for i in range(10):
        plex.library.section('Siren Movies').update()
        time.sleep(0.5)
        
    logging.plex_log("Uploaded and finished.", "info")

def main(query):
    """
    Main function.

    @params
    query: The movie title.
    """
    run(query)

if __name__ == "__main__":
    #main('Despicable Me 3')
    baseurl = 'http://127.0.0.1:32400'
    token = 'QZ7rm9ZoZzRWtUDJASFz'
    plex = PlexServer(baseurl, token)
    print(plex.library.section('Siren Movies').search(resolution="4K"))