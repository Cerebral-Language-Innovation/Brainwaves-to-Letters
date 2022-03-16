import os
import glob
import pandas as pd

# script to convert all csv files into one pandas Dataframe. Note the read in is not in the order stored on the computer.
# .iloc[][] will return that specific row and column in the data frame respectively.

# "Movement" types.. change as needed
MOVEMENT_TYPES = ['baseline', 'bite', 'blink']

FILEPATH = path_to_files = "/Users/markbenhamu/Desktop/QCLI/Data/Brainwaves-to-Letters/Bite and Blink Data Analysis v1"

# TODO: Make file path/naming more modular
'''
Function looks for the path to the data directory
'''
def dynamic_filepath():
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for name in dirs:
            if name == "Bite and Blink Data Analysis v1":
                return os.path.join(root, name)

def csv_to_dataframe(path_to_files = None):
    if path_to_files is not None:
        os.chdir(path_to_files)
    else:
        os.chdir(dynamic_filepath())

    file_extension = '.csv'

    # These are the column headers. Action type, time logs then all 4 channels (c1->c4) in order
    tmp = [['Type', 'Time', 'c1', 'c2', 'c3', 'c4']]

    for i in glob.glob(f"*{file_extension}"):
        type = check_type(i)
        data = pd.read_csv(i, usecols=[1, 6, 7, 8, 9])  # based on current csv formatting
        tmp.append([type, data['time'], data['c1'], data['c2'], data['c3'], data['c4']])

    headings = tmp.pop(0)
    temp = pd.DataFrame(tmp, columns=headings)
    return temp

'''
Determines action type from CSV name.
@:returns movement type name if found in file name
'''
def check_type(file_name):
    for a in range(len(MOVEMENT_TYPES)):
        if MOVEMENT_TYPES[a] in file_name.lower():
            return MOVEMENT_TYPES[a]
    raise ValueError("Input file: " + file_name + " has no recognizable movement type")