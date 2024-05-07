from tkinter import *
from Report import *


class Admin(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        self.controller = controller
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")

        # This segment of code implements the 'Administrator Menu' banner onto the window.
        self.admin_photo = PhotoImage(file="Images/Administrator Menu.png")
        self.admin_menu_title = Label(self, image=self.admin_photo, height=80, width=725, borderwidth=0, activebackground="#97c7f1")
        self.admin_menu_title.pack()
        self.admin_menu_title.config(bg="#97c7f1")

        # 'Sign Out' button so the Administrator can log out of the system efficiently.
        self.sign_out_photo = PhotoImage(file="Images/Sign Out Button.png")
        self.sign_out_button = Button(self, image=self.sign_out_photo, command=self.sign_out,
                        height=50, width=165, borderwidth=0, activebackground="#97c7f1")
        self.sign_out_button.place(x=563, y=80)
        self.sign_out_button.config(bg="#97c7f1")

        # Spacer so there is a gap between the Administrator banner and the buttons.
        self.spacer = Label(self, text="", font=("", 35))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # "Member Anonymise" button to allow the Administrator access the "Member Anonymise" window.
        self.member_anonymise_photo = PhotoImage(file="Images/Member Anonymise Button.png")
        self.member_anonymise_button = Button(self, image=self.member_anonymise_photo, command=lambda: controller.show_frame("MemberAnonymise"),
                        height=75, width=400, borderwidth=0, activebackground="#97c7f1")
        self.member_anonymise_button.pack()
        self.member_anonymise_button.config(bg="#97c7f1")

        # "Emergency Report" button to allow the Administrator to generate an 'Emergency Report'.
        self.emergency_photo = PhotoImage(file="Images/Emergency Report Button.png")
        self.emergency_report_button = Button(self, image=self.emergency_photo, command=Report.emergency_report,
                        height=75, width=400, borderwidth=0, activebackground="#97c7f1")
        self.emergency_report_button.pack()
        self.emergency_report_button.config(bg="#97c7f1")

        # "Staff Sign Up" button to allow the Administrator to access the 'Staff Sign Up' window.
        self.staff_photo = PhotoImage(file="Images/Staff Sign Up Form Button.png")
        self.staff_signup_button = Button(self, image=self.staff_photo, command=lambda: controller.show_frame("StaffSignUpPage"),
                        height=75, width=400, borderwidth=0, activebackground="#97c7f1")
        self.staff_signup_button.pack()
        self.staff_signup_button.config(bg="#97c7f1")

        # "Executive Report" button to allow the Administrator to generate an 'Executive Report'.
        self.executive_photo = PhotoImage(file="Images/Generate Executive Report Button.png")
        self.executive_report_button = Button(self, image=self.executive_photo, command=Report.executive_report,
                        height=75, width=550, borderwidth=0, activebackground="#97c7f1")
        self.executive_report_button.pack()
        self.executive_report_button.config(bg="#97c7f1")

    # This method is executed when an Administrator desires to sign out of the system
    # through clicking the 'Sign Out' button.
    def sign_out(self):
        connection.connect(user="root", password="")
        query = "UPDATE logged_in_users SET Logged_Out_Time = CURRENT_TIMESTAMP WHERE Logged_Out_Time is NULL;"
        cursor.execute(query)
        connection.commit()
        connection.close()
        self.controller.show_frame("ThankYou")