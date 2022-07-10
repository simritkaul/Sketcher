import cv2


def sketch_image(photo):
    # Read Image
    img = cv2.imread(photo)

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    img = cv2.bitwise_not(grey_img)
    # invert_img=255-grey_img

    # Blur image
    img = cv2.GaussianBlur(img, (33, 33), 0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(img)
    # invblur_img=255-blur_img

    # Sketch Image
    img = cv2.divide(grey_img, invblur_img, scale=256.0)

    # Save Sketch
    cv2.imwrite('./static/images/sketch.png', img)

    # Display sketch
    # cv2.imshow('sketch image', sketch_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
