from DontEdit import *
import cv2
def loadingBar(iterations, delay=0.1, width=40):
    for load in range(iterations + 1):
        progress = load / iterations
        bar_length = int(progress * width)
        bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)
        percentage = int(progress * 100)
        
        print(f'\r[{bar}] {percentage}% ', end='', flush=True)
        time.sleep(delay)

loadingBar(50)

esc = int(27)
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == esc: # exit on ESC
        break
cv2.destroyWindow("preview")
