import re
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
res = urllib.request.urlopen(url)
content = res.read().decode('utf-8')

match_strings = re.findall(r'<!--(.+?)-->', content, re.S)
char_list = re.findall(r'[a-zA-Z]', match_strings[1])
print(char_list)