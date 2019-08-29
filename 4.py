import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
nothing = '8022'

while(True):
    try:
        res = urllib.request.urlopen(url.format(nothing))
    except:
        break
    content = res.read().decode('utf-8')
    print(content)
    nothing = content.split()[-1]
    print('nothing is ', nothing)