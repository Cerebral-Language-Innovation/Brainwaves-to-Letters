# creates a dataset of the signals to analyze with different transformations
# work in progress

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats, scipy.signal
import scipy.stats, scipy.signal

# read a bunch in
names2 = ['chris', 'daniel','eva', 'judah', 'leo', 'quinn']
actions2 =  ['blink', 'bite']
time = ['5seconds']
filenames, blinkfiles, bitefiles = [], [], []
for i in names2:
    for j in actions2:
        if j=='blink':
            for k in time:
                blinkfiles.append(i + "_" + j + '_'+ k + ".csv")
        else:
            for k in time:
                bitefiles.append(i + "_" + j + "_"+ k + ".csv")

df = pd.DataFrame(columns = ['signal', 'action'])
prefix = 'Brainwaves-to-Letters/Bite and Blink Data Analysis v1/'
for blink in blinkfiles:
    d = pd.read_csv(prefix + blink)
    darray = np.array(d.c3)
    df = df.append({'signal' : darray, 'action' : [0]}, ignore_index = True)


for bite in bitefiles:
    d = pd.read_csv(prefix + bite)
    darray = np.array(d.c3)
    df = df.append({'signal' : darray, 'action' : [1]}, ignore_index = True)

# for signal, transform, append under transform coloumn
def signaltonoise(a, axis, ddof):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)

# this has format issues,
# also not really seeing a trend but should try with other electrodes and a shortened sample 1s ish invervals over the action
for s in df.signal:
    df = df.append({'SNR' : signaltonoise(s,0,0)}, ignore_index=True)



# TODO : add other channels specify channel name in a new column
# we only want one signal in here ^ so some step to choose the best electrode, or we use a few of them


# Visualizations
f1 = 'Brainwaves-to-Letters/02-24-22_eva_bite_8seconds'
f2 = 'Brainwaves-to-Letters/02-24-22_eva_blink_5seconds.csv'
f3 = 'Brainwaves-to-Letters/02-24-22_eva_blink_6seconds.csv'
f4 = 'Brainwaves-to-Letters/eva_bite_10seconds'

data = pd.read_csv(f1)
data = data.drop(columns='Unnamed: 0')
data.time = data.time - data.time[0]
data.time = data.time/1000000 # into seconds

#cut the data actiontime - 1: actiontime + 2, sfreq = 256 so 256*starts:256*ends
# 5or6s 2:6, 10s 4:8, 8s 3:7
# static time series
fig = plt.plot(data.time[256*3:256*7], data.c3[256*3:256*7], linewidth=0.1)
# massive spike in c3 only

#static square
fig = plt.plot(data.time[256*3:256*7], (data.c3[256*3:256*7])**2, linewidth=0.1)


