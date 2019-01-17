import glob
# paste your pngs in their folders in the same directory as this script
# example.. /setpoint4/filename.png
# \newcommand{\lineScale}{0.8} makes the lineScale variable work for a given value
# in this case.. 0.8
def figureNameGen():
    # grab all filenames that are PNG
    filenames = glob.glob('**/*.png', recursive=True)

    for filename in filenames:
        print("\\begin{figure}[H]")
        print("\\centering")
        print("\\includegraphics[width=\\lineScale\\linewidth]{" + filename + "}")
        print("\\caption{" + filename + "}")
        print("\\label{fig:" + filename + "}")
        print("\\end{figure}")
        print("")


if __name__=="__main__":
    figureNameGen()
