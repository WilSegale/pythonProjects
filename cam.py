from  cv2 import cv2
 
baseIm = image.new('RGBA', (370, 298), 'black')
for x in range(5, baseIm.width-5):
    for y in range(5, baseIm.height-5):
        baseIm.putpixel((x,y), (239, 222, 205))
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False