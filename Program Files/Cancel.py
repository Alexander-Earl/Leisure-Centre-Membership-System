from MainApp import *
from tkinter import *
from Database import *


class Cancel(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        self.controller = controller
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")

        # This segment implements the 'Cancel Subscription' banner onto the window.
        self.cancel_photo = PhotoImage(file="Images/Cancel Subscription Title.png")
        self.cancel_banner = Label(self, image=self.cancel_photo, height=90, width=725, borderwidth=0, activebackground="#97c7f1")
        self.cancel_banner.pack()
        self.cancel_banner.config(bg="#97c7f1")

        # This block implements a back button which allows a user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=lambda: controller.show_frame("InternalMenu"),
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This spacer allows for a gap between the 'Cancel Subscription' banner and the confirmation notice.
        self.space = Label(self, text="", font=("", 45))
        self.space.pack()
        self.space.config(bg="#97c7f1")

        # This block is a label widget which displays a confirmation notice to the member.
        self.confirmation_notice = Label(self, text="By clicking "
                                                    "the “Okay”  button,\n"
                                                    "you are agreeing to the Terms & Conditions\n "
                                                    "as well as confirming that"
                                                    " you want to cancel your\n membership with "
                                                    "Crook Log Leisure Centre.", font=("", 20))
        self.confirmation_notice.pack()
        self.confirmation_notice.config(bg="#97c7f1")

        # This spacer allows for a gap between the confirmation notice and the 'Okay' button.
        self.space1 = Label(self, text="", font=("", 20))
        self.space1.pack()
        self.space1.config(bg="#97c7f1")

        # This block implements the 'Okay' button which is only pressed by the member when they are certain about
        # cancelling their subscription with Crook Log. This button then executes the 'cancel' method.
        self.okay_photo = PhotoImage(file="Images/Small Okay Button.png")
        self.okay_button = Button(self, image=self.okay_photo, command=self.cancel,
                        height=65, width=150, borderwidth=0, activebackground="#97c7f1")
        self.okay_button.pack()
        self.okay_button.config(bg="#97c7f1")

    # This method terminates the member's subscription and revokes their access to entering the system.
    # The method also signs the member out of the system and redirects them back to the 'Welcome' page.
    def cancel(self):
        """Functionality for membership cancellation"""
        connection.connect(user="root", password="")
        query = "UPDATE users INNER JOIN logged_in_users ON logged_in_users.User_ID = users.User_ID SET Status = 'INACTIVE' WHERE Logged_Out_Time IS NULL;"
        cursor.execute(query)
        connection.commit()
        connection.close()
        self.controller.show_frame("ThankYou")