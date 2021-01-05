import cv2
import numpy as np
import math

def detect_circles_demo(image):
    h = image.shape[1]
    dst = cv2.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(cimage, cv2.HOUGH_GRADIENT, 1, 20, param1=60, param2=40, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    tmp1 = 0
    tmp2 = 0
    cList = [[tmp1,tmp2]]
    for i in circles[0, :]:
        signal = 0
        for each in cList:
            tmp1 = each[0]
            tmp2 = each[1]
            tt = abs(int(i[0])-int(tmp1))+abs(int(i[1])-int(tmp2))
            if tt < 70:
                signal = 1
        if signal == 0:   # judge if two circle is too close
            if i[2] <= 120: # too large circle
                cList.append([i[0],i[1]])
    
    # rerange the dot list
    cList = sorted(cList,key=lambda cList: cList[0])
    del cList[0]    #delete [0,0]
    index = 0
    while index < len(cList):
        a = cList[index]
        b = cList[index+1]
        c = cList[index+2]
        if a[1] > b[1]:
            tmp1 = b
            b = a
            a = tmp1
        if b[1] > c[1]:
            tmp2 = c
            c = b
            b = tmp2
        if a[1] > b[1]:
            tmp1 = b
            b = a
            a = tmp1
        cList[index] = a
        cList[index+1] = b
        cList[index+2] = c
        index += 3

    binList = []
    ret = []
    x = 0
    for i in cList:
        r,g,b = dst[i[1],i[0]]
        if (r*0.299 + g*0.578 + b*0.114 >= 100):
            binList.append(0)
        else:
            binList.append(1)
        if x % 6 == 5:
            ret.append(binList)
            binList = []
        x += 1
    #print(ret)
    return ret

def getDot():
    img = cv2.imread("/home/que/Desktop/AI/mv.jpg")
    return  detect_circles_demo(img)

if __name__ == "__main__":
    getDot()