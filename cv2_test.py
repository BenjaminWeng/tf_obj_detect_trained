import cv2

cap = cv2.VideoCapture(0)
cap.open(0)
if cap.isOpened() == False:
    print ("VideoCapture failed")
    

while(cap.isOpened()== True):
  ret, frame = cap.read()
  if ret == False:
    print("Frame is empty")

  cv2.imshow('frame', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
