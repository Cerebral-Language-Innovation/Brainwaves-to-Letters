def input_name():
    # TODO: Add in user ID functionality
    while 1:
        name = input("Please enter your name: ")
        correct = input("You entered " + name.title() + " as your name.\nContinue? \n(Y/N): ")
        if correct.lower() == "y":
            return name.lower()
        else:
            continue


def install_packages():
    # TODO: Check for packages? Using sys to see if the user has the required packages or not?
    packages = input("Do you have all of the necessary packages installed? \n(Y/N): ")
    if packages.lower() == "y":
        return True
    else:
        return False


def input_action():
    # TODO: Make this more flexible by having a TXT file with a list of actions that gets read into an array
    action_arr = ["Bite", "Blink", "Chatter", "Baseline"]
    while 1:
        for x in range(0, len(action_arr)):
            print(str(x + 1) + ") " + action_arr[x])
        action_num = int(input("Enter the action you will be performing: "))
        selected_action = (action_arr[(action_num - 1)]).lower()  # -1 since the printed list starts at 1.

        # Checking the action selected is in the array
        if 0 < action_num <= len(action_arr):
            correct = input("You will be performing a " + selected_action + " for this sample.\nContinue? \n(Y/N): ")
            if correct.lower() == "y":
                return selected_action
        else:
            continue


# Checks if the input is a string or a number
def is_number(user_input):
    # Loops through each character of the input
    for i in range(len(user_input)):
        # Checks if the current character is a number
        if not user_input[i].isdigit():
            # The current character is not a number, so the input must be a string
            return False
    return True


def sample_length():
    # TODO: Possibly change if statement with time_amount? Should these bounds be any different?
    while 1:
        time_amount = int(input("Enter the total sample collection time (seconds): "))
        if 1 < time_amount <= 120:
            correct = input("The sample will be taken for " + str(time_amount) + " seconds.\nContinue? \n(Y/N): ")
            if correct.lower() == "y":
                return time_amount
        else:
            continue
