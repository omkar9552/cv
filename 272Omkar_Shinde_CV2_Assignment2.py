import cv2
top_left_corner=[]
bottom_right_corner=[]
image = cv2.imread('jellyfish.jpg')
def drawRectangle(action, x, y, flags, *userdata):
  # Referencing global variables
  global top_left_corner, bottom_right_corner
  # Mark the top left corner when left mouse button is pressed
  if action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
    # When left mouse button is released, mark bottom right corner
  elif action == cv2.EVENT_LBUTTONUP:
    bottom_right_corner = [(x,y)]   
    # Draw the rectangle
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    cv2.imshow("Windo",image)
# cv_imshow(image)
# Make a temporary image, will be useful to clear the drawing
temp = image.copy()
# Create a named window
cv2.namedWindow("Win")
# highgui function called when mouse events occur
cv2.setMouseCallback('Win',drawRectangle)
k=0
while k!=113:
  cv2.imshow("Win", image)
  k = cv2.waitKey(0)
  if (k == 99):
    image= temp.copy()
    cv2.imshow("Win", image)
cv2.destroyAllWindows()


maxScaleUp = 100
scaleFactor = 1
windowName = "Resize Image"
trackbarValue = "Scale"
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)


def scaleImage(*args):
    # Get the scale factor from the trackbar
    scaleFactor = 1+ args[0]/100.0
    # Resize the image
    scaledImage = cv2.resize(image, None, fx=scaleFactor, fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)


# Create trackbar and associate a callback function
cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
# Display the image
cv2.imshow(windowName, image)
c = cv2.waitKey(0)
cv2.destroyAllWindows()
