from tkinter import *
from MainApp import *
from Database import *


class MemberAnonymise(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Configures the window to have the selected background colour.
        self.config(bg="#97c7f1")

        # This block implements the 'Member Anonymise' banner onto the window.
        self.member_anonymise_photo = PhotoImage(file="Images/Member Anonymise Title.png")
        self.member_anonymise_banner = Label(self, image=self.member_anonymise_photo, height=90, width=725, borderwidth=0, activebackground="#97c7f1")
        self.member_anonymise_banner.pack()
        self.member_anonymise_banner.config(bg="#97c7f1")

        # This block implements a back button which allows a user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=lambda: controller.show_frame("Admin"),
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This spacer creates a gap between the 'Member Anonymise' banner and then 'User ID' label & entry box.
        self.spacer = Label(self, text="", font=("", 46))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This segment of code creates a label widget next to the entry box so the Administrator is aware of the purpose
        # of the entry box.
        self.user_id_label = Label(self, text="User ID:", font=("", 20))
        self.user_id_label.place(x=215, y=165)
        self.user_id_label.config(bg="#97c7f1")

        # This creates the Entry box widget in which the Administrator inputs the User ID of the ex-member he wishes
        # to anonymise in the database.
        self.user_id_entry = Entry(self, bd=2, width=5, font=("", 20))
        self.user_id_entry.pack()

        # This spacer creates a gap between the entry box and the 'Submit' button
        self.spacer1 = Label(self, text="", font=("", 15))
        self.spacer1.pack()
        self.spacer1.config(bg="#97c7f1")

        self.submit_photo = PhotoImage(file="Images/Member Anonymise Submit Button.png")
        self.submit_button = Button(self, image=self.submit_photo, command=self.member_anonymise,
                        height=70, width=140, borderwidth=0, activebackground="#97c7f1")
        self.submit_button.pack()
        self.submit_button.config(bg="#97c7f1")

        # This spacer creates a space between the 'Submit' button and the 'answer' label widget.
        self.spacer2 = Label(self, text="", font=("", 15))
        self.spacer2.pack()
        self.spacer2.config(bg="#97c7f1")

        # This label widget is used to inform the Administrator of the final outcome when they anonymise an ex-member.
        self.answer = Label(self, text="", font=("", 20))
        self.answer.pack()
        self.answer.config(bg="#97c7f1")

    # The 'member_anonymise' method is executed when the Administrator presses the 'Submit' button.
    def member_anonymise(self):
        connection.connect(user="root", password="")
        id = self.user_id_entry.get()
        query = "SELECT User_ID from users WHERE User_ID = %s AND Status = 'INACTIVE';"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        if result:
            query = ("UPDATE users SET First_Name = 'x', Last_Name = 'x', DOB = 0001-01-01, Email = 'x', Gender = 'x', Address = 'x', Post_Code = 'x', City = 'x', Membership_Type = 'x', Password = 'x' WHERE User_ID = %s;")
            cursor.execute(query, (result[0][0],))
            connection.commit()
            self.answer.config(text="Entry UPDATED.")
            connection.close()
        else:
            self.answer.config(text="User_ID Not Found or Status is ACTIVE.")
            connection.close()
