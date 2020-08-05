'''import sys
from PIL import Image
import PIL

im1=Image.open('./public/uploads/'+sys.argv[1])
im1.save('public/pyimages/py'+sys.argv[1])
print('py'+sys.argv[1])

'''

import os

load_folder='public/uploads'
up_img_folder = os.listdir('public/uploads')
py_img_folder = os.listdir('public/pyimages')
if(py_img_folder):
    for name in py_img_folder:
        os.remove('public/pyimages/'+name)
if(up_img_folder):
    for name in up_img_folder:
        if(name!=sys.argv[1]):
            os.remove('public/uploads/'+name)