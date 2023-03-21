"""
NOTE: THIS FILE IS NOW OUTDATED AND NOT COMPATIBLE WITH THE CURRENT DATA FORMAT
"""
from file_importing import get_newer_files
import pandas as pd
import numpy as np

'''
A function which takes the data samples from the Bite and Blink Data analysis folder and makes them the same length.
The function accounts for the sample length to ensure the action is preserved.
'''


def cut_samples():
    df = pd.DataFrame(columns=['c1', 'c2', 'c3', 'c4'])

    bites, blinks = get_newer_files()
    bite_tuples = []
    blink_tuples = []

    for b in bites:
        length = b[(len(b) - 12)]  # logic issue with code seeing 10 as 0. Don't have a more elegant solution,
        # this is temporary
        if length == "0":
            length = 10
        bite_tuples.append((b, length))

    for b in blinks:
        length = b[(len(b) - 12)]
        if length == "0":
            length = 10
        blink_tuples.append((b, length))

    for blink in blinks:
        d = pd.read_csv(blink)
        df = df.append({'c1': np.array(d.c1), 'c2': np.array(d.c2), 'c3': np.array(d.c3), 'c4': np.array(d.c4)},
                       ignore_index=True)

    for bite in bites:
        d = pd.read_csv(bite)
        df = df.append({'c1': np.array(d.c1), 'c2': np.array(d.c2), 'c3': np.array(d.c3), 'c4': np.array(d.c4)},
                       ignore_index=True)

    # Temporary code which shows the number of samples.
    # These vary even within samples of the same labelled length. Discuss at next meeting.
    idx = 0
    for file, length in bite_tuples:
        print(len(df.loc[idx][0]))
        print(str(length) + " seconds")
        idx += 1

    for file, length in blink_tuples:
        print(len(df.loc[idx][0]))
        print(str(length) + " seconds")
        idx += 1



# TODO: Fix df.append, functionality will be deprecated soon from Pandas.
# TODO: Check the number of samples

cut_samples()