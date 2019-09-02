from PIL import Image
import numpy as np

im = Image.open('./cave.jpg')
im = np.array(im)
num_row, num_col, _ = im.shape
row_even_index = np.arange(0, num_row, 2)
col_even_index = np.arange(0, num_col, 2)
im_odd = Image.fromarray(im[row_even_index[:, None], col_even_index])
im_odd.show() 