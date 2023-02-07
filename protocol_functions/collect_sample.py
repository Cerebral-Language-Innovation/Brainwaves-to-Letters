"""
NOTE: THIS FILE IS NOW OUTDATED AND NOT COMPATIBLE WITH THE CURRENT DATA FORMAT
"""

import mne
import time
import pandas as pd
import pylsl
import protocol_functions.tkinter_timer
import os

# TODO: Sensor naming in channels?
# TODO: Extracting any other sensor info?? Battery? Model?
# TODO: Make uVic alternative again from scratch?
# TODO: File naming + reorganization

# async def start_uvic():
#     os.system("uvicmuse")
#     while stream_started():
#         continue


def keep():
    bad_recording = str(input('Keep this recording? \n Enter (Y\\N): '))
    if bad_recording.upper() == "Y":
        return True
    elif bad_recording.upper() == "N":
        return False
    else:
        print("Invalid input. Enter Y or N.")
        return keep()

def run(sample_length, action_name, file_name):
    stream = pylsl.resolve_stream('type', 'EEG')
    inlet = pylsl.StreamInlet(stream[0])

    info = inlet.info()
    name = info.name()
    # look at the stream frequency
    stream_freq = info.nominal_srate()  # 256

    # look at these for insight
    # channel_format = inlet.channel_format()
    # indices = mne.channel_indices_by_type(info)

    # creating a data set
    names = ['time', 'c1', 'c2', 'c3', 'c4']  # corrected names for the channel columns
    df = pd.DataFrame(columns=names)
    start = time.time()
    # Starts a GUI to notify the participant when to start their action.
    # protocol_functions.tkinter_timer.run(sample_length, action_name.title())
    while 1:
        s, t = inlet.pull_sample()
        df = df.append(
            {'time': t,
             'c1': s[0],
             'c2': s[1],
             'c3': s[2],
             'c4': s[3]},
            ignore_index=True)
        if time.time() - start > sample_length:
            break
    keep_file = keep()
    if not keep_file:
        file_name = file_name[:-4] + '_BAD' + file_name[-4:]  # Adds FATAL to the file name
    return df.to_csv(file_name)  # converting data to csv

run(10, "Bite", "file_name.csv")