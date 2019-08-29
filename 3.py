import urllib.request
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
res = urllib.request.urlopen(url)
content = res.read().decode('utf-8')

mathing_strings = re.findall(r'<!--(.+?)-->', content, re.S)
clues = mathing_strings[0]
print(len(clues))
results = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', clues)
print(''.join(results))