from tkinter import *
from MainApp import *
from Database import *


class ReactivateMembership(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")
        self.controller = controller

        # This block creates a gap between the member 'Reactivate Membership' banner and the 'Email' label.
        self.spacer = Label(self, text="", font=("", 96))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This block implements the 'Membership Reactivation' title onto the window.
        self.membership_photo = PhotoImage(file="Images/Membership Reactivation Title.png")
        self.membership_title = Label(self, image=self.membership_photo, height=65, width=730, borderwidth=0,
                                   activebackground="#97c7f1")
        self.membership_title.place(x=20, y=12)
        self.membership_title.config(bg="#97c7f1")

        # This section implements a back button which allows a user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=self.back,
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This block implements the 'Email:' label widget so that users of the system are aware of
        # the purpose of the entry box below.
        self.email_lbl = Label(self, text="Email:", font=("", 25))
        self.email_lbl.pack()
        self.email_lbl.config(bg="#97c7f1")

        # This piece of code creates the email entry box to which the user would enter their email address in order to
        # reactivate their membership with the centre.
        self.EmailBox = Entry(self, bd=5, font=("", 25))
        self.EmailBox.pack()

        # This block implements the 'Password:' label widget so that users of the system are aware of
        # the purpose of the entry box below.
        self.password_lbl = Label(self, text="\nPassword:", font=("", 25))
        self.password_lbl.pack()
        self.password_lbl.config(bg="#97c7f1")

        # This piece of code creates the email entry box to which the user would enter their email address in order to
        # reactivate their membership with the centre.
        self.PasswordBox = Entry(self, bd=5,font=("", 25), show="•")
        self.PasswordBox.pack()

        # This spacer creates a gap between the 'Password' entry box and the 'Submit' button.
        self.space1 = Label(self, text="", font=("", 46))
        self.space1.pack()
        self.space1.config(bg="#97c7f1")

        # This segment implements the 'Submit' button onto the 'Reactivate Membership' window. When the button is
        # pressed, the 'membership_reactivation' method is executed.
        self.reactivate_membership_photo = PhotoImage(file="Images/Reactivate Membership Submit Button.png")
        self.reactivate_button = Button(self, image=self.reactivate_membership_photo, command=self.membership_reactivation, height=90, width=725, borderwidth=0, activebackground="#97c7f1")
        self.reactivate_button.pack()
        self.reactivate_button.config(bg="#97c7f1")

        # This block creates a gap between the 'Submit' button and the 'answer' label.
        self.space2 = Label(self, text="", font=("", 36))
        self.space2.pack()
        self.space2.config(bg="#97c7f1")

        # This piece of code implements the 'answer' label, which is used to inform the user of the result from the
        # entered information they have inputted into the entry boxes.
        self.answer = Label(self, text="", font=("", 23))
        self.answer.pack()
        self.answer.config(bg="#97c7f1")

    # The 'membership_reactivation' method checks the database against the information entered into the entry boxes
    # by the user. If a match is found, the database updates the 'Status' of that user back to 'ACTIVE'. If no match
    # is found, the 'answer' label updates informing the user of the result via the interface.
    def membership_reactivation(self):
        connection.connect(user="root", password="")
        email = self.EmailBox.get()
        password = self.PasswordBox.get()
        query = "SELECT * FROM users WHERE Email = %s AND Password = %s;"
        cursor.execute(query, (email, password,))
        result = cursor.fetchall()
        if result:
            update = "UPDATE users SET Status = 'ACTIVE' WHERE Email = %s AND Password = %s;"
            cursor.execute(update, (email, password,))
            connection.commit()
            self.controller.show_frame("ThankYou")
            self.EmailBox.delete(0, 'end')
            self.PasswordBox.delete(0, 'end')
        else:
            self.answer.config(text="Credentials Not Found. Please Try Again.")

    # The 'back' method resets the 'answer' result and clears the inputted data into both 'Email' and 'Password' entry
    # boxes. The method then traverses the user back to the 'External Menu' page.
    def back(self):
        self.answer.config(text="")
        self.EmailBox.delete(0, 'end')
        self.PasswordBox.delete(0, 'end')
        self.EmailBox.focus_set()
        self.controller.show_frame("ExternalMenu")