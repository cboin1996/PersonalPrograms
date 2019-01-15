from PIL import Image
import numpy as np

from SelSort3DArray import SelSort3DArray

def processImage(userSelection):


    imageName = input("Enter the name of your image: ")

    try:
        image = Image.open(imageName)

    except:
        print("unrecognized file. quitting.")
        return

    if userSelection == 'hue' or userSelection == 'sat' or userSelection == 'val': #convert format to HSV if selected by user
        image = image.convert('HSV')

    imArr = np.array(image) #converts to numpy array

    processArr = SelSort3DArray(imArr, userSelection)

    if userSelection == 'hue' or userSelection == 'sat' or userSelection == 'val':
        processedImage = Image.fromarray(processArr, 'HSV') #convert back to image
        processedImage = processedImage.convert('RGB')

    if userSelection == "red" or userSelection == 'green' or userSelection == 'blue':
        processedImage = Image.fromarray(processArr, 'RGB')

    image.show()
    processedImage.show()

    userSave = input("Would you like to save this image? (yes/no): ")

    if userSave == "yes":
        filename = input("Enter a filename for your artwork: ")
        processedImage.save('/Users/christianboin/MyDocuments/Programming/Python/SortAlg/art/'+filename+'.png', 'PNG')
        print("Image saved.")
    else:
        print("have a lovely day.")

def main():

    userInput = input("Welcome to the image processor. \nPlease type 'HSV' or 'RGB' to continue: ")

    if userInput == 'RGB' or userInput == 'rgb':
        colorSelection = input("Enter a color choice of red, green or blue: ")

        if colorSelection == "red" or colorSelection == 'green' or colorSelection == 'blue':
            processImage(colorSelection)

        else:
            print("Oof.  Wrong input goodbye.")

    elif userInput == 'HSV' or userInput == 'hsv':
        hsvSelection = input("Enter a color choice of hue, saturation (sat) or value (val): ")

        if hsvSelection == 'hue' or hsvSelection == 'val' or hsvSelection == 'sat':
            processImage(hsvSelection)

        else:
            print("Oof.  Wrong input goodbye.", hsvSelection)

    else:
        print("Oof.  Wrong input goodbye.")

if __name__=="__main__":
    main()
