import cv2
import math

img = cv2.imread('ex.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, math.pi/180, 200)

angle = lines[0][0][1] * 180 / math.pi

rows, cols, _ = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))
rotacao = cv2.rotate(rotated, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('rotated.jpeg', rotacao)
