import urllib.request
import io
from PIL import Image
import numpy as np

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
with urllib.request.urlopen(url) as f:
    im = Image.open(io.BytesIO(f.read()))
    im = np.array(im)

height, width, num_channel = im.shape
h = height // 2
for w in range(width):
    pixel = im[h, w, :]
    if pixel[0] != pixel[1]:
        continue
    if w % 7 == 0:
        print(chr(pixel[0]), end="")
print()
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(c) for c in next_level]))