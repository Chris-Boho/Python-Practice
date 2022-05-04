import cv2

img = cv2.imread('assets/piano.jpg', -1)

# imread('image.jpg', )
# the second param for imread will take:
# -1 , cv2.IMREAD_COLOR
#  0 , cv2.IMREAD_GRAYSCALE
#  1 , cv2.IMREAD_UNCHANGED

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
