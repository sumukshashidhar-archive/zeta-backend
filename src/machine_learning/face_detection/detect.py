import cv2 as cv
import sys


def detect(input_filename, output_filename):

    """Takes in input and output files and

    Args:
        input_filename (string): path to the input image
        output_filename (string): path to the output

    Returns:
        dict: returns a keyvalue pair with executed? as True
    """


    original_image = cv.imread(input_filename)
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')


    detected_faces = {}


    i = 0
    for face in face_cascade.detectMultiScale(grayscale_image):
        detected_faces["face" + str(i)] = list(face)
        i += 1
    
    detected_faces["executed"] = True

    return detected_faces


if __name__ == "__main__":
    print( detect("faceTest.jpg", "") )
