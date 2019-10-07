import cv2
cv2.namedWindow("Resize Preview")
cap = cv2.VideoCapture('tree.avi')
#cap = cv2.VideoCapture(0-0)
print(cap.isOpened())

if cap.isOpened():
    ret, frame = cap.read()
    print("Original Dimensions: ", frame.shape)
else:
    print(ret)

while (cap.isOpened()):
    ret, frame = cap.read()
    print(ret)
    print(frame)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
