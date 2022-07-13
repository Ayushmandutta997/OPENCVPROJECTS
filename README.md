# Project-1 [Ball Detector and Canny Edge Detector]

![Output](https://user-images.githubusercontent.com/82443192/178718583-3757c79d-d131-41c9-a7c6-da0dc1f2e939.JPG)
![CannyEdge](https://user-images.githubusercontent.com/82443192/178718625-e3d15fea-6903-4972-a4a5-ceb47aaf8c67.JPG)

Found the lower and upper Hue Saturation Value thresholds of ball to be detected using create_trackbar and tuning get_trackbar functions of OpenCV.
Then using the findcontour function detected the contour of the ball. After finding the coordinates of rectangle engulfing the contour drew the rectangle
and printed the colour. Used the Canny function to detected edges in the video in a particular threshold.

# Project-2 [Colour Detector]

![Picture](https://user-images.githubusercontent.com/82443192/178720740-f05c1318-b1c3-4440-83b7-f2a6181a252f.JPG)
![colour](https://user-images.githubusercontent.com/82443192/178720781-9dda77df-b61a-488d-97f1-0ab69af24026.JPG)

The colours.csv file contains the name of different colours and their r,g,b values. So first of all whenever the mouse button is clicked at some part of flowers.jpg
the decolour functions stores the B,G,R value in b,g,r variables then using this values I found the colour name whose r,g,b values have least difference as compared 
to that of r,g,b values of the clicked point and printed that colour name on a blank window.

# Project-3 [Invisible Man]

https://user-images.githubusercontent.com/82443192/178725920-a5e504ed-ca77-4055-8946-7632a1206824.mp4

Created a mask variable which stores the lower and upper hsv thresholds of the cloak (I have used tshirt).A back variable stores the background without anyone else in the frame before the actual detection starts. When the video runs, the frame variable stores the current frames from video and does bitwise and with the mask variable giving us the portion of frame that is only common with mask (i.e where the cloak is present), this value is stored in res1. Another variable res2 stores bitwise and of back variable and inverse of mask variable giving us the fake background as seen in video. Final ouput is sum of res1 and res2. Thus the person in the frame is not detected as res1 only contains part common with the tshirt.

# Project-4 [Object Detector]

https://user-images.githubusercontent.com/82443192/178738822-25945307-b072-4712-a3b5-742f7b06edfc.mp4

Used You-Only-Look-Once (YOLO) pretrained model to detect objects on live video feed. Learned about Convolutional Neural Networks (CNN) and working of YOLO algorithm.


