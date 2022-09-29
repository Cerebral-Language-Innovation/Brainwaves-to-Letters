"""
# TODO: Improve on the defensive programming- some errors could happen based on issues with types etc. (EG if the user
        enters a string for the time_amount integer input)
# TODO: Improve ease of use. Some of the wording here is a bit hard to follow on the user end also.
# TODO: Add in labelling of the specific channels in the data? Rather than C1, etc.
        Q: How do we know which is which?
"""

from user_info_input import *
import pandas as pd
import time
import os
from pylsl import *
from datetime import date


def stream_started():
    started = input("Have you connected to the Muse in uVicMUSE and started a stream? \n(Y/N): ")
    if started.lower() == "y":
        return True
    else:
        print("Please connect to uVicMUSE and start a stream. Asking this question again.")
        return False


def relax_check():
    relaxed = input("Are you in a relaxed state according to the protocol instructions? \n(Y/N): ")
    if relaxed.lower() == "y":
        return True
    else:
        print("Please get into a relaxed state as per the protocol instructions. Asking this question again.")
        return False


def main():
    person_name = input_name()
    action_name = input_action()
    action_time = 10  # Can be changed to sample_length() function for time selection.
    collection_date = date.today().strftime("%d-%m-%Y")

    file_name = collection_date + "_" + person_name + "_" + action_name + "_" + str(action_time) + "seconds.csv"
    print("Resulting file name: " + file_name)

    while not stream_started():
        continue

    stream = resolve_stream('type', 'EEG')
    inlet = StreamInlet(stream[0])

    names = ['time', 'c1', 'c2', 'c3', 'c4']  # corrected names for the channel columns
    df = pd.DataFrame(columns=names)

    while not relax_check():
        continue

    start = time.time()
    notified = False

    while 1:
        s, t = inlet.pull_sample()
        df = pd.concat([df, pd.DataFrame.from_records([{'time': t,
                                                        'c1': s[0],
                                                        'c2': s[1],
                                                        'c3': s[2],
                                                        'c4': s[3]}])], ignore_index=True)
        if time.time() - start > (action_time / 2) and not notified and action_name != "baseline":
            notified = True
            print(action_name + "now")

        if time.time() - start > action_time:
            break

    directory = os.getcwd()
    directory = directory.replace("protocol_functions", "sample_data")

    df.to_csv(directory + "/" + file_name)  # converting data to csv


if __name__ == "__main__":
    main()
