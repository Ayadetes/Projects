import cv2 
import numpy as np
imgexample = cv2.imread("assets/example.jpg")
def apply_filter(image, userinput):
    img = image.copy()
    if userinput.strip(" ").lower() == "redtint":
        img[:,:,1] = img[:,:,0] = 0
    elif userinput.strip(" ").lower() == "greentint":
        img[:,:,0] = img[:,:,2] = 0
    elif userinput.strip(" ").lower() == "bluetint":
        img[:,:,1] = img[:,:,2] = 0
    elif userinput.strip(" ").lower() == "sobel":
        grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(grayed, cv2.CV_64F,1,0,ksize=3)
        sy = cv2.Sobel(grayed, cv2.CV_64F,0,1,ksize=3)
        sob = cv2.bitwise_or(sx.astype('uint8'), sy.astype('uint8'))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif userinput.strip(" ").lower() == "canny":
        grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(grayed,100,200)
        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)
    elif userinput.strip(" ").lower() == "cartoon":
        grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayed = cv2.medianBlur(grayed, 5)
        edges = cv2.adaptiveThreshold(grayed,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        color = cv2.bilateralFilter(image, 9, 300,300)
        img = cv2.bitwise_and(color,color,mask=edges)
    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened:
        print("Camera Error")
        return
    userinput = "original"
    print("Keys =\n r=red tint\n g=green tint\n b=blue tint\n s=sobel filter\n c=canny filter\n a=cartoon filter\n q=quit")
    while True:
        ret, frame=cap.read()
        if not ret:
            print("can't recieve frame")
            break
        out = apply_filter(frame, userinput)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(0)
        if key == ord('r'):
            userinput = "redtint"
        elif key == ord('g'):
            userinput = "greentint"
        elif key == ord('b'):
            userinput = "bluetint"
        elif key == ord('s'):
            userinput = "sobel"
        elif key == ord('c'):
            userinput = "canny"
        elif key == ord('a'):
            userinput = "cartoon"
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
        

    
