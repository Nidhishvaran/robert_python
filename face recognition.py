import cv2

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

detector = cv2.CascadeClassifier('C:/Users/hp/Pictures/kali linux/python application demo/haarcascade_frontaface_default.xml')
faceid = input('enter a numeric user ID here: ')
print('taking samples look at camera...........')
count = 0

while True:
    ret,img =cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)
    
    for (x,y,w,h) in faces:
                        
                    cv2.rectangle(img, (x,y), (x+w,y+h)< (255,0,0), 2)
                    count+= 1
                    
                    cv2.imwrite('C:/Users/hp/Pictures/kali linux/python application demo/face recognition'+ str(faceid)+ "." +str(count) + "jpg",converted_image[y:y+h,x:x+w])
                    
                    cv2.imshow('image',img)
    k = cv2.waitKey(100) & 0xff 
    if k== 27:
        break
    elif count>=10:
        break
print('samples taking now closing the program')