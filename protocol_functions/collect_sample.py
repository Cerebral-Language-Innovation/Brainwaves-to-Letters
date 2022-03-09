import mne
from mne import *
import protocol_functions.tkinter_timer
import pandas as pd
import time
from pylsl import *


def run(sample_length, action_name, file_name):
    stream = resolve_stream('type', 'EEG')
    inlet = StreamInlet(stream[0])

    info = inlet.info()
    name = info.name()
    # look at the stream frequency
    stream_freq = info.nominal_srate()  # 256

    # look at these for insight
    channel_format = inlet.channel_format()
    channel_indices_by_type(info)

    # creating a data set
    c1, c2, c3, c4, timestamps = [], [], [], [], []
    names = ['time', 'c1', 'c2', 'c3', 'c4'] # corrected names for the channel columns
    df = pd.DataFrame(columns=names)
    start = time.time()
    # Starts a GUI to notify the participant when to start their action.
    protocol_functions.tkinter_timer.run(sample_length, action_name.title(), int(sample_length/2))
    while 1:
        s, t = inlet.pull_sample()
        print(s, t)
        df = df.append(
            {'time': t,
             'c1': s[0],
             'c2': s[1],
             'c3': s[2],
             'c4': s[3]},
            ignore_index=True)
        if time.time() - start > sample_length:
            break

    return df.to_csv(file_name) # converting data to csv