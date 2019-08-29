import urllib.request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

with urllib.request.urlopen(url) as f:
    hidden_info = pickle.load(f)
    for line in hidden_info:
        for item in line:
            print(item[0] * int(item[1]), end='')
        print()