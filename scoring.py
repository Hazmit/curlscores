import cv2
import pytesseract
import math
import time
from datetime import datetime
import array

#define CV_RGB(r, g, b)

# 
# 0    Orientation and script detection (OSD) only.
# 1    Automatic page segmentation with OSD.
# 2    Automatic page segmentation, but no OSD, or OCR.
# 3    Fully automatic page segmentation, but no OSD. (Default)
# 4    Assume a single column of text of variable sizes.
# 5    Assume a single uniform block of vertically aligned text.
# 6    Assume a single uniform block of text.
# 7    Treat the image as a single text line.
# 8    Treat the image as a single word.
# 9    Treat the image as a single word in a circle.
# 10    Treat the image as a single character.
# 11    Sparse text. Find as much text as possible in no particular order.
# 12    Sparse text with OSD.
# 13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

# x=1600
# y=390
# w=x+470
# h=y+160

# x=1635
# x=2600
# y=410
# w=x+40
# h=y+40

def clean_results(text):
    text = text[0:1]
    if(text == 'i'):
        return " 1 "
    if(len(text) > 2):
        return " - "
    if(text.isnumeric()):
        return text

    return " - "


image = cv2.imread(r"./snapshot.jpg")
display_image = image

# dividing height and width by 2 to get the center of the image
height, width = display_image.shape[:2]
# get the center coordinates of the image to create the 2D rotation matrix
center = (width/2, height/2)
 
# using cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=-4, scale=1)
 
# rotate the image using cv2.warpAffine
# display_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

scores = []

for row in range(2):
    print("")
    print(" Score:", end="")
    for i in range(16):
        x=1635+(i*24)
        y=410+(row*65)
        w=x+40
        h=y+40
        
        start_point = (x, y)
        end_point = (w, h)

        if(i % 2) == 0:
            color = (255, 0, 0)
        else:
            color = (0,255,0)
        
        thickness = 2
        
        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        display_image = cv2.rectangle(image, start_point, end_point, color, thickness)
    
        crop_image = image[y:h, x:w]
    
        #grey_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY) 
        # Apply dilation and erosion to remove some noise    kernel = np.ones((1, 1), np.uint8)    img = cv2.dilate(img, kernel, iterations=1)    img = cv2.erode(img, kernel, iterations=1)
    
        # cv2.imshow("Grey", grey_image)
    
        # h, w, c = crop_image.shape
        # boxes = pytesseract.image_to_boxes(crop_image)
        # for b in boxes.splitlines():
            # b = b.split(' ')
            # display_image = cv2.rectangle(crop_image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
        
        # Adding custom options
        custom_config = r'--oem 3 --psm 10 -l eng'
        text = pytesseract.image_to_string(crop_image, config=custom_config)
        
        clean_text = clean_results(text)
        
        # scores[row][i] = clean_text
        print(clean_text, end=" ")

print("")

cv2.imshow("Original", display_image)
# cv2.imshow("Processed", crop_image)
cv2.waitKey(0)