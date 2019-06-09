import cv2
import numpy as np
import sys
import time
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FPS,10)
qrDecoder = cv2.QRCodeDetector()

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        barcodes = pyzbar.decode(frame)
        if len(barcodes)>0:
            for barcode in barcodes:
                (x,y,w,h) = barcode.rect
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
                
        cv2.imshow("QR Finder", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
