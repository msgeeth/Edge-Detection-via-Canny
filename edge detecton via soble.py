import cv2


#get hardware acceleration if it is on the system 
if cv2.ocl.useOpenCL():
    print("hardware acceleration enabled")
else:
    print("hardware acceleration not enabled ")

#read the image 
img = cv2.imread(r'C:\Users\Lenovo\Desktop\man3.jpeg')

cv2.imshow('orginal image',img) #showing the orignal image 
cv2.waitKey(0)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(3,3),0)

soblex = cv2.Sobel(src = img_blur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
sobley = cv2.Sobel(src = img_blur,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5)
soblexy = cv2.Sobel(src = img_blur,ddepth=cv2.CV_64F,dx=1,dy=1,ksize=5)

cv2.imshow('Sobel X',soblex)
cv2.waitKey(0)
cv2.imshow('Sobel Y',sobley)
cv2.waitKey(0)
cv2.imshow('Soble x and y ',soblexy)
cv2.waitKey(0)

#canny edge detection 
edges = cv2.Canny(image=img_blur,threshold1=100,threshold2=200)
#display the detected image 
cv2.imshow('canny edge detection',edges)
cv2.waitKey(0)

cv2.destroyAllWindows()