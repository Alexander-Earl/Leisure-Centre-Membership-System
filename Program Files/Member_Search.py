from tkinter import *
from MainApp import *
from Database import *


class MemberSearch(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Configures the window to have the selected background colour.
        self.config(bg="#97c7f1")
        self.controller = controller

        # This block implements the banner onto the window.
        self.member_search_photo = PhotoImage(file="Images/Member Search Title.png")
        self.member_search_title = Label(self, image=self.member_search_photo, height=80, width=725, borderwidth=0, activebackground="#97c7f1")
        self.member_search_title.pack()
        self.member_search_title.config(bg="#97c7f1")

        # This block implements a back button which allows a user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=self.back,
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This spacer allows for a gap between the 'Member Search' banner and the 'Last Name:' label widget.
        self.spacer = Label(self, text="", font=("", 25))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This segment implements the 'Last Name:' label widget.
        self.last_name = Label(self, text="Last Name:", font=("", 15))
        self.last_name.place(x=142, y=127)
        self.last_name.config(bg="#97c7f1")

        # This segment implements the entry box widget in which the staff associate will use to enter the last name
        # of the person they wish to find.
        self.search_entry = Entry(self, bd=5, font=("", 15))
        self.search_entry.pack()

        # This block implements the 'Search' button in which the staff member presses when they wish to check the
        # database for a result using the last name they have entered.
        # When this button is pressed, the 'last_name_db_search' method is executed.
        self.search_photo = PhotoImage(file="Images/Search Button.png")
        self.search_button = Button(self, image=self.search_photo, command=self.last_name_db_search,
                        height=47, width=120, borderwidth=0, activebackground="#97c7f1")
        self.search_button.place(x=493, y=117)
        self.search_button.config(bg="#97c7f1")

        # This spacer creates a gap between the entry box and the outputted result.
        self.spacer1 = Label(self, text="", font=("", 5))
        self.spacer1.pack()
        self.spacer1.config(bg="#97c7f1")

        # This label widget is created in order for the returned result to be outputted to the staff associate via the
        # graphical interface.
        self.answer = Label(self, text="", font=("", 14))
        self.answer.pack()
        self.answer.config(bg="#97c7f1")

    # When executed, the 'last_name_db_search' method connects to the MySQL Database and searches through its contents
    # within the 'users' table and attempts to find a last name match with what was entered into the entry box.
    def last_name_db_search(self):
        connection.connect(user="root", password="")
        search = self.search_entry.get()
        query = "SELECT * FROM users WHERE Last_Name = %s"
        cursor.execute(query, [search, ])
        connection.commit()
        result = cursor.fetchall()
        if result:
            for (Customer_ID, Title, First_Name, Last_Name, DOB, Email, Gender, Address, Post_Code, City,
                 Membership_Type, Password, Deleted) in result:
                self.answer.config(text="Customer ID: {} \n\nTitle: {}\n\nFirst Name: {} \n\nLast Name: {} \n\nDate Of Birth: {} \n\nEmail: {} \n\nGender: {} \n\nAddress: {} \
            \n\nPost Code: {} \n\nCity: {} \n\n Membership Type: {} \n\nPassword: {} \n\nStatus: {}".format(Customer_ID, Title, First_Name, Last_Name,
                                                                                   DOB,
                                                                                   Email, Gender, Address, Post_Code,
                                                                                   City, Membership_Type,
                                                                                   Password, Deleted))
                connection.close()
        else:
            self.answer.config(text="Last Name Not Found.")

    # The 'back' method clears the last name entry box and resets the answer label widget back to an empty string.
    # The method also then traverses the staff associate back to the 'Staff Menu' page.
    def back(self):
        self.search_entry.delete(0, 'end')
        self.answer.config(text="")
        self.controller.show_frame("Staff")