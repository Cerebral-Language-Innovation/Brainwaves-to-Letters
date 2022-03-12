'''
Functions for verifying the individual inputs
# TODO: Improve on the defensive programming- some errors could happen based on issues with types etc. (EG if the user enters a string for the time_amount integer input)
  # Could also notify the user about the timing ranges, or their input being inconsistent with the array of possible actions
# TODO: Improve ease of use. Some of the wording here is a bit hard to follow on the user end also.
#  done: Add a date and time option so they are all differnt files.
#  done: Add a "ready to start?" question
'''

import pandas as pd
import time
import os
from pylsl import *

def input_name():
  while (1):
    name = input("Please enter your name: ")
    correct = input("You entered " + name.title() + " as your name.\nContinue? \n(Y/N): ")
    if correct.lower() == "y":
      return name.lower()
    else:
      continue

def input_date():
  while (1):
    date = input("Please enter the datetime mm-dd-yy, e.g. feb 24 2022: 02-24-22: ")
    correct = input("You entered " + date.title() + " as the date.\nContinue? \n(Y/N): ")
    if correct.lower() == "y":
      return date.lower()
    else:
      continue

def input_action():
  action_arr = ["Bite", "Blink", "Chatter"] # Will be modified in the future- I used these 3 array elements to test the code
  while (1):
    for x in range(0, len(action_arr)):
      action = action_arr[x]
      print(str(x + 1) + ") " + action_arr[x])
    action_num = int(input("Enter the action you will be performing: "))
    selected_action = (action_arr[(action_num - 1)]).lower() # -1 since the printed list starts at 1.

    # Checking the action selected is in the array
    if 0 < action_num <= len(action_arr):
      correct = input("You will be performing a " + selected_action + " for this sample.\nContinue? \n(Y/N): ")
      if correct.lower() == "y":
        return selected_action
    else:
      continue

#Checks if the input is a string or a number
# would a decimal character identify as a character or digit?
def isNumber(input):
  # Loops through each character of the input
  for i in range(len(input)):
    # Checks if the current character is a number
    if input[i].isdigit() != True:
      # The current character is not a number, so the input must be a string
      return False

  return True

def input_time():
  while (1):
    time_amount = int(input("Enter the total sample collection time (seconds): "))
    if 1 < time_amount <= 120: # I set bounds for time here. These can be changed easily though
      correct = input("The sample will be taken for " + str(time_amount) + " seconds.\nContinue? \n(Y/N): ")
      if correct.lower() == "y":
        return time_amount
    else:
      continue

def main():
  # get sample info
  person_name = input_name()
  action_name = input_action()
  action_time = input_time()
  collection_date = input_date()
  file_name = collection_date + "_" +person_name + "_" + action_name + "_" + str(action_time) + "seconds.csv"
  print("Resulting file name: " + file_name + ".csv")
  # os.system("uvicmuse") # search, connect, start strea
  print("in another terminal type 'uvicmuse' search for device, connect to muse, and start stream")
  while (1):
    cont = int(input("type 1 if connected and stream started"))
    break
  stream = resolve_stream('type', 'EEG')
  inlet = StreamInlet(stream[0])

  names = ['time', 'c1', 'c2', 'c3', 'c4'] # corrected names for the channel columns
  df = pd.DataFrame(columns=names)
  startrelax = time.time()
  # relax
  print("take a deep breath")
  while time.time() - startrelax < 5:
    print(' take a deep breath ')
      # take deep breath

  print('start reading')
  start = time.time()
  while 1:
      s, t = inlet.pull_sample()
      df = df.append(
          {'time': t,
           'c1': s[0],
           'c2': s[1],
           'c3': s[2],
           'c4': s[3]},
          ignore_index=True)
      if time.time() - start > (action_time/2):
        print("DO " + action_name + " NOW!!!!!!!") # so they know
      else:
        print(s, t)
      if time.time() - start > action_time:
        break

  df.to_csv(file_name) # converting data to csv


if __name__ == "__main__":
  main()
