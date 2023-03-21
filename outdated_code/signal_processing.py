# creates a dataset of the signals to analyze with different transformations
# work in progress
import math
from os.path import exists
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats, scipy.signal
import scipy.stats, scipy.signal


# TODO: not seeing the functions giving good results, -> should we plot more...


# read a bunch in
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

names2 = ['chris', 'daniel','eva', 'judah', 'leo', 'quinn']
actions2 = ['blink', 'bite']
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
dates = ['02-24-22', '03-24-22', '03-24']
names3 = ['eva', 'chris', 'leo', 'judah']
times = ['6seconds', '5seconds', '10seconds', '8seconds']
actions3 = ['blink', 'bite']
for i in names3:
    for j in actions3:
        if j=='blink':
            for k in times:
                for d in dates:
                    blinkfiles.append(d + "_" +i + "_" + j + '_'+ k + ".csv")
        else:
            for k in times:
                for d in dates:
                    bitefiles.append(d + "_" + i + "_" + j + "_"+ k + ".csv")

newfiles = [
'03-16-22-2_mark_blink_6seconds.csv',
'03-16-22_dan_blink_6seconds.csv',
'03-16-22_eva_blink_6seconds.csv',
'03-16-22_judah_blink_6seconds.csv',
'03-16-22_leo_blink_6seconds.csv',
'03-16-22_mark_blink_6seconds.csv',
'03-16-22_mark_blink_6seconds.csv'
]
for i in newfiles:
    blinkfiles.append(i)

bites = ['03-16-22_dan_bite_6seconds.csv',
'03-16-22_eva_bite_6seconds.csv',
'03-16-22_eva_bite_10seconds.csv',
'03-16-22_judah_bite_6seconds.csv',
'03-16-22_leo_bite_6seconds.csv',
'03-16-22_mark_bite_6seconds.csv',"03-16-22-2_mark_bite_6seconds.csv"]

for i in bites:
    bitefiles.append(i)

eyes = ["03-16-22-2_mark_eyebrow_6seconds.csv",
'03-16-22_mark_eyebrow_6seconds.csv'
'03-16-22_leo_eyebrow_6seconds.csv',
'03-16-22_judah_eyebrow_6seconds.csv',

            ]

df = pd.DataFrame(columns = ['signal', 'channel', 'action', 'accumulated energy', 'initial steepness', 'ascent steppness', 'decsent steepness', 'meanvariance', 'snr'])
prefix = 'Brainwaves-to-Letters/Bite and Blink Data Analysis v1/'
for blink in blinkfiles:
    if(exists(prefix+blink)):
        d = pd.read_csv(prefix + blink)
        darray = np.array(d.c3)
        df = df.append({'signal' : darray, 'channel' : 3, 'action' : 0}, ignore_index = True)
        darray = np.array(d.c1)
        df = df.append({'signal' : darray, 'channel' : 1, 'action' : 0}, ignore_index = True)
        darray = np.array(d.c2)
        df = df.append({'signal' : darray, 'channel' : 2, 'action' : 0}, ignore_index = True)
        darray = np.array(d.c4)
        df = df.append({'signal' : darray, 'channel' : 4, 'action' : 0}, ignore_index = True)

    elif(exists(blink)):
        d = pd.read_csv(blink)
        darray = np.array(d.c3)
        df = df.append({'signal' : darray, 'channel' : 3,'action' : 0}, ignore_index = True)
        darray = np.array(d.c1)
        df = df.append({'signal' : darray, 'channel' : 1, 'action' : 0}, ignore_index = True)
        darray = np.array(d.c2)
        df = df.append({'signal' : darray, 'channel' : 2, 'action' : 0}, ignore_index = True)
        darray = np.array(d.c4)
        df = df.append({'signal' : darray, 'channel' : 4, 'action' : 0}, ignore_index = True)
    elif(exists('Brainwaves-to-Letters/' + blink)):
        d = pd.read_csv('Brainwaves-to-Letters/' + blink)
        darray = np.array(d.c3)
        df = df.append({'signal': darray, 'channel' : 3,'action': 0}, ignore_index=True)
        darray = np.array(d.c1)
        df = df.append({'signal' : darray, 'channel' : 1, 'action' : 0}, ignore_index = True)
        darray = np.array(d.c2)
        df = df.append({'signal' : darray, 'channel' : 2, 'action' : 0}, ignore_index = True)
        darray = np.array(d.c4)
        df = df.append({'signal' : darray, 'channel' : 4, 'action' : 0}, ignore_index = True)



for bite in bitefiles:
    if(exists(prefix+bite)):
        d = pd.read_csv(prefix + bite)
        darray = np.array(d.c3)
        df = df.append({'signal' : darray, 'channel' : 3,'action' : 1}, ignore_index = True)
        darray = np.array(d.c1)
        df = df.append({'signal' : darray, 'channel' : 1, 'action' : 1}, ignore_index = True)
        darray = np.array(d.c2)
        df = df.append({'signal' : darray, 'channel' : 2, 'action' : 1}, ignore_index = True)
        darray = np.array(d.c4)
        df = df.append({'signal' : darray, 'channel' : 4, 'action' : 1}, ignore_index = True)

    elif(exists(bite)):
        d = pd.read_csv(bite)
        darray = np.array(d.c3)
        df = df.append({'signal' : darray, 'channel' : 3,'action' : 1}, ignore_index = True)
        darray = np.array(d.c1)
        df = df.append({'signal' : darray, 'channel' : 1, 'action' : 1}, ignore_index = True)
        darray = np.array(d.c2)
        df = df.append({'signal' : darray, 'channel' : 2, 'action' : 1}, ignore_index = True)
        darray = np.array(d.c4)
        df = df.append({'signal' : darray, 'channel' : 4, 'action' : 1}, ignore_index = True)

    elif(exists('Brainwaves-to-Letters/' + bite)):
        d = pd.read_csv('Brainwaves-to-Letters/' + bite)
        darray = np.array(d.c3)
        df = df.append({'signal': darray, 'channel' : 3,'action': 1}, ignore_index=True)
        darray = np.array(d.c1)
        df = df.append({'signal' : darray, 'channel' : 1, 'action' : 1}, ignore_index = True)
        darray = np.array(d.c2)
        df = df.append({'signal' : darray, 'channel' : 2, 'action' : 1}, ignore_index = True)
        darray = np.array(d.c4)
        df = df.append({'signal' : darray, 'channel' : 4, 'action' : 1}, ignore_index = True)




# for signal, transform, append under transform coloumn
def AccumulatedEnergy(event):
    sq = [x ** 2 for x in event]
    energy = sum(sq)
    return energy

def InitialSteepness(event, samplingInterval): # changed x to be event
    # Not sure how many samples are in a typical event
    start = event[: math.floor(len(event) / 2)]
    slope = []
    for i in range(len(event) - 1):
        slope.append((event[i] - event[i + 1]) / samplingInterval)
    avgSlope = sum(slope) / len(slope)
    return avgSlope

def AscentSteepness(event, samplingInterval):
    # Not sure how many samples are in a typical event
    cutoff = event.index(max(event))
    start = event[: cutoff]
    slope = []
    for i in range(len(x) - 1):
        slope.append(abs((x[i] - x[i + 1]) / samplingInterval))
    avgSlope = sum(slope) / len(slope)
    return avgSlope

def DescentSteepness(event, samplingInterval):
    # Not sure how many samples are in a typical event
    cutoff = event.index(max(event))
    start = event[cutoff:]
    slope = []
    for i in range(len(x) - 1):
        slope.append(abs((x[i] - x[i + 1]) / samplingInterval))
    avgSlope = sum(slope) / len(slope)
    return avgSlope

def MeanVarRatio(event):
    ratio = []
    lenSS = 20
    numSubsections = math.floor(len(event) / lenSS)
    for i in range(numSubsections):
        ratio.append((sum(event[(lenSS * i):(lenSS * (i + 1))]) / lenSS) / np.var(event[(lenSS * i):(lenSS * (i + 1))]))

    m = max(ratio)
    return m

def MeanScaledVar(event, lenSS=20):
    ratio = []
    numSubsections = math.floor(len(event) / lenSS)
    for i in range(numSubsections):
        ratio.append((sum(event[(lenSS * i):(lenSS * (i + 1))]) / lenSS) * np.var(event[(lenSS * i):(lenSS * (i + 1))]))
    m = max(ratio)
    return m

def signaltonoise(a, axis, ddof):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)

# this has format issues,
# also not really seeing a trend but should try with other electrodes and a shortened sample 1s ish invervals over the action

for s in df.signal:
    df = df.append({'SNR' : signaltonoise(s[3*256:4*256],0,0)}, ignore_index=True)
#fix this
df.SNR[0:11] = df.SNR[12:23]
df.SNR[11] = df.SNR[23]
df = df.drop([12,13,14,15,16,17,18,19,20,21,22,23])

snrs, m1, m2, m3, m4, m5, m6 = [], [], [], [], [], [], []

for s in df.signal:
    snrs.append(signaltonoise(s,0,0))
    m1.append(AccumulatedEnergy(s))
    m2.append(MeanVarRatio(s))
    m3.append(MeanScaledVar(s, lenSS=20))


#'accumulated energy', 'initial steepness', 'ascent steppness', 'decsent steepness', 'meanvariance', 'snr'

df['snr'] = snrs
df['accumulated energy'] = m1
df['meanvariance'] = m2
df['mean scaled var'] = m3

for i in range(len(df.signal)):
    if (df.action[i] == 0):
        plt.plot(df.signal[i], color = 'blue', label = 'blink')
    else:
        plt.plot(df.signal[i], color = 'green', label = 'bite')

#TODO: make a time labeling application
#TODO: just see if the NN can handle any of these, some stats maybe first
# we only want one signal in here ^ so some step to choose the best electrode, or we use a few of them

# analytics
x, y = [],[]
for i in range(len(df.signal)):
    x.append(df.signal[i])
    y.append(df.action[i])

X_train, X_validation, Y_train, Y_validation = train_test_split(x, y, test_size=0.2, random_state=42)

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
models.append(('RF', RandomForestClassifier()))
models.append(('MLP', MLPClassifier(hidden_layer_sizes=(64,15))))

# evaluate each model
results = []
names = []
for name, model in models:
  kfold = StratifiedKFold(n_splits=9, random_state=1, shuffle=True)
  cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
  results.append(cv_results)
  names.append(name)
  print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))






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


