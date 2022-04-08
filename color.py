import cv2
import numpy as np

#https://github.com/offsouza/color-segmentation.git
colorBlindness = 'red'
#To get the lower range go to https://alloyui.com/examples/color-picker/hsv.html
#To get the H value divide by 2 from the value on the website the S and V values stay as is


#prompts()
def red(blur, image):
    red_lower = np.array([0, 95, 100])
    red_upper = np.array([25, 255, 255])
    mask = cv2.inRange(blur, red_lower, red_upper)
    res = masking(blur, red_lower, red_upper, image)
    res[mask > 0] = [144,139,246] #pink color
    return res

def green(blur, image):
    green_lower = np.array([20, 0, 0])
    green_upper = np.array([75, 255, 255])

    red_lower = np.array([0, 50, 100])
    red_upper = np.array([20, 255, 255])

    green_mask = cv2.inRange(blur, green_lower,green_upper)
    red_mask = cv2.inRange(blur, red_lower, red_upper)

    result_green = masking(blur, green_lower, green_upper, image)
    result_red = masking(blur, red_lower, red_upper, image)

    result_green[green_mask > 0] = [67, 146, 112]
    result_red[red_mask > 0] = [187, 139, 255]

    return result_green, result_red


def masking(blur, lower, upper, image):
    mask = cv2.inRange(blur, lower, upper)
    res = cv2.bitwise_and(image, image, mask=mask)
    return res


def colorDetection(colorBlindness, file):
    image = cv2.imread("uploads/" + file)


    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




    blur = cv2.medianBlur(hsv, 11)

    if(colorBlindness == 'red'):
    #establishes color bounds for red
        result = red(blur, image)
       # result2 = green(blur, image)

        #need something here to adjust green
    elif(colorBlindness == 'green'):
        result_red, result_green = green(blur, image)

    #mask_inv = cv2.bitwise_not(result)
   # background = cv2.bitwise_and(gray, gray, mask=mask_inv)

    # Opacity settings
    alpha = .6
    beta = (1.0 - alpha)

   # result = cv2.bitwise_or(result_green, result_red)


    #changes opacity of the picture
   # filteredImage = cv2.addWeighted(result, alpha, image, beta, 0.0)

    #target = cv2.bitwise_and(image, image, mask=result)

    cv2.imwrite('photo.png', image)




