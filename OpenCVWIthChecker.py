import cv2 
import matplotlib.pyplot as plt
image = cv2.imread("assets/MarioBG.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
width = image_rgb.shape[1]
cv2.line(image_rgb, (0, 100), (width, 100), (255, 0, 0), 10)
cv2.putText(image_rgb, f"Width Measurement: {width}px", (width//2 - 100, 90), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 5, cv2.LINE_AA)
plt.imshow(image_rgb)
plt.title(f"Width: {width}")
plt.show()