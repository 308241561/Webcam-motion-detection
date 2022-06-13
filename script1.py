import cv2

img = cv2.imread("/Users/xingguohuang/Documents/app2/galaxy.jpg",0)

print((img).shape)
print(img.ndim)


resizedImage = cv2.resize(img,((int)(img.shape[1]/2),(int)(img.shape[0]/2)))
cv2.imshow("G", resizedImage)
cv2.imwrite("/Users/xingguohuang/Documents/app2/Galaxy_resized.jpg", resizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()