import cv2 as cv
import sys
from PIL import Image


def detect(input_filename, output_filename):

    """Takes in input and output files and

    Args:
        input_filename (string): path to the input image
        output_filename (string): path to the output

    Returns:
        dict: returns a keyvalue pair with executed? as True
    """


    #read and detect face from image using cv
    original_image = cv.imread(input_filename)
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')


    detected_faces = {}

    #save and name all faces
    i = 0
    for face in face_cascade.detectMultiScale(grayscale_image):
        detected_faces["face" + str(i)] = list(face)
        i += 1
    
    #add boxes
    for (column, row, width, height) in detected_faces.values():
        cv.rectangle(
            original_image,
            (column, row),
            (column + width, row + height),
            (0, 255, 0),
            2
        )
    
    #save metadata
    detected_faces["count"] = len(detected_faces)
    detected_faces["executed"] = True

    #save image
    cv.imwrite(output_filename, original_image)


    return {
        "count": detected_faces["count"],
        "executed": detected_faces["executed"]
    }

    
    # returns : {
    #     "face0": the (column, row, width, height) for a face, can be renamed
    #     "face...": more faces
    #     "count": number of the faces
    #     "executed": <True> if normally executed
    # }


if __name__ == "__main__":
    print( detect("faceTest04.png", "output.jpg") )
