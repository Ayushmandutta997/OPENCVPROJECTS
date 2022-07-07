import cv2 as cv
import numpy as np
import pandas as pd
clicked=False
b=g=r=X=Y=0
blank=np.zeros((500,500),dtype=np.uint8)
img=cv.imread(r'C:\Users\91766\Downloads\flowers.jpg')
img=cv.resize(img,(700,500))
cv.imshow('flowers',img)
ind=['colour','colourname','hex','R','G','B']
csv=pd.read_csv(r'C:\Users\91766\Desktop\projects\colours.csv',names=ind,header=None)
def decolor(event,x,y,flags,param):
    global blank
    blank=np.zeros((500,500),dtype=np.uint8)
    if event==cv.EVENT_LBUTTONDOWN:
        global clicked,X,Y,b,g,r
        clicked=True
        X=x
        Y=y
        b,g,r=img[x,y]
        b=int(b)
        g=int(g)
        r=int(r)
def colna(B,G,R):
    min=1000
    for i in range(len(csv)):
        d=abs(R-int(csv.loc[i,'R']))+abs(G-int(csv.loc[i,'G']))+abs(B-int(csv.loc[i,'B']))
        if(d<=min):
            min=d
            cn=csv.loc[i,'colourname']
    return cn
cv.setMouseCallback('flowers',decolor)
while 1:
    cv.imshow('flowers',img)
    cv.imshow('colour',blank)
    if clicked==True:
        cv.putText(blank,colna(b,g,r),(50,50),cv.FONT_HERSHEY_COMPLEX,1,(b,g,r),1,cv.LINE_AA)   
    if cv.waitKey(10)&0xFF==ord('q'):
        break

cv.destroyAllWindows()