systems = {1: "Windows", 2: "Linux", 3: "macOS"}


# Key indexes store the OS name as their values so the user can see their selection.
'''
Function returns user's operating system as an int. 1 for Windows, 2 for Linux, and 3 for macOS.
'''


def run():
    while 1:
        operating_system = int(input(
            "Please input the number corresponding to your device operating system\n1)Windows\n2)Linux\n3)macOS\nYour "
            "Input: "))
        if (operating_system != 1) and (operating_system != 2) and (operating_system != 3):
            print("Please select one of the 3 OS options")
            continue
        else:
            print("Executing the process for a device running " + systems[operating_system])
        break
    return operating_system
