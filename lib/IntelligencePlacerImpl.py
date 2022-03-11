import os.path
# import matplotlib.pyplot as plt
import cv2
import random


class IntelligencePlacerImpl:

    __paper_min = 200
    __paper_max = 255

    def __init__(self):
        self.__last_error_message = ""

    def find_objects(self, path):
        image = self.load_image(path)
        if image is None:
            return None
        contours = self.find_contours(image)
        if contours is None:
            return None
        image_with_contours = image.copy()
        for contour in contours:
            color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            image_with_contours = cv2.drawContours(image_with_contours, contour, -1, color, 5)

        return False, image_with_contours

    def load_image(self, path):
        if not os.path.exists(path):
            self.__last_error_message = "Incorrect path: %s" % path
            return None

        if not os.path.isfile(path):
            self.__last_error_message = "Not a file: %s" % path
            return None

        full_path = os.path.abspath(path)
        image = cv2.imread(full_path)
        if image is None:
            self.__last_error_message = "Not an image: %s" % full_path
            return None
        return image

    def find_contours(self, image):
        image_copy = image.copy()
        image_copy = cv2.GaussianBlur(image_copy, (3, 3), 0)
        image_copy = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)
        t, image_copy = cv2.threshold(image_copy, 150, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(image_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        new_contours = list()
        for contour in contours:
            moment = cv2.moments(contour)
            if moment['m00'] <= 1e-5:
                continue
            cx = moment['m10']/moment['m00']
            cy = moment['m01']/moment['m00']
            if cy < image.shape[1] / 2:
                new_contours.append(contour)
        if len(new_contours) < 2:
            self.__last_error_message = "error to find contours"
            return None
        new_contours = sorted(new_contours,  key=lambda cont: cv2.arcLength(cont, True))
        return [new_contours[-1], new_contours[-2]]


    def get_last_err_message(self):
        return self.__last_error_message
