"""
This file contains multiple functions which can be used for EEG data preprocessing.
May repurpose parts of signal_processing.py
"""

import mne
from file_importing import get_newer_files
import pandas as pd
import numpy as np


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


def test_fourier():
    df = pd.DataFrame(columns=['c1', 'c2', 'c3', 'c4'])
    bites, blinks = get_newer_files()

    d = pd.read_csv(blinks[0])
    arr = [np.array(d.c1), np.array(d.c2), np.array(d.c3), np.array(d.c4)]

    fourier_transform(arr, 4)
    print("")


test_fourier()

# TODO: Implement these (and possibly more)
# TODO: Determine the format of the input data passed to the function

# def PCA():
# def ICA():

