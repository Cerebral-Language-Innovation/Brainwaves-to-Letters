"""
This file contains multiple functions which can be used for EEG data preprocessing.
May repurpose parts of signal_processing.py
"""

import mne
import pandas as pd
import numpy as np
import file_importing

def get_ICA(front_electrodes_only):
    """
    :param: front_electrodes_only will not include TP09 and TP10 in ICA calculations
    :returns
    """
    # TODO: Clarify what this returns
    ica_subjects = []
    dataframe_arr = file_importing.get_all_dataframes(with_time=False, front_electrodes_only=front_electrodes_only)
    if front_electrodes_only:
        ch_names = ['AF7', 'AF8']
        ch_types = ['eeg', 'eeg']
    else:
        ch_names = ['TP09', 'AF7', 'AF8', 'TP10']
        ch_types = ['eeg', 'eeg', 'eeg', 'eeg']

    for df in dataframe_arr:
        sfreq = 255.66666667
        info = mne.create_info(ch_types=ch_types, ch_names=ch_names, sfreq=sfreq)
        raw = mne.io.RawArray(df.transpose(), info)
        raw.crop(tmax=5.9)
        raw.filter(14., 30.)

        ica = mne.preprocessing.ICA(random_state=97)
        ica.fit(raw)

        ica_subjects.append(ica.get_components())

    return ica_subjects

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


# def PCA():


# TODO: Different filter types, beta range. Notch filtering?
# TODO: Re-referencing at infinity?
# TODO: Look at resampling. Is this worth it?
# TODO: Rejecting channels based on data spectrum
# TODO: Artifact rejection?