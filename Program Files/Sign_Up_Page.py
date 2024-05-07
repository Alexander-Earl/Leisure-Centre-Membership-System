from tkinter import *
from User import *
from Database import *
from MainApp import *
import tkinter.messagebox


class SignUpPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        self.controller = controller
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")

        # This section implements a back button which allows the user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=self.back,
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This spacer creates a gap between the top of the window and the 'Title' field on the sign up form.
        self.spacer = Label(self, text="", font=("", 80))
        self.spacer.grid(row=0, column=0, sticky=E)
        self.spacer.config(bg="#97c7f1")

        # This segment implements the 'Sign Up to Crook Log' banner onto the window.
        self.sign_up_photo = PhotoImage(file=self.file)
        self.sign_up_title = Label(self, image=self.sign_up_photo, height=65, width=700, borderwidth=0,
                                   activebackground="#97c7f1")
        self.sign_up_title.place(x=30, y=12)
        self.sign_up_title.config(bg="#97c7f1")

        # This block implements the 'Title' label widget and aligns it to the left of the 'Title' drop down box.
        self.title_lbl = Label(self, text="Title:", font=("", 20))
        self.title_lbl.grid(row=1, column=0, sticky=E)
        self.title_lbl.config(bg="#97c7f1")

        # This block of code creates a list of all the possible titles for the 'Title' drop down box. It also sets the
        # default 'Title' value to null and places the menu into the grid.
        self.title_list = ["Mr", "Miss", "Mrs", "Ms", "Dr"]
        self.selected_title = StringVar()
        self.selected_title.set("")
        self.title_options = OptionMenu(self, self.selected_title, *self.title_list)
        self.title_options.grid(row=1, column=1, sticky=W)
        self.title_options.config(font=("", 15), width=5, borderwidth=0, bg="white", activebackground="white")

        # This block implements the first name entry box widget as well as the 'First Name:' label widget which is then
        # aligned to the left of the entry box.
        self.first_name_lbl = Label(self, text="First Name:", font=("", 20))
        self.first_name_lbl.grid(row=2, column=0, sticky=E)
        self.first_name_lbl.config(bg="#97c7f1")
        self.First_Name_Box = Entry(self, font=("", 20))
        self.First_Name_Box.grid(row=2, column=1, sticky=W)

        # This block implements the last name entry box widget as well as the 'Last Name:' label widget which is then
        # aligned to the left of the entry box.
        self.last_name_lbl = Label(self, text="Last Name:", font=("", 20))
        self.last_name_lbl.grid(row=3, sticky=E)
        self.last_name_lbl.config(bg="#97c7f1")
        self.Last_Name_Box = Entry(self, font=("", 20))
        self.Last_Name_Box.grid(row=3, column=1, sticky=W)

        # This block implements the 'Date of Birth' label widget and aligns it to the left of the 'Date' option menu.
        self.dob_year_lbl = Label(self, text="Date of Birth:", font=("", 20))
        self.dob_year_lbl.grid(row=4, sticky=E)
        self.dob_year_lbl.config(bg="#97c7f1")

        # This block creates the 'Date' option menu which contains all of the possible dates that a user could have been
        # born (1st-31st). The dates are stored within the list and displayed to the user via the option menu.
        self.date_list = []
        self.selected_date = StringVar()
        for date in range(1, 32):
            self.date_list.append("%s" % date)
        self.selected_date.set("Date")
        self.date_menu = OptionMenu(self, self.selected_date, *self.date_list)
        self.date_menu.place(x=315, y=240)
        self.date_menu.config(font=("", 15), width=3, borderwidth=0, bg="white", activebackground="white")

        # This segment implements a forward slash between the 'Date' option menu and the 'Month' option menu.
        self.dash = Label(self, text="/", font=("", 26))
        self.dash.place(x=390, y=238)
        self.dash.config(bg="#97c7f1")

        # This block creates the 'Month' option menu which contains all of the possible months that a user could have
        # been born (01-12). The months are stored within the list and displayed to the user via the option menu.
        self.month_list = []
        self.selected_month = StringVar()
        for month in range(1, 13):
            self.month_list.append("%s" % month)
        self.selected_month.set("Month")
        self.month_menu = OptionMenu(self, self.selected_month, *self.month_list)
        self.month_menu.place(x=409, y=240)
        self.month_menu.config(font=("", 15), width=4, borderwidth=0, bg="white", activebackground="white")

        # This segment implements a forward slash between the 'Month' option menu and the 'Year' option menu.
        self.dash1 = Label(self, text="/", font=("", 26))
        self.dash1.place(x=496, y=238)
        self.dash1.config(bg="#97c7f1")

        # This block creates the 'Year' option menu which contains all of the possible years that a user could have
        # been born (1935-2019). The years are stored within the list and displayed to the user via the option menu.
        self.year_list = []
        self.selected_year = StringVar()
        for year in range(1935, 2019):
            self.year_list.append("%s" % year)
        self.selected_year.set("Year")
        self.year_menu = OptionMenu(self, self.selected_year, *self.year_list)
        self.year_menu.place(x=515, y=240)
        self.year_menu.config(font=("", 15), width=4, borderwidth=0, bg="white", activebackground="white")

        # This module implements the 'Email:' label widget as well as the email entry box onto the sign up page.
        self.email_lbl = Label(self, text="Email:", font=("", 20))
        self.email_lbl.grid(row=7, stick=E)
        self.email_lbl.config(bg="#97c7f1")
        self.Email_Box = Entry(self, font=("", 20))
        self.Email_Box.grid(row=7, column=1, sticky=W)
        self.Email_Box.config(width=15)

        # This segment implements the 'Gender:' label widget which aligns next to the 'Gender' option menu.
        self.gender_lbl = Label(self, text="Gender:", font=("", 20))
        self.gender_lbl.grid(row=8, sticky=E)
        self.gender_lbl.config(bg="#97c7f1")

        # This module creates a list called 'gender_list' which stores both the 'Male' and 'Female' gender choices for
        # the users of the system to select from. This segment also creates the option menu which allows the user to
        # choose their selected gender via the graphical interface.
        self.gender_list = ["Male", "Female"]
        self.selected_gender = StringVar()
        self.selected_gender.set("")
        self.gender_menu = OptionMenu(self, self.selected_gender, *self.gender_list)
        self.gender_menu.grid(row=8, column=1, sticky=W)
        self.gender_menu.config(font=("", 15), width=6, borderwidth=0, bg="white", activebackground="white")

        # This module implements the 'Address:' label widget as well as the address entry box onto the sign up page.
        self.address_lbl = Label(self, text="Address:", font=("", 20))
        self.address_lbl.grid(row=9, sticky=E)
        self.address_lbl.config(bg="#97c7f1")
        self.Address_Box = Entry(self, font=("", 20))
        self.Address_Box.grid(row=9, column=1, sticky=W)
        self.Address_Box.config(width=12)

        # This module implements the 'Post Code:' label widget as well as the post code entry box onto the sign up page.
        self.post_code_lbl = Label(self, text="Post Code:", font=("", 20))
        self.post_code_lbl.grid(row=10, sticky=E)
        self.post_code_lbl.config(bg="#97c7f1")
        self.Post_Code_Box = Entry(self, font=("", 20))
        self.Post_Code_Box.grid(row=10, column=1, sticky=W)
        self.Post_Code_Box.config(width=8)

        # This module implements the 'City:' label widget as well as the city entry box onto the sign up page.
        self.city_lbl = Label(self, text="City:", font=("", 20))
        self.city_lbl.grid(row=11, sticky=E)
        self.city_lbl.config(bg="#97c7f1")
        self.City_Box = Entry(self, font=("", 20))
        self.City_Box.grid(row=11, column=1, sticky=W)
        self.City_Box.config(width=11)

        # This module implements the 'Password:' label widget as well as the password entry box onto the sign up page.
        self.password_lbl = Label(self, text="Password:", font=("", 20))
        self.password_lbl.grid(row=12, sticky=E)
        self.password_lbl.config(bg="#97c7f1")
        self.Password_Box = Entry(self, show="•", width=17, font=("", 20))
        self.Password_Box.grid(row=12, column=1, sticky=W)

        # This module implements the 'Confirm Password:' label widget as well as the password confirmation entry box.
        self.password_confirmation_lbl = Label(self, text="Confirm Password:", font=("", 20))
        self.password_confirmation_lbl.grid(row=13, sticky=E)
        self.password_confirmation_lbl.config(bg="#97c7f1")
        self.Password_Confirmation_Box = Entry(self, show="•", width=17, font=("", 20))
        self.Password_Confirmation_Box.grid(row=13, column=1, sticky=W)

        # This segment implements the 'Membership Option:' label widget and aligns it next to the membership option menu
        self.membership_option_label = Label(self, text="        Membership Option:", font=("", 20))
        self.membership_option_label.grid(row=14, sticky=E)
        self.membership_option_label.config(bg="#97c7f1")

        # This module creates the 'membership_list' which contains both types of membership options 'Gym' and 'Swim23'.
        # The segment also creates the membership option menu which allows the user to choose their membership option
        # via the graphical interface.
        self.membership_list = ["Gym", "Swim23"]
        self.selected_membership = StringVar()
        self.selected_membership.set("")
        self.membership_menu = OptionMenu(self, self.selected_membership, *self.membership_list)
        self.membership_menu.grid(row=14, column=1, sticky=W)
        self.membership_menu.config(font=("", 15), width=6, borderwidth=0, bg="white", activebackground="white")

        # This segment of code implements the 'Submit' button to the sign up page.
        # When the button is pressed, the 'submit_validation' method is executed in order to validate the inputted data.
        self.submit_photo = PhotoImage(file="Images/Submit Button.png")
        self.submit_button = Button(self, image=self.submit_photo, command=self.submit_validation,
                        height=60, width=200, borderwidth=0, activebackground="#97c7f1")
        self.submit_button.place(x=260, y=630)
        self.submit_button.config(bg="#97c7f1")

        # This label widget is implemented within the window in order to inform the users of any mistakes they may make
        # when completing the sign up form.
        self.validation_label = Label(self, text="", fg="red", font=("", 18, "bold italic"))
        self.validation_label.place(x=217, y=592)
        self.validation_label.config(bg="#97c7f1")

    # The 'back' method clears all of the completed fields on the sign up form and resets the 'validation_label'.
    # The method then traverses the user back to the 'External Menu' page. This method is only executed when the user
    # presses the back button and when executed. The method also contains a pop-up window informing users that
    # traversing back to the 'External Menu' will delete all of their inputted information.
    def back(self):
        result = tkinter.messagebox.askquestion("Crook Log Leisure Centre", "Are you sure?\nGoing back to the main menu "
                                                                            "will reset the form.", icon='warning')
        if result == 'yes':
            self.controller.show_frame(self.page)
            self.clear()

    # The 'clear' method resets all of the entry boxes back to their default value, blank.
    def clear(self):
        self.selected_title.set("")
        self.First_Name_Box.delete(0, 'end')
        self.Last_Name_Box.delete(0, 'end')
        self.selected_year.set("Year")
        self.selected_date.set("Date")
        self.selected_month.set("Month")
        self.Email_Box.delete(0, 'end')
        self.selected_gender.set("")
        self.Address_Box.delete(0, 'end')
        self.Post_Code_Box.delete(0, 'end')
        self.City_Box.delete(0, 'end')
        self.Password_Box.delete(0, 'end')
        self.Password_Confirmation_Box.delete(0, 'end')
        self.selected_membership.set("")
        self.First_Name_Box.focus_set()
        self.validation_label.config(text="")

    # The 'submit_validation' method validates all of the data inputted into the form by the user. The method carries
    # out an array of checks on the data such as; making sure all fields have been completed, verifying that the email
    # address given is not already in use at the centre as well as making sure that the inputted password matches the
    # 'confirmation password' in order to eliminate the possibility of the user making a typographical error.
    def submit_validation(self):
        """"Method that validates all entry box information"""
        title = self.selected_title.get()
        first_name = self.First_Name_Box.get()
        last_name = self.Last_Name_Box.get()
        dob_year = self.selected_year.get()
        dob_month = self.selected_month.get()
        dob_date = self.selected_date.get()
        email = self.Email_Box.get()
        gender = self.selected_gender.get()
        address = self.Address_Box.get()
        post_code = self.Post_Code_Box.get()
        city = self.City_Box.get()
        membership_type = self.selected_membership.get()
        password = self.Password_Box.get()

        entries = [title, first_name, last_name, dob_year, dob_month, dob_date, email, gender, address, post_code, city, membership_type, password]

        error = False
        for entry in entries:
            pass
            if not entry[0:]:
                self.validation_label.config(text="Not All Fields Are Completed.")
                error = True
                break

        if error is False:
            email = self.Email_Box.get()
            connection.connect(user="root", password="")
            query = "SELECT * FROM users WHERE Email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchall()
            if result:
                self.validation_label.config(text="This Email is Already in Use.")
            else:
                self.validation_label.config(text="")
                if dob_date == "Date":
                    self.validation_label.config(text="Please Enter DOB Date")

                elif dob_month == "Month":
                    self.validation_label.config(text="Please Enter DOB Month")

                elif dob_year == "Year":
                    self.validation_label.config(text="Please Enter DOB Year")
                else:
                    password = self.Password_Box.get()
                    confirm_password = self.Password_Confirmation_Box.get()
                    if password == confirm_password:
                        user = User(title, first_name, last_name, int(dob_year), int(dob_month), int(dob_date), email,
                                        gender, address, post_code, city, membership_type, password)
                        id = User.db_user_write(user)
                        User.db_user_role_write(id, self.role_type_id)
                        self.clear()
                        self.controller.show_frame("ThankYou")

                    else:
                        self.validation_label.config(text="Passwords do not match.")


class MemberSignUpPage(SignUpPage):
    def __init__(self, parent, controller):
        self.file = "Images/Sign Up to Crook Log.png"
        self.role_type_id = 1
        self.page = "ExternalMenu"
        SignUpPage.__init__(self, parent, controller)


class StaffSignUpPage(SignUpPage):
    def __init__(self, parent, controller):
        self.file = "Images/Staff Sign Up Form Title.png"
        self.role_type_id = 2
        self.page = "Admin"
        SignUpPage.__init__(self, parent, controller)
