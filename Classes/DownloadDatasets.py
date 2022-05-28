import requests
import os
from Classes.InitValues import InitValues as iv

class DownloadDatasets():
    def __init__(self) -> None:
        pass
    
    def downloadDatasets(self) -> None:
        try:
            os.chdir(iv.ROOT_DIR)
            print("Downloading datasets.exe...")
            url = 'https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/win64/datasets.exe'
            req = requests.get(url, allow_redirects=True)
            open('.\\bin\\datasets.exe', 'wb').write(req.content)
        except Exception as e:
            print(f"Datasets download error. {e}")
            pass
