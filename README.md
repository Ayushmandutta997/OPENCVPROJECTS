# Project-1 Ball Detector

![Output](https://user-images.githubusercontent.com/82443192/178718583-3757c79d-d131-41c9-a7c6-da0dc1f2e939.JPG)

![CannyEdge](https://user-images.githubusercontent.com/82443192/178718625-e3d15fea-6903-4972-a4a5-ceb47aaf8c67.JPG)

Found the lower and upper Hue Saturation Value thresholds of ball to be detected using create_trackbar and tuning get_trackbar functions of OpenCV.
Then using the findcontour function detected the contour of the ball. After finding the coordinates of rectangle engulfing the contour drew the rectangle
and printed the colour. Used the Canny function to detected edges in the video in a particular threshold.


