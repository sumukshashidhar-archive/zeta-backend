from colorthief import ColorThief
import sys


def detect(input_filename):
    """Opens a filename and outputs the dominant color in the frame

    Args:
        input_filename (string): path to the image

    Returns:
        dict: a dictionary with the dominant color as a key-value pair
    """


    color_thief = ColorThief(input_filename)
    color = color_thief.get_color(quality=1)


    return {
        "dominant_color": color
    }


if __name__ == "__main__":
    print(detect("colorTest.jpg"))
