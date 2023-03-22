import glob
import pandas as pd
import numpy as np
import preprocessing_functions

def get_blink_bite_filenames():
    path = 'sample_data'
    bites = []
    blinks = []
    files = glob.glob(path + '/*.csv')
    for f in files:
        if 'bad' not in f:
            if 'blink' in f:
                blinks.append(f)
            elif 'bite' in f:
                bites.append(f)
    return bites, blinks

def get_all_filenames():
    path = 'sample_data'
    files = []
    glob_files = glob.glob(path + '/*.csv')
    for f in glob_files:
        if 'bad' not in f:
            files.append(f)
    return files

def get_bite_blink_dataframes(with_time, front_electrodes_only):
    """
    :param: with_time Boolean to specify if timestamps are included in the df
    :param: front_electrodes_only will not include TP09 and TP10 in each df
    :returns: an arrays of blink and bite Pandas dataframes from the sample_data folder
    """
    bites, blinks = get_blink_bite_filenames()
    bite_dataframes = []
    blink_dataframes = []

    for bite_file in bites:
        if with_time:
            if front_electrodes_only:
                bite_dataframes.append(pd.read_csv(bite_file, skiprows=0, usecols=[1, 3, 4]))
            else:
                bite_dataframes.append(pd.read_csv(bite_file, skiprows=0, usecols=[*range(1, 6)]))
        else:
            if front_electrodes_only:
                bite_dataframes.append(pd.read_csv(bite_file, skiprows=0, usecols=[*range(3, 5)]))
            else:
                bite_dataframes.append(pd.read_csv(bite_file, skiprows=0, usecols=[*range(2, 6)]))

    for blink_file in blinks:
        if with_time:
            if front_electrodes_only:
                blink_dataframes.append(pd.read_csv(blink_file, skiprows=0, usecols=[1, 3, 4]))
            else:
                blink_dataframes.append(pd.read_csv(blink_file, skiprows=0, usecols=[*range(1, 6)]))
        else:
            if front_electrodes_only:
                blink_dataframes.append(pd.read_csv(blink_file, skiprows=0, usecols=[*range(3, 5)]))
            else:
                blink_dataframes.append(pd.read_csv(blink_file, skiprows=0, usecols=[*range(2, 6)]))

    return bite_dataframes, blink_dataframes


def get_all_dataframes(with_time, front_electrodes_only):
    """
    :param: with_time Boolean to specify if timestamps are included in the df
    :param: front_electrodes_only will not include TP09 and TP10 in each df
    :returns: a combined array of blink and bite Pandas dataframes from the sample_data folder
    """
    dataframes = []
    filenames = get_all_filenames()

    for f in filenames:
        if with_time:
            if front_electrodes_only:
                dataframes.append(pd.read_csv(f, skiprows=0, usecols=[1, 3, 4]))
            else:
                dataframes.append(pd.read_csv(f, skiprows=0, usecols=[*range(1, 6)]))
        else:
            if front_electrodes_only:
                dataframes.append(pd.read_csv(f, skiprows=0, usecols=[*range(3, 5)]))
            else:
                dataframes.append(pd.read_csv(f, skiprows=0, usecols=[*range(2, 6)]))
    return dataframes

def df_to_numpy_array(input_df, with_time, front_electrodes_only):
    """
    :param: input_df A Pandas dataframe in the format from CSVs in sample_data
    :param: with_time Boolean to specify if timestamps are included in the array
    :param: front_electrodes_only will not include TP09 and TP10 in the array
    :return: A NumPy array
    """
    if with_time:
        if front_electrodes_only:
            return input_df[['time', 'AF7', 'AF8']].values
        else:
            return input_df[['time', 'TP09', 'AF7', 'AF8', 'TP10']].values
    else:
        if front_electrodes_only:
            return input_df[['AF7', 'AF8']].values
        else:
            return input_df[['TP09', 'AF7', 'AF8', 'TP10']].values

def labelled_ICA(front_electrodes_only):
    """
    :type front_electrodes_only: bool
    :param: front_electrodes_only will not include TP09 and TP10 in the X arrays
    :returns: ndarray of all csv samples for X, and labels for bite/blink in y
    """
    file_list = get_all_filenames()
    if front_electrodes_only:
        x_array = np.array(preprocessing_functions.get_ICA(front_electrodes_only)).reshape(len(file_list), 4)
    else:
        x_array = np.array(preprocessing_functions.get_ICA(front_electrodes_only)).reshape(len(file_list), 16)

    y_array = []

    for name in file_list:
        if "blink" in name.lower():
            y_array.append("0")
        elif "bite" in name.lower():
            y_array.append("1")

    return x_array, np.array(y_array)
