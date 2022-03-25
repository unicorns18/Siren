class Errors:

    # 100-199 for plex
    # 200 - 299 for alldebrid
    # 300 - 399 for torrent engine
    # 400 - 499 for client
    # 900 - 999 reserved

    # Individual error variables for each module for cleanliness
    plex_error_codes = {
        # TODO: Add more error codes
    }

    alldebrid_error_codes = {
        # TODO: Fix the eror codes for alldebrid
        "GENERIC": "An error occured.",
        "404": "Endpoint doesn't exist.",
        "AUTH_MISSING_AGENT": "You must send a meaningful agent parameter. See API docs."
        "AUTH_BAD_AGENT": "Bad agent.",
        "AUTH_MISSING_APIKEY": "The auth apikey was not sent.",
        "AUTH_BAD_APIKEY": "Bad API key. (Invalid API key.)",
        "AUTH_BLOCKED": "This apikey is geo-blocked or ip-blocked.",
        "AUTH_USER_BANNED": "This user is banned.",
        "LINK_IS_MISSING": "No link was sent.",
        "LINK_HOST_NOT_SUPPORTED": "This host is not supported.",
        "LINK_DOWN": "This link is not available on the file hoster website.",
        "LINK_PASS_PROTECTED": "This link is password protected.",
        "LINK_NOT_AVAILABLE": "This link is not available.",
        "LINK_TOO_MANY_DOWNLOADS": "Too many concurrent downloads for this host.",
        "LINK_HOST_FULL": "All servers are full for this host, please try again later.",
        "LINK_HOST_LIMIT_REACHED": "You have reached the limit for this host.",
        "LINK_ERROR": "Could not unlock this link.",
        "REDIRECTOR_NOT_SUPPORTED": "This redirector is not supported.",
        "REDIRECTOR_ERROR": "Could not extract links",
        "STREAM_INVALID_GEN_ID": "Invalid generation ID.",
        "STREAM_INVALID_STREAM_ID": "Invalid stream ID.",
        "DELAYED_INVALID_ID": "This delayed link is invalid.",
        "FREE_TRIAL_LIMIT_REACHED": "You have reached the free trial limit (7 days // 25GB downloaded or host uneligible for free trial)",
        "MUST_BE_PREMIUM": "You must be premium to process this link.",
        "MAGNET_INVALID_ID": "This magnet ID does not exist or is invalid.",
        "MAGNET_INVALID_URI": "This magnet URI is invalid.",
        "MAGNET_INVALID_FILE": "File is not a valid torrent.",
        "MAGNET_FILE_UPLOAD_FAILED": "File upload failed.",
        "MAGNET_NO_URI": "No magnet sent.",
        "MAGNET_PROCESSING": "Magnet is being processed or completed.",
        "MAGNET_TOO_MANY_ACTIVE": "Already have maximum allowed active magnets.",
        "MAGNET_MUST_BE_PREMIUM": "You must be premium to use this feature.",
        "MAGNET_NO_SERVER": "Server are not allowed to use this feature. Visit https://alldebrid.com/vpn if you're using a VPN.",
        "MAGNET_TOO_LARGE": :"Magnet files are too large. (max 1TB)",
        "PIN_ALREADY_AUTHED": "You already have a valid auth apikey.",
        "PIN_EXPIRED": "The pin has expired.",
        "PIN_INVALID": "The pin is invalid.",
        "USER_LINK_MISSING": "No link provided.",
        "USER_LINK_INVALID": "Can't save those links.",
        "NO_SERVER": "	Server are not allowed to use this feature. Visit https://alldebrid.com/vpn if you're using a VPN.",
        "MISSING_NOTIF_ENDPOINT": "You must provide an endpoint to unsubscribe.",
    }

    torrent_engine_error_codes = {
        # TODO: Add more error codes
    }

    def __init__(self):
        self.plex_error_codes = self.plex_error_codes
        self.alldebrid_error_codes = self.alldebrid_error_codes
        self.torrent_engine_error_codes = self.torrent_engine_error_codes