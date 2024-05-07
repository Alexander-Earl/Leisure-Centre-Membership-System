from tkinter import *


class ThankYou(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        self.controller = controller
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")

        # This segment implements the 'Thank You' banner.
        self.thank_you_photo = PhotoImage(file="Images/Thank You.png")
        self.thank_you_banner = Label(self, image=self.thank_you_photo,
                                      height=70, width=500,
                                      borderwidth=0, activebackground="#97c7f1")
        self.thank_you_banner.pack()
        self.thank_you_banner.config(bg="#97c7f1")

        # This spacer implements a gap between the 'Thank You' banner and the 'Okay' button.
        self.spacer = Label(self, text="", font=("", 165))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This segment implements the 'Okay button which when pressed redirects the user back to the 'Welcome' page.
        self.okay_photo = PhotoImage(file="Images/Okay Button.png")
        self.okay_button = Button(self, image=self.okay_photo,
                                                 command=lambda :controller.show_frame("Welcome"), height=100, width=300,
                                                 borderwidth=0, activebackground="#97c7f1")
        self.okay_button.pack()
        self.okay_button.config(bg="#97c7f1")