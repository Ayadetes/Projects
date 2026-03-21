import cv2
import matplotlib.pyplot as plt
com = ""
filepath = input("Enter the file path of the image you want to edit:\n")
img = cv2.imread(filepath)
def change(img, command):
    if command == "g":
        img[:,:,0] = 0
        img[:,:,2] = 0
    elif command == "b":
        img[:,:, 1] = 0
        img[:,:,2] = 0
    elif command == "r":
        img[:,:,1] = 0
        img[:,:,0] = 0
    elif command == "a":
        img[:,:,2]= cv2.add(img[:,:,2], 50)
    elif command == "d":
        img[:,:,0]= cv2.add(img[:,:,0], 50) 
    else:
        pass
#



if img is None:
    print("Error: Could not read the image. Please check the file path and try again.")
    exit()
print("Welcome to OpenCV Filter Creator!\ntype in g for a green tint,\nb for a blue tint,\nr for a red tint,\na for a reddish tint,\nd for a default bluish tint,\ns for save,\nq to quit.")
while True:
    img = change(img, com)   
    cv2.imshow("Image Editor", img)
    key = cv2.waitKey(0) and 0xFF
    if key == ord('r'):
        com = 'r'
  
    elif key == ord('g'):
        com = 'g'
       
    elif key == ord('b'):
        com = 'b'
        
    elif key == ord('a'):
        com = 'a'

    elif key == ord('d'):
        com = 'd'

    elif key == ord('s'):
        savepath = input("enter where you wanna save the image")
        cv2.imwrite(savepath, img)
    elif key == ord('q'):
        print("Exiting...")
        exit()
    else: 
        pass
    
cv2.destroyAllWindows()
