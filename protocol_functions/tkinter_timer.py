import tkinter
import time

class Timer(tkinter.Tk):
    ACTION_BACKGROUND_COLOUR = "green"
    ACTION_TEXT_COLOUR = "white"
    BACKGROUND_COLOUR = "white"
    TEXT_COLOUR = "black"

    def __init__(self, count_from, action_type):
        tkinter.Tk.__init__(self)
        self.title("QCLI Muse Data Collection")
        self.geometry("300x300")  # Setting window size
        self.label = tkinter.Label(self, font=("Arial", 100))
        self.label.pack()
        self.remaining = count_from
        self.action_type = action_type.title()
        self.action_timing = int(count_from/2)
        self.stream_started = None

    def prompt_action(self):
        self.label.configure(text=str(self.action_type), background=self.ACTION_BACKGROUND_COLOUR,
                             foreground=self.ACTION_TEXT_COLOUR)
        self.configure(background=self.ACTION_BACKGROUND_COLOUR)

    def countdown(self):
        while True:
            if self.remaining <= 0:
                self.end_timer()
                break
            if self.remaining == self.action_timing:
                self.prompt_action()
            else:
                self.label.configure(text="%d" % self.remaining, background=self.BACKGROUND_COLOUR,
                                     foreground=self.TEXT_COLOUR)
                self.configure(background=self.BACKGROUND_COLOUR)
            self.remaining -= 1
            self.update()
            time.sleep(1)

    def end_timer(self):
        # time.sleep(1)
        # TODO: ending screen
        self.destroy()



def run(count_from, action_type):
    """
    count_from: start time on countdown
    action_type: EG, Bite, Blink, etc.
    action_timing: time when the user should be alerted
    """
    timer = Timer(count_from=count_from, action_type=action_type)
    timer.countdown()


run(10, "Bite")