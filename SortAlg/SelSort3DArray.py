# colorChoice: red, green, blue is 0, 1, 2 respectively
def PrintSortedElements(array, colorChoiceIndex):
    print("Here are the pixels of your color selection all sorted horizontally")

    i = 0
    for i in range(len(array)):

        j = 0
        for j in range(len(array[j])):

            print(str(array[i][j][colorChoiceIndex]), end ="-")
        print("\n---Next Row---")

    print("Done Processing.")

def SelSort3DArray(inputArr, colorChoice):

    if colorChoice == "red" or colorChoice == "hue":
        colorChoiceIndex = 0

    if colorChoice == "green" or colorChoice == "sat":
        colorChoiceIndex = 1

    if colorChoice == "blue" or colorChoice == "val":
        colorChoiceIndex = 2

    print("Your picture has a length of: " + str(len(inputArr)) + " x " + str(len(inputArr[0])))
    print("Processing... sorting with ", colorChoice)

    i = 0
    while i < len(inputArr):

        j = 0

        while j < len(inputArr[i]) - 1: #perform n-1 searches of 2nd lvl of array

            minIndex = j
            k = j+1

            while k < len(inputArr[i]): #for each 2nd level of array (..a row of pixels..)
                                        #sort rgb arrays in order of color choice lowest to highest

                if inputArr[i][k][colorChoiceIndex] < inputArr[i][minIndex][colorChoiceIndex]:
                    minIndex = k
                k += 1

            if minIndex != j:
                temp = inputArr[i][j]
                inputArr[i][j] = inputArr[i][minIndex]
                inputArr[i][minIndex] = temp

            j += 1

        i += 1

    PrintSortedElements(inputArr, colorChoiceIndex)

    return inputArr

if __name__=="__main__":
    userInput = input("Enter a color (red, green or blue): ")
    SelSort3DArray(array, "red")
