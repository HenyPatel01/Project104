import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (15,220), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255))
cv2.putText(img, "Mercury", (120,245), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Venus", (195,260), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Earth", (293,265), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Mars", (388,255), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Jupiter", (540,380), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255))
cv2.putText(img, "Saturn", (770,305), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (970,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1115,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.imshow("The Solar System", img)

cv2.imwrite("Solar_systemwithname.jpg", img)

cv2.waitKey(0)