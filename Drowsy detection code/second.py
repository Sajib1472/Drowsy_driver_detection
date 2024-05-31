#WEBSITE: easycode.com
#Generated with EasyPython
######################
import numpy as np
import cv2 # pip install opencv-python
import urllib.request

frame = None
key = None

######################

print('START')
while True:
    imgResp=urllib.request.urlopen('http://192.168.0.108/capture')
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    cv2.imshow('window',frame)
    key = cv2.waitKey(500)

    if key == (ord('q')):
        break

cv2.destroyAllWindows()
print('END')
