import numpy as np
import cv2
from imutils.video import VideoStream
import imutils
import time
import json


def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

max_cams = 4
window_titles = ['first', 'second', 'third', 'fourth']


# cap = [cv2.VideoCapture(i) for i in names]
print('Initializing Cameras...')
# streams = [VideoStream(src=i).start() for i in range(max_cams)]
streams = []
for i in range(max_cams):
    stream = None
    try:
        stream = VideoStream(src=i).start() 
        time.sleep(3.0)
        if stream.grabbed is True:
            streams.append(stream)

    except: 
        print('Failed to open cam at index: ' + str(i))

    # print(str(i))
    # dump(stream)

print('Cams opened: ' + str(len(streams)))





frames = [None] * len(streams)
gray = [None] * len(streams)
ret = [None] * len(streams)

while True:

    for i,c in enumerate(streams):
        if c is not None:
            frames[i] = c.read()
            if frames[i] is not None:
                frames[i] = imutils.resize(frames[i], width=600)


    for i,f in enumerate(frames):
        if frames[i] is not None:
            cv2.imshow(window_titles[i], frames[i])

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break


for c in streams:
    if c is not None:
        c.release()

cv2.destroyAllWindows()