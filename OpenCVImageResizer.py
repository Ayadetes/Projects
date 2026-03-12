import cv2
while True:
    size = input("Enter the new size of the image\n (1: 200, 2: 400 3: 600):")
    if size == "1":
        width, height = 200, 200
        break
    elif size == "2":
        width, height = 400, 400
        break
    elif size == "3":
        width, height = 600, 600
        break
    else:
        print("Invalid Input")
img = cv2.cvtColor(cv2.imread("assets/MarioBG.png"), cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (width, height))
cv2.namedWindow("Image Resizer", cv2.WINDOW_NORMAL)
cv2.imshow("Image Resizer", img)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("Save#1.png", img)
else: 
    print("Image Not Saved")
cv2.destroyAllWindows()