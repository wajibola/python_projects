"""
@author: waziri
"""

from tkinter import *
from tkinter.ttk import *

class ProgressBarApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        self.progress_bar = Progressbar(orient="horizontal",
                                        length=200, mode="determinate")
        self.progress_bar.pack(side=TOP)
    
        self.btn_start = Button(text="Start", command = self.start_progress_bar)
        self.btn_start.pack(side=LEFT)
        
        self.btn_stop = Button(text="Stop", command = self.stop_progress_bar)
        self.btn_stop.pack(side=RIGHT)

        self.btn_reset = Button(text="Reset", command = self.reset_progress_bar)
        self.btn_reset.pack(side=RIGHT)
        
        self.barVal = 0
        self.maxbarVal = 5000
        self.enable_bar = False
        
    def update_bar(self):
        if self.enable_bar == True:
            self.barVal += 1000
            self.progress_bar["value"] = self.barVal
            if (self.barVal < self.maxbarVal):
                # call update_bar every 1000 ms
                self.after(1000, self.update_bar)
            else:
                print("Progress bar update completed")


    def start_progress_bar(self):
        self.enable_bar = True
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 5000
        self.update_bar()
    

    def stop_progress_bar(self):
        self.enable_bar = False


    def reset_progress_bar(self):
        self.enable_bar = False
        self.barVal = 0
        self.progress_bar["value"] = self.barVal
        print("Progress bar reset")



pBar = ProgressBarApp()
pBar.mainloop()