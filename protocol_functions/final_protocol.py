# TODO: Improve on the defensive programming
# TODO: Improve ease of use. Wording here is a bit hard to follow on the user end.
# TODO: Check for stream in from muselsl?
# TODO: Add support for more actions

import pandas as pd
import time
import os
from pylsl import *
from datetime import datetime
import user_info_input


def bad_sample_check():
    bad_recording = str(input('Was this a good sample? \n Enter (Y\\N): '))
    if bad_recording.upper() == "Y":
        return True
    elif bad_recording.upper() == "N":
        return False
    else:
        print("Invalid input. Enter Y or N.")
        return bad_sample_check()


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
    person_name = user_info_input.input_name()
    action_name = user_info_input.input_action()
    action_time = user_info_input.sample_length()
    collection_date = datetime.now().strftime("%d-%m-%Y_%H:%M")

    file_name = collection_date + "_" + person_name + "_" + action_name + "_" + str(action_time) + "seconds.csv"
    print("Resulting file name: " + file_name)

    while not stream_started():
        continue

    stream = resolve_stream('type', 'EEG')
    inlet = StreamInlet(stream[0])

    names = ['time', 'TP09', 'AF7', 'AF8', 'TP10']
    df = pd.DataFrame(columns=names)

    while not relax_check():
        continue

    start = time.time()
    notified = False
    while 1:
        s, t = inlet.pull_sample()
        df = pd.concat([df, pd.DataFrame.from_records([{'time': t,
                                                        'TP09': s[0],
                                                        'AF7': s[1],
                                                        'AF8': s[2],
                                                        'TP10': s[3]}])], ignore_index=True)
        # 'RIGHT_AUX': s[4] can be added to the pd.concat, but is unnecessary
        if time.time() - start > (action_time / 2) and not notified and action_name != "baseline":
            notified = True
            print("\n" + action_name + " now." + "\n")

        if time.time() - start > action_time:
            break

    # Starts at 0 rather than UNIX by subtracting first timestamp
    first_sample = df['time'][0]
    for x in range(0, (len(df['time'] - 1))):
        df['time'][x] -= first_sample

    directory = os.getcwd()
    directory = directory.replace("protocol_functions", "sample_data")

    bad_sample = bad_sample_check()
    if not bad_sample:
        file_name = file_name[:-4] + '_BAD' + file_name[-4:]  # Adds BAD to the file name

    return df.to_csv(directory + "/" + file_name)  # converting data to csv


if __name__ == "__main__":
    main()
