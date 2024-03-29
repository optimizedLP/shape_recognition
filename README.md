# shape_recognition

## Description
This script performs the following steps:

1. Loads an image containing various shapes.
2. Converts the image to grayscale.
3. Thresholds the grayscale image to create a binary image.
4. Finds contours in the binary image.
5. Approximates the contours to simplify them.
6. Classifies the contours as squares, rectangles, triangles, or circles based on the number of vertices.
7. Draws contours around the detected shapes and displays the count of each shape.

## Dependencies
Python 3.x
OpenCV (cv2)
