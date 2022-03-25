from subprocess import Popen, PIPE
from siren_logging import siren_logging
import subprocess, sys, requests

logging = siren_logging()

try:
    # Python 3
    from urllib.parse import (
        urljoin
    )
except ImportError:
    # Fall back on future.backports
    from future.backports.urllib.parse import (
        urljoin
    )

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45", "Accept-Encoding": "*"}

PYTHON3 = True if sys.version_info.major == 3 else False

def copy2clip(text):
    """
    Copy text to clipboard.
    
    @params
    text: The text to copy to the clipboard.
    """
    
    platform = sys.platform

    if platform == "win32":
        try:
            command = "echo " + text.strip() + "|clip"
            return subprocess.check_call(command, shell=True)
        except Exception as e:
            logging.general_log("Could not copy to clipboard: " + str(e), "error")
    elif platform.startswith("linux") or platform == "darwin":
        try:
            command = "pbcopy" if platform == "darwin" else ["xsel", "-pi"]
            kwargs = {"stdin": PIPE, "text": True} if PYTHON3 else {"stdin": PIPE}
            p = Popen(command, **kwargs)
            p.communicate(input=str(text))
        except Exception as e:
            logging.general_log("Could not copy to clipboard: " + str(e), "error")

def get(url):
    """
    Send a GET request to the given url.

    @params
    url: The url to send the request to.
    """
    return requests.get(url, headers=headers)