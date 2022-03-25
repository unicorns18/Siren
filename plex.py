from plexapi.server import PlexServer
from siren_logging import siren_logging
from difflib import SequenceMatcher
import jellyfish
import re

logging = siren_logging()

baseurl = 'http://127.0.0.1:32400'
token = 'QZ7rm9ZoZzRWtUDJASFz'

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

class PPlex:

    def __init__(self):
        self.plex = PlexServer(baseurl, token)

    def check_if_in_library(self, query):
        """
        Check if the movie is in the library.

        @params
        query: The movie title.
        """

        movies = self.plex.library.section('Siren Movies')
        
        for i in movies.search(query):
            jellyfish_similarity_5 = jellyfish.match_rating_comparison(i.title, query)
            while jellyfish_similarity_5 != True:
                logging.plex_log("Movie not found in library!", "info")
                plex.library.section('Siren Movies').update()
                return False
            logging.plex_log("Movie found in library!", "info")
            return True

    def check_if_in_library_alt(self, query):
        """
        Check if the movie is in the library.

        @params
        query: The movie title.
        """
        found = False

        while found != True:
            movies = self.plex.library.section('Siren Movies')
            for i in movies.search(query):
                jellyfish_similarity_5 = jellyfish.match_rating_comparison(i.title, query)
                while jellyfish_similarity_5 != True:
                    logging.plex_log("Movie not found in library! (Alternative used.)", "info")
                    plex.library.section('Siren Movies').update()
                    return False
                logging.plex_log("Movie found in library! (Alternative used.)", "info")
                found = True
                return True