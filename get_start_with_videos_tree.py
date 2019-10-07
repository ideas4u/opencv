import cv2
cv2.namedWindow("Resize Preview")
cap = cv2.VideoCapture(0-0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#cap = cv2.VideoCapture(0-0)
print(cap.isOpened())

if cap.isOpened():
    ret, frame = cap.read()
    print("Original Dimensions: ", frame.shape)
else:
    print(ret)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        # print(ret)
        # print(frame)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)

        if cv2.waitKey(5000) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
