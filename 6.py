from urllib import request
import zipfile
import re

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
dest_path = './channel.zip'
request.urlretrieve(url, dest_path)


files = {}
with zipfile.ZipFile(dest_path) as fzip:
    for name in fzip.namelist():
        with fzip.open(name) as f:
            files[name] = f.read().decode('utf-8')
nothing = "90052"
while True:
    f = nothing + '.txt'
    print(fzip.getinfo(f).comment.decode("utf-8"), end="")
    res = re.search(r"Next nothing is (\d+)", files[f])
    try:
        nothing  = res.group(1)
    except:
        break