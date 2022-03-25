from colorama import Fore, Style

class siren_logging:

    def __init__(self):
        self.general_log("Logging engine initialized.", "init")
        self.plex_log("Logging engine initialized.", "init")
        self.alldebrid_log("Logging engine initialized.", "init")
        self.torrentengine_log("Logging engine initialized.", "init")
        return
    
    def general_log(self, message, level):
        """
        General logging function.

        @params
        message: The message to be logged.
        level: The level of the message. (Severity.)
        """
        if message == "":
            raise ValueError("Empty message passed to general_log()")
        if level not in ["info", "warning", "error", "init", "report"]:
            raise ValueError("Invalid level passed to general_log()")
        if level == "report":
            print(Fore.GREEN + "[REPORT] General: " + Fore.RED + message + ". Please report this message to the developer" + Style.RESET_ALL)
        if level == "init":
            print(Fore.GREEN + "[INIT] General: " + Fore.WHITE + message + Style.RESET_ALL)
        if level == "info":
            print(Fore.GREEN + "[INFO] General: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "warning":
            print(Fore.YELLOW + "[WARNING] General: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "error":
            print(Fore.RED + "[ERROR] General: " + Fore.WHITE + message + Style.RESET_ALL)
        return True

    def plex_log(self, message, level):
        """
        Plex logging function.

        @params
        message: The message to be logged.
        level: The level of the message.
        """
        if message == "":
            raise ValueError("Empty message passed to plex_log()")
        if level not in ["info", "warning", "error", "init", "report"]:
            raise ValueError("Invalid level passed to plex_log()")
        if level == "report":
            print(Fore.GREEN + "[REPORT] Plex: " + Fore.RED + message + ". Please report this message to the developer" + Style.RESET_ALL)
        if level == "init":
            print(Fore.GREEN + "[INIT] Plex: " + Fore.WHITE + message + Style.RESET_ALL)
        if level == "info":
            print(Fore.GREEN + "[INFO] Plex: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "warning":
            print(Fore.YELLOW + "[WARNING] Plex: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "error":
            print(Fore.RED + "[ERROR] Plex: " + Fore.WHITE + message + Style.RESET_ALL)
        return True

    def alldebrid_log(self, message, level):
        """
        AllDebrid logging function.

        @params
        message: The message to be logged.
        level: The level of the message.
        """
        if message == "":
            raise ValueError("Empty message passed to alldebrid_log()")
        if level not in ["info", "warning", "error", "init", "report"]:
            raise ValueError("Invalid level passed to alldebrid_log()")
        if level == "report":
            print(Fore.GREEN + "[REPORT] AllDebrid: " + Fore.RED + message + ". Please report this message to the developer" + Style.RESET_ALL)
        if level == "init":
            print(Fore.GREEN + "[INIT] AllDebrid: " + Fore.WHITE + message + Style.RESET_ALL)
        if level == "info":
            print(Fore.GREEN + "[INFO] AllDebrid: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "warning":
            print(Fore.YELLOW + "[WARNING] AllDebrid: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "error":
            print(Fore.RED + "[ERROR] AllDebrid: " + Fore.WHITE + message + Style.RESET_ALL)
        return True

    def torrentengine_log(self, message, level):
        """
        Torrent Engine logging function.

        @params
        message: The message to be logged.
        level: The level of the message.
        """
        if message == "":
            raise ValueError("Empty message passed to torrentengine_log()")
        if level not in ["info", "warning", "error", "init", "report"]:
            raise ValueError("Invalid level passed to torrentengine_log()")
        if level == "report":
            print(Fore.GREEN + "[REPORT] TorrentEngine: " + Fore.RED + message + ". Please report this message to the developer" + Style.RESET_ALL)
        if level == "init":
            print(Fore.GREEN + "[INIT] TorrentEngine: " + Fore.WHITE + message + Style.RESET_ALL)
        if level == "info":
            print(Fore.GREEN + "[INFO] TorrentEngine: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "warning":
            print(Fore.YELLOW + "[WARNING] TorrentEngine: " + Fore.WHITE + message + Style.RESET_ALL)
        elif level == "error":
            print(Fore.RED + "[ERROR] TorrentEngine: " + Fore.WHITE + message + Style.RESET_ALL)
        return True
