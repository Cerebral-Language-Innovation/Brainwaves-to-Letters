"""
This file contains multiple functions which can be used for EEG data preprocessing.
May repurpose parts of signal_processing.py
"""

import mne
from file_importing import get_newer_files
import pandas as pd
import numpy as np
import os


def fourier_transform(np_arrs, window_size):
    """
    :param window_size is the amount of time the sample
    :param np_arrs is an array of NumPy arrays with sample data
    :returns an array of data depending on the sampling window
    """
    if window_size % 4 != 0:  # window size must be multiple of 4
        return False
    # TODO: consider verbose and tstep parameters
    return mne.time_frequency.stft(np_arrs, window_size)


"""
def test_fourier():
    df = pd.DataFrame(columns=['c1', 'c2', 'c3', 'c4'])
    bites, blinks = get_newer_files()

    d = pd.read_csv(blinks[0])
    arr = [np.array(d.c1), np.array(d.c2), np.array(d.c3), np.array(d.c4)]

    fourier_transform(arr, 4)
    print("")
"""


# def PCA():
# def ICA():

# TODO: Different filter types, beta range. Notch filtering?
# TODO: Re-referencing at infinity?
# TODO: Look at resampling. Is this worth it?
# TODO: Rejecting channels based on data spectrum
# TODO: Artifact rejection?


def get_pandas_dataframes():
    """
    :returns an arrays of blink and bit Pandas dataframes from the sample_data folder
    """
    bites, blinks = get_newer_files()  # Function which searches for all bites and blinks from the sample_data folder
    bite_dataframes = []
    blink_dataframes = []

    for bite_file in bites:
        bite_dataframes.append(pd.read_csv(bite_file))

    for blink_file in blinks:
        blink_dataframes.append(pd.read_csv(blink_file))

    return bite_dataframes, blink_dataframes


def get_numpy_array(input_df):
    """
    :param: A Pandas dataframe in the format from CSVs in sample_data
    :return: A NumPy array
    """
    return input_df[['time', 'TP09', 'AF7', 'AF8', 'TP10']].values

def main():
    bite_dfs, blink_dfs = get_pandas_dataframes()
    np_bites = []
    np_blinks = []

    for df in bite_dfs:
        np_bites.append(get_numpy_array(df))
    for df in blink_dfs:
        np_blinks.append(get_numpy_array(df))

# Gets
