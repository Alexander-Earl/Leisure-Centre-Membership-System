from tkinter import *
from Database import *


class SignIn(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")
        self.controller = controller

        # This spacer creates a gap between the top of the window and the 'Email:' label widget.
        self.spacer = Label(self, text="", font=("", 96))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This block implements the 'Sign In' banner on to the 'Sign In' window.
        self.sign_in_photo = PhotoImage(file="Images/Member Sign In.png")
        self.sign_in_title = Label(self, image=self.sign_in_photo, height=65, width=700, borderwidth=0,
                                   activebackground="#97c7f1")
        self.sign_in_title.place(x=30, y=12)
        self.sign_in_title.config(bg="#97c7f1")

        # This block implements a back button which allows a user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=self.back,
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This segment implements the 'Email:' label widget onto the 'Sign In' window.
        self.email_lbl = Label(self, text="Email:", font=("", 25))
        self.email_lbl.pack()
        self.email_lbl.config(bg="#97c7f1")

        # The two statements below create the 'Email' entry box which allows active members to input their email address
        # in order to prove their authenticity.
        self.EmailBox = Entry(self, bd=5, font=("", 25))
        self.EmailBox.pack()

        # This segment implements the 'Password:' label widget onto the 'Sign In' window.
        self.password_lbl = Label(self, text="\nPassword:", font=("", 25))
        self.password_lbl.pack()
        self.password_lbl.config(bg="#97c7f1")

        # The two statements below create the 'Password' entry box which allows active members to input their email
        # address in order to prove their authenticity.
        self.PasswordBox = Entry(self, bd=5,font=("", 25), show="*")
        self.PasswordBox.pack()

        # This spacer creates a gap between the 'Password' entry box and the 'Login' button.
        self.spacer1 = Label(self, text="", font=("", 56))
        self.spacer1.pack()
        self.spacer1.config(bg="#97c7f1")

        # This segment implements the 'Login' button which is pressed by the active member when they have inputted their
        # email and password credentials.
        self.login_photo = PhotoImage(file="Images/Login Button.png")
        self.login_button = Button(self, image=self.login_photo, command=self.login,
                        height=60, width=200, borderwidth=0, activebackground="#97c7f1")
        self.login_button.pack()
        self.login_button.config(bg="#97c7f1")

        # This spacer creates a gap between the 'Login' button and the 'answer' label.
        self.spacer2 = Label(self, text="", font=("", 46))
        self.spacer2.pack()
        self.spacer2.config(bg="#97c7f1")

        # This segment creates the 'answer' label widget, which is primarily used to inform the members of Crook Log
        # that they have entered wrong information into the 'Email' and 'Password' entry boxes.
        self.answer = Label(self, text="", font=("", 26))
        self.answer.pack()
        self.answer.config(bg="#97c7f1")

    # The 'login' method is executed when the 'Login' button is pressed by a user of the system. The method validates
    # the authenticity of the information inputted into both the 'Email' and 'Password' entry boxes and if the inputted
    # data matches the contents in the database, the user will be redirected to an internal menu appropriate for their
    # user level. If no match can be made, the user is notified through the use of the 'answer' label widget.
    def login(self):
        """Functionality that validates users' credentials for authenticity"""
        connection.connect(user="root", password="")
        email_get = self.EmailBox.get()
        password = self.PasswordBox.get()
        query = ("""SELECT * FROM users INNER JOIN user_roles ON users.User_ID = user_roles.User_ID 
        INNER JOIN role_types ON role_types.Role_Type_ID = user_roles.Role_Type_ID WHERE Email = %s AND Password = %s and Status = 'ACTIVE';""")
        cursor.execute(query, [email_get, password])
        result = cursor.fetchall()
        if result:
            role_type_id = result[0][15]
            query = "INSERT INTO logged_in_users (User_ID) VALUES (%s)"
            cursor.execute(query, [result[0][0], ])
            connection.commit()
            self.EmailBox.delete(0, 'end')
            self.PasswordBox.delete(0, 'end')
            self.EmailBox.focus_set()
            self.answer.config(text="")
            if role_type_id == 1:
                self.controller.show_frame("InternalMenu")
            if role_type_id == 2:
                self.controller.show_frame("Staff")
            if role_type_id == 3:
                self.controller.show_frame("Admin")
        else:
            connection.commit()
            self.answer.config(text="Credentials are incorrect.")
            connection.close()

    # The 'back' method clears any information inputted into both the 'Email' and 'Password' entry boxes as well as
    # removes any messages displayed to the user through the 'answer' label. The cursor is then placed back onto to the
    # 'Email' entry box and the user is traversed back to the 'External Menu'. This method is only executed when a user
    # presses the 'Back' button.
    def back(self):
        self.EmailBox.delete(0, 'end')
        self.PasswordBox.delete(0, 'end')
        self.EmailBox.focus_set()
        self.answer.config(text="")
        self.controller.show_frame("ExternalMenu")
