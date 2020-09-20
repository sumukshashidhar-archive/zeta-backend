from machine_learning.handwriting_recognition import SimpleHTR as SimpleHTR

def analyse(input_filename):
    """Analyses and outputs predicted text from the given picture

    Args:
        input_filename (string): The filepath that can be opened and analysed

    Returns:
        dict: A dictionary with certain values
    """

    results = SimpleHTR.predict(input_filename)

# 	"recognized": results[0][0],
# 	"probability": float(results[1][0])

    return {
        "text_predicted": results[0][0], 
        "accuracy_rate": float(results[1][0])
    }


#test
#print(analyse(".\\test.png"))
