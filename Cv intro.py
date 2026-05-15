import cv2

#Load image

image = cv2.imread('BATMAN.jpg')

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)


cv2.imshow('Loaded image', image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")