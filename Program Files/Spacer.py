from tkinter import *
import time


class Spacer(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")

        self.welcome_lbl = Label(self, text="                               ", font=("", 26))
        self.welcome_lbl.pack()
        self.welcome_lbl.config(bg="#97c7f1")

        # This segment creates the 'clock_frame' label widget, which is used to output live date and time to the users
        # of the system in a real-time manner.
        self.clock_frame = Label(self, font=("", 16, "bold"))
        self.clock_frame.pack()
        self.clock_frame.config(bg="#97c7f1")

        # This statement executes runs the 'clock' method as soon as the program starts.
        self.clock()

        # This segment implements the gym advertisement banner, when pressed, the system redirects the user to the 'Sign
        # Up' page in attempt to get the user to join Crook Log's monthly membership scheme.
        self.gym_price_photo = PhotoImage(file="Images/Gym Price Banner.png")
        self.gym_price = Button(self, image=self.gym_price_photo, command=lambda: controller.show_frame("MemberSignUpPage"),
                        height=270, width=260, borderwidth=0, activebackground="#97c7f1")
        self.gym_price.pack()
        self.gym_price.config(bg="#97c7f1")

        # This segment implements the 'Swim23' advertisement banner which when pressed, will redirect the user to the
        # 'Sign Up' page in attempt to get them to join Crook Log's monthly membership scheme.
        self.swim23_price_photo = PhotoImage(file="Images/Swim23 Price Banner.png")
        self.swim23_price = Button(self, image=self.swim23_price_photo, command=lambda: controller.show_frame("MemberSignUpPage"),
                        height=320, width=265, borderwidth=0, activebackground="#97c7f1")
        self.swim23_price.pack()
        self.swim23_price.config(bg="#97c7f1")

    # The 'clock' method is executed so the latest date and time can be outputted to the user via the 'clock_frame'
    # label widget. The method re-executes itself every second in order to output the latest date and time.
    def clock(self, time1=""):
        time2 = time.strftime("%A, %d %b %Y\n%H:%M:%S")
        if time2 != time1:
            time1 = time2
            self.clock_frame.config(text=time2)
        self.clock_frame.after(1000, self.clock)
