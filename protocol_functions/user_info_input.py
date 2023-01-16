def input_name():
    while 1:
        name = input("Please enter your first name, a space, then your last initial: ")
        correct = input("You entered " + name.title() + " as your name.\nContinue? \n(Y/N): ")
        if correct.lower() == "y":
            name = name.replace(" ", "_")
            return name.lower()
        else:
            continue


# TODO: Check for packages? Using sys to see if the user has the required packages or not?
def install_packages():
    packages = input("Do you have all of the necessary packages installed? \n(Y/N): ")
    if packages.lower() == "y":
        return True
    else:
        return False


# TODO: Add defensive programming for this function.
def input_action():
    action_arr = ["Baseline", "Bite", "Blink"]
    while 1:
        for x in range(0, len(action_arr)):
            print(str(x + 1) + ") " + action_arr[x])
        action_num = int(input("Enter the action you will be performing: "))

        # Check that this is within the list range.
        selected_action = (action_arr[(action_num - 1)]).lower()

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
    while 1:
        time_amount = int(input("Enter the total sample collection time (seconds): "))
        if 1 < time_amount <= 120:
            correct = input("The sample will be taken for " + str(time_amount) + " seconds.\nContinue? \n(Y/N): ")
            if correct.lower() == "y":
                return time_amount
        else:
            continue
