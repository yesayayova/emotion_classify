import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    res, im = cap.read()

    im2 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im2 = cv2.resize(im2, (48,48))
    a, b = learn(im2)
        
    cv2.putText(im,
                a[0]+' '+str(b[0][0])+' %',
                (30,350),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)
    cv2.putText(im,
                a[1]+' '+str(b[0][1])+' %',
                (30,380),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)
    cv2.putText(im,
                a[2]+' '+str(b[0][2])+' %',
                (30,410),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)
    cv2.putText(im,
                a[3]+' '+str(b[0][3])+' %',
                (30,440),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)
    cv2.putText(im,
                a[4]+' '+str(b[0][4])+' %',
                (30,470),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)
    
    face = haar(im)
    for (x, y, w, h) in face:
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('cam', im)
    
    if cv2.waitKey(10) == 27:
        cv2.imwrite('capture.jpg', im)
        break
    if cv2.waitKey(10) == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()
