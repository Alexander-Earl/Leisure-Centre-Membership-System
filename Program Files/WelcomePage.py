from tkinter import *
from MainApp import *


class Welcome(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Configures the window to have the selected background colour.
        self.config(bg="#97c7f1")

        # This block implements the welcome banner onto the welcome window.
        self.welcome_title = PhotoImage(file="Images/Welcome Title.png")
        self.welcome = Label(self, image=self.welcome_title, height=90, width=725, borderwidth=0, activebackground="#97c7f1")
        self.welcome.pack()
        self.welcome.config(bg="#97c7f1")

        # This block of code allows for a space between the banner and the "Welcome!" button.
        self.welcome_spacer = Label(self, text="", font=("", 165))
        self.welcome_spacer.pack()
        self.welcome_spacer.config(bg="#97c7f1")

        # This block implements the "Welcome!" button in order to allow users to redirect to the external menu window.
        self.welcome_button_image = PhotoImage(file="Images/Welcome_Button.png")
        self.welcome_button = Button(self, image=self.welcome_button_image, command=lambda: controller.show_frame("ExternalMenu"),
                        height=150, width=450, borderwidth=0, activebackground="#97c7f1")
        self.welcome_button.pack()
        self.welcome_button.config(bg="#97c7f1")