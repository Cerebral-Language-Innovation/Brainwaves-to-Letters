# Code mostly from here: https://stackoverflow.com/questions/10596988/making-a-countdown-timer-with-python-and-tkinter
import tkinter as tk
import time


class Timer(tk.Tk):
    ACTION_BACKGROUND_COLOUR = "green"
    ACTION_TEXT_COLOUR = "white"
    BACKGROUND_COLOUR = "white"
    TEXT_COLOUR = "black"

    def __init__(self, count_from, action_type, action_timing):
        tk.Tk.__init__(self)
        self.geometry("300x300")  # Setting window size
        self.label = tk.Label(self, font=("Arial", 100))
        self.label.pack()
        self.remaining = 0
        self.action_type = action_type
        self.action_timing = action_timing
        self.countdown(count_from)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= -1:
            self.end_timer()
        if self.remaining == self.action_timing:
            self.label.configure(text=str(self.action_type), background=self.ACTION_BACKGROUND_COLOUR,
                                 foreground=self.ACTION_TEXT_COLOUR)
            self.configure(background=self.ACTION_BACKGROUND_COLOUR)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
        else:
            if self.remaining >= 0:
                self.label.configure(text="%d" % self.remaining, background=self.BACKGROUND_COLOUR,
                                     foreground=self.TEXT_COLOUR)
                self.configure(background=self.BACKGROUND_COLOUR)
                self.remaining = self.remaining - 1
                self.after(1000, self.countdown)

    def end_timer(self):
        time.sleep(1)
        self.destroy()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    # Makes an instance of the GUI class and runs it
    # Parameters are specified this way so that they can be changed easily while testing
    app = Timer(count_from=10, action_type="Bite", action_timing=5)
