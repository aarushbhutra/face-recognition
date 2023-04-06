import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\aarus\Downloads\xmlClassifiers\haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(r'C:\Users\aarus\Downloads\xmlClassifiers\haarcascade_eye.xml')  

cap = cv2.VideoCapture(0)

prev_center = None

while True:  
    ret, img = cap.read()  
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray_img, 1.25, 4) 

    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        rec_gray = gray_img[y:y+h, x:x+w]
        rec_color = img[y:y+h, x:x+w]
  
        eyes = eye_cascade.detectMultiScale(rec_gray)  
  
        for (ex, ey, ew, eh) in eyes: 
            cv2.rectangle(rec_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

        # Determine the direction of movement
        center = (x + w // 2, y + h // 2)
        if prev_center is not None:
            dx = center[0] - prev_center[0]
            dy = center[1] - prev_center[1]
            
            if abs(dx) > 10 or abs(dy) > 10:
                direction = ""
                if dx > 10:
                    direction += "Right"
                elif dx < -10:
                    direction += "Left"
                if dy > 10:
                    direction += " Down"
                elif dy < -10:
                    direction += " Up"
                
                print("Direction:", direction)

        prev_center = center

    cv2.imshow('Face Recognition', img) 
  
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
cap.release() 
cv2.destroyAllWindows()
