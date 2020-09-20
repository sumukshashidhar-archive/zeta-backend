import json
import os

def predict(filename):
    mPath = ".\\simpTrain\\handwriting\\python36_venv\\"

    assert os.system("copy " + filename + " " + mPath + "SimpleHTR\\pic\\pic.png") == 0

    os.system(mPath + "Scripts\\python.exe " + mPath + "SimpleHTR\\src\\main.py")

    return json.loads(open(mPath + "SimpleHTR\\pic\\results.json", 'r').read())
