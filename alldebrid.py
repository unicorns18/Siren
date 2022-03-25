import requests
import tools
from time import sleep
import time
from urllib3 import Retry
import sqlite3

AD_API_KEY = "IFnHU9lFDoLMDxpJjEsP"
AD_AGENT_NAME = "un1c0rns"

class AllDebrid:
    base_url = "https://api.alldebrid.com/v4/"

    http_codes = {
        200: "Success",
        400: "Bad Request, The request was unacceptable, often due to missing a required parameter",
        401: "Unauthorized",
        404: "Not Found, Api endpoint doesn't exist",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        524: "Internal Server Error"
    }

    def __init__(self):
        """
        Initialize the AllDebrid object
        """
        self.apikey = AD_API_KEY
        self.agent_name = AD_AGENT_NAME
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[429, 500, 502, 503, 504])
        self.session.mount('https://', requests.adapters.HTTPAdapter(max_retries=retries, pool_maxsize=100))

    def __del__(self):
        """
        Close the session
        """
        self.session.close()

    def get(self, url, **params):
        """
        Send a GET request

        @params
        url: The url to request
        params: The parameters to send with the request
        """
        params.update({ 
            "agent": self.agent_name,
            "apikey": self.apikey if not params.pop("reauth", None) else None 
        })

        return self.session.get(tools.urljoin(self.base_url, url), params=params)
    
    def get_json(self, url, **params):
        """
        Same as get() but returns the json response

        @params
        url: The url to request
        params: The parameters to send with the request
        """
        return self._extract_data(self.get(url, **params).json())
    
    def post(self, url, post_data=None, **params):
        """
        Send a POST request

        @params
        url: The url to request
        post_data: The data to send with the request
        params: The parameters to send with the request
        """

        params.update({
            "agent": self.agent_name,
            "apikey": self.apikey
        })

        return self.session.post(tools.urljoin(self.base_url, url), data=post_data, params=params)

    def post_json(self, url, post_data=None, **params):
        """
        Same as post() but returns the json response

        @params
        url: The url to request
        post_data: The data to send with the request
        params: The parameters to send with the request
        """
        return self._extract_data(self.post(url, post_data, **params).json())

    def _extract_data(self, response):
        """
        Extract the data from the response
        
        @params
        response: The response to extract the data from
        """
        if "data" in response:
            return response["data"]
        else:
            return response
    
    def auth(self):
        """
        Authenticate with AllDebrid
        """
        response = self.get_json("pin/get", reauth=True)
        expiry = pin_ttl = int(response["expires_in"])
        auth_complete = True
        tools.copy2clip(response["pin"])
        sleep(5)
        while (not auth_complete and not expiry <= 0):
            auth_complete, expiry = self.poll_auth(check=response["check"], pin=response["pin"])
            progress_percent = 100 - int((float(pin_ttl - expiry) / pin_ttl) * 100)
            print("Authentication progress: %s%%" % progress_percent)
            sleep(1)
        self.store_user_info()

        if auth_complete:
            print("Authentication successful!")
            return True
        else:
            return

    def poll_auth(self, **params):
        """
        Poll the authentication status

        @params
        params: The parameters to send with the request
        """
        response = self.get_json("pin/check", **params)
        if response["activated"]:
            self.apikey = response["apikey"]
            return True, 0
        return False, int(response["expires_in"])
    
    def get_user_info(self):
        """
        Get the user information
        """
        return self._extract_data(self.get_json("user")).get("user", {})

    def store_user_info(self):
        """
        Store the user information
        """
        user_information = self.get_user_info()

        # TODO: Store user information in database or local file for security

        return
    
    def check_hash(self, hash_list):
        """
        Check if a magnet is available instantly.

        @params
        hash_list: Magnets URI or hash you want to check. Can be one or many links.
        """
        return self.post_json("magnet/instant", {"magnets[]": hash_list})

    def upload_magnet(self, magnet_hash):
        """
        Upload a magnet to AllDebrid

        @params
        magnet_hash: Magnet URI or hash to upload
        """
        return self.get_json("magnet/upload", magnet=magnet_hash)

    def update_relevant_hosters(self):

        return self.get_json("hosts")

    def get_hosters(self, hosters):
        host_list = self.update_relevant_hosters()

        if host_list is not None:
            hosters["premium"]["all_debrid"] = [
                (d, d.split(".")[0])
                for l in host_list["hosts"].values()
                if "status" in l and l["status"]
                for d in l["domains"]
            ]
        else:
            hosters["premium"]["all_debrid"] = []

    def resolve_hoster(self, url):
        resolve = self.get_json("link/unlock", link=url)
        return resolve["link"]

    def magnet_status(self, magnet_id):
        """
        Get the status of a magnet

        @params
        magnet_id: ID given to you by AllDebrid when you upload the magnet.
        """
        return self.get_json("magnet/status", id=magnet_id) if magnet_id else self.get_json("magnet/status")
    
    def saved_magnets(self):
        """
        Get the magnets you have saved
        """
        return self.get_json("magnet/status")['magnets']

    def delete_magnet(self, magnet_id):
        """
        Delete a magnet by magnet ID (given by AllDebrid)

        @params
        magnet_id: ID given to you by AllDebrid when you upload the magnet.
        """
        return self.get_json("magnet/delete", id=magnet_id)

    def saved_links(self):
        """
        Get links the user saved.
        """
        return self.get_json("user/links")

    def check_magnet_status(self):
        """
        Check the status of all magnets you have saved
        """
        magnet_id = self.saved_magnets()[0]['id']
        status = self.magnet_status(magnet_id)
        print(type(status['magnets']['status']))
        return bool(status['magnets']['status'] if status['magnets']['status'] == "Ready" else False)
    
    def get_account_status(self):
        """
        Get the account status (premium, subscribed, trial, unknown)
        """
        user_info = self.get_user_info()

        if not isinstance(user_info, dict):
            raise ValueError("Unknown. get_account_status() returned %s" % user_info)

        premium = user_info.get("isPremium")
        premium_until = user_info.get("premiumUntil", 0)
        subscribed = user_info.get("isSubcribed")
        trial = user_info.get("isTrial")

        if premium and premium_until > time.time():
            return "premium"
        elif subscribed:
            return "subscribed"
        elif trial:
            return "trial"
        else:
            return "unknown"