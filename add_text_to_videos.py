import cv2
import datetime
cap = cv2.VideoCapture(0-0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 3000)
#cap.set(4, 3000)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        # 'Width: '+str(cap.get(3)) + " Height: " + str(cap.get(4))
        text = "70"
        #datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (400, 450), font,
                            5, (19, 196, 240), 20, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
