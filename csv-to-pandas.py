import os
import glob
import pandas as pd
from IPython.core.display import display

# script to convert all csv files into one pandas Dataframe. Note the read in is not in the order stored on the computer.
# displaying/printing is odd due to the large number of entries per "index". use .iloc[] to access a specific "file"
# .iloc[][] will return that specific row and column in the data frame respectively.
# I called the data frame ye cuz idk why not

# Path to files where all csv data folders are stored
path_to_files = "/Users/markbenhamu/Desktop/QCLI/Data/Brainwaves-to-Letters/Bite and Blink Data Analysis v1"
os.chdir(path_to_files)
file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"*{file_extension}")]

# These are the column headers. Action type, time logs then all 4 channels (c1->c4) in order
tmp = [['Type', 'Time', 'c1', 'c2', 'c3', 'c4']]

# "Movement" types.. change as needed
types = ['baseline', 'bite', 'blink']


# Determines action type from what was saved in file. Should be modular enough for any changes in what actions we are recording
def check_type(file_name):
    a = 0
    while a < len(types):
        if types[a] in file_name.lower():
            return types[a]
        a = a + 1


for i in glob.glob(f"*{file_extension}"):
    Type = check_type(i)
    data = pd.read_csv(i, usecols=[1, 6, 7, 8, 9])  # based on current csv formatting
    tmp.append([Type, data['time'], data['c1'], data['c2'], data['c3'], data['c4']])

headings = tmp.pop(0)
ye = pd.DataFrame(tmp, columns=headings)
display(ye.columns.values)
print(ye.iloc[0])
print(ye.iloc[len(ye)-1])
