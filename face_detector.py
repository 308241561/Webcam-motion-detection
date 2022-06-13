import cv2

# app2/haarcascade_smile.xml

face_cascade = cv2.CascadeClassifier("app2/haarcascade_frontalface_default.xml")

img = cv2.imread("app2/1341631503461_.pic_hd.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.03,  minNeighbors = 20)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

# print(type(faces))
# print(faces)

resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))

cv2.imshow("G", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

