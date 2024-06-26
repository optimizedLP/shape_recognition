import cv2
from google.colab.patches import cv2_imshow

# Load the image
IMAGE = cv2.imread('shape.png')

# Convert the image to grayscale
GREYSCALE = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image
_, THRESHOLD = cv2.threshold(GREYSCALE, 50, 255, 0)

# Find contours in the thresholded image
CONTOURS, _ = cv2.findContours(THRESHOLD, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Initialize counters for shapes
RECTANGLES = 0
SQUARES = 0
TRIANGLES = 0
CIRCLES = 0

# Loop over contours
for cnt in CONTOURS:
    # Approximate the contour to simplify it
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)

    # Get the number of vertices
    vertices = len(approx)

    # Determine the shape based on the number of vertices
    if vertices == 3:
        TRIANGLES += 1
        cv2.drawContours(IMAGE, [cnt], 0, (255, 0, 0), 3)
    elif vertices == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        ratio = float(w) / h
        if ratio >= 0.9 and ratio <= 1.1:
            SQUARES += 1
            cv2.drawContours(IMAGE, [cnt], 0, (0, 255, 0), 3)
        else:
            RECTANGLES += 1
            cv2.drawContours(IMAGE, [cnt], 0, (0, 255, 255), 3)
    else:
        # Assuming all other contours are circles
        CIRCLES += 1
        cv2.drawContours(IMAGE, [cnt], 0, (0, 0, 255), 3)

# Draw text indicating the number of each shape
cv2.putText(IMAGE, 'Number of SQUARES: ' + str(SQUARES), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
cv2.putText(IMAGE, 'Number of RECTANGLES: ' + str(RECTANGLES), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
cv2.putText(IMAGE, 'Number of TRIANGLES: ' + str(TRIANGLES), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
cv2.putText(IMAGE, 'Number of CIRCLES: ' + str(CIRCLES), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Display the image
cv2_imshow(IMAGE)
cv2.waitKey(0)
cv2.destroyAllWindows()
