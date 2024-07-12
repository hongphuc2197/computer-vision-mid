# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:55:11 2024

 
"""
import cv2
import numpy as np

def is_inside(o,i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih

def draw_person(image, person):
    x, y, w, h = person
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,255),2)
    
 
img = cv2.imread("./bt1-image.jpg")

# Define HOG and determine detecting method (we're using default)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Detect mullti scale
found, w = hog.detectMultiScale(img)
 
found_filtered = []

# If detect people, append it to founded array
for ri, r in enumerate(found):
    for qi, q in enumerate(found):
        if ri != qi and is_inside(r,q):
            break
        else:
            found_filtered.append(r)

# Draw rectangles around the person
for person in found_filtered:
    draw_person(img, person)
    

cv2.imshow("Detected people", img)
cv2.waitKey(0)
cv2.destroyAllWindows()