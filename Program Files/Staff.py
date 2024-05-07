from tkinter import *
from Database import *
from ViewMemberContents import *
from Sign_Up_Page import *


class Staff(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self)
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")
        self.controller = controller

        # This segment implements the 'Staff Menu' banner onto the 'Staff' window.
        self.staff_photo = PhotoImage(file="Images/Staff Menu.png")
        self.staff_menu_title = Label(self, image=self.staff_photo, height=80, width=725, borderwidth=0, activebackground="#97c7f1")
        self.staff_menu_title.pack(anchor=E)
        self.staff_menu_title.config(bg="#97c7f1")

        # 'Sign Out' button so the Administrator can log out of the system efficiently.
        self.sign_out_photo = PhotoImage(file="Images/Sign Out Button.png")
        self.sign_out_button = Button(self, image=self.sign_out_photo, command=self.sign_out,
                        height=50, width=165, borderwidth=0, activebackground="#97c7f1")
        self.sign_out_button.place(x=563, y=80)
        self.sign_out_button.config(bg="#97c7f1")

        # This spacer creates a gap between the 'Staff Menu' banner and the 'Search for a Member' button.
        self.spacer = Label(self, text="", font=("", 35))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This segment implements the 'Search for a Member' button. When pressed, the system redirects the staff member
        # to the 'Member Search' page.
        self.member_search_photo = PhotoImage(file="Images/Search for Member Button.png")
        self.member_search_button = Button(self, image=self.member_search_photo, command=lambda: controller.show_frame("MemberSearch"),
                        height=75, width=355, borderwidth=0, activebackground="#97c7f1")
        self.member_search_button.pack()
        self.member_search_button.config(bg="#97c7f1")

        # This segment implements the 'View Member Contents' button. When pressed, the system redirects the staff member
        # to the 'View Member Contents' page.
        self.database_contents_photo = PhotoImage(file="Images/View Member Contents Button.png")
        self.database_contents_button = Button(self, image=self.database_contents_photo, command=lambda: controller.show_frame("ViewMemberContents"),
                        height=75, width=450, borderwidth=0, activebackground="#97c7f1")
        self.database_contents_button.pack()
        self.database_contents_button.config(bg="#97c7f1")

        # This segment implements the 'Generate Member Report' button. When pressed, the system redirects the staff
        # member to the 'Report' page.
        self.member_report_photo = PhotoImage(file="Images/Generate Member Report Button.png")
        self.member_report_button = Button(self, image=self.member_report_photo, command=lambda: controller.show_frame("Report"),
                        height=75, width=450, borderwidth=0, activebackground="#97c7f1")
        self.member_report_button.pack()
        self.member_report_button.config(bg="#97c7f1")

    # The 'sign_out' method is executed when a staff associate presses the 'Sign Out' button. When pressed, the method
    # will redirect the staff member back to the 'Welcome' page.
    def sign_out(self):
        connection.connect(user="root", password="")
        query = "UPDATE logged_in_users SET Logged_Out_Time = CURRENT_TIMESTAMP WHERE Logged_Out_Time is NULL;"
        cursor.execute(query)
        connection.commit()
        connection.close()
        self.controller.show_frame("ThankYou")
