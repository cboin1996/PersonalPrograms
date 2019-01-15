import glob
import pandas as pd
import matplotlib.pyplot as plt
import os

def textPlotter(filenames, columnNames):
    #iterates on filenames to open all text files
    for filename in filenames:
        #read in the text file, the columns are separated by \t
        data = pd.read_csv(filename, delimiter="\t", header = None)
        #rename all the columns to what you want.. this is written to work in general for n columns
        for i in range(0, len(data.columns)):
            #pandas default name for columns is integers index starting at 0
            data.rename(columns={i : columnNames[i]}, inplace=True)

        for i in range(0, len(data.columns)):
            #for every 2 columns produce a plot
            if i % 2 == 0:
                #clf clears the plot each iteration
                plt.clf()
                plt.plot(data[columnNames[i]], data[columnNames[i+1]], color="blue")
                plt.xlabel(columnNames[i])
                plt.ylabel(columnNames[i+1])

                #formatting the filename for saving witha relevant name
                filenameNoExtension = filename.replace('.txt', '')
                #remove spaces from columns names for savinn
                columnNamexNoSpace = columnNames[i].replace(' ', '')
                columnNameyNoSpace = columnNames[i + 1].replace(' ', '')
                #gets directory foldername for the appropriate graph to save to
                saveFolder = filenameNoExtension.split('/')
                plt.savefig(saveFolder[0] + '/' + columnNamexNoSpace + 'vs' + columnNameyNoSpace + saveFolder[1] + ".png")


def main():
    #takes all text files in any subdirectories to the current directory
    filenames = glob.glob('**/*.txt', recursive=True)

    columnNames = ["Time (s)", "Heater Output (V)", "Time (s)", "Temperature Sensor Output (V)"]
    textPlotter(filenames, columnNames)

if __name__=="__main__":
    main()
