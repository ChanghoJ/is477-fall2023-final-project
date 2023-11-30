# 1 hash key and file name
HASH_WINE = "2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab"
FILE_WINE = "data/wine.zip"

# 2 downloads and verifies both datasets
import requests
import os
import hashlib
import zipfile

# make sure directory exist
if not os.path.exists('data'):
    os.makedirs('data', exist_ok=True)

##import zipfile

# UCI Wine dataset
url01 = 'https://archive.ics.uci.edu/static/public/109/wine.zip'

# get response from the download
try:
    response01 = requests.get(url01)
except:
    print("failed to connect wine.zip. check url")

# download if data/wine.zip not exist
if os.path.exists(FILE_WINE) is False:
    try:
        with open(FILE_WINE, mode='wb') as f:
            f.write(response01.content)
    except:
        print("failed to download wine.zip")

# get hash from the data
with open(FILE_WINE, 'rb') as f:
    data01 = f.read()
    sha256hash01 = hashlib.sha256(data01).hexdigest()

# comparing hash and send error messege
if HASH_WINE != sha256hash01:
    print("wine.zip hash does not match expected hash, not matching with original file") 
else:
    print("wine.zip hash matches expected hash")

# unzip dataset
with zipfile.ZipFile(FILE_WINE, mode="r") as archive:
    try:
        archive.extractall(path="data/")
        print("Unzip of wine.zip complete")
    except:
        print("Unzip failed. Check dataset downloaded correctly")