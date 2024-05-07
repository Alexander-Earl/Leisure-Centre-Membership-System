from tkinter import *
from SignIn import *
import webbrowser


class InternalMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        self.controller = controller
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")

        # This segment implements the 'Member Menu' banner.
        self.member_photo = PhotoImage(file="Images/Member Menu.png")
        self.member_menu_title = Label(self, image=self.member_photo, height=90, width=725, borderwidth=0, activebackground="#97c7f1")
        self.member_menu_title.pack(anchor=E)
        self.member_menu_title.config(bg="#97c7f1")

        # 'Sign Out' button which allows members of Crook Log to sign out of the system when they so desire.
        self.sign_out_photo = PhotoImage(file="Images/Sign Out Button.png")
        self.sign_out_button = Button(self, image=self.sign_out_photo, command=self.sign_out,
                        height=50, width=165, borderwidth=0, activebackground="#97c7f1")
        self.sign_out_button.place(x=563, y=77)
        self.sign_out_button.config(bg="#97c7f1")

        # Allows for a gap between the 'Member Menu' banner and the 'Gym' button.
        self.spacer = Label(self, text="", font=("", 35))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # 'Use the Gym' button which allows members of Crook Log to access the gym facilities.
        self.gym_photo = PhotoImage(file="Images/Gym Button.png")
        self.gym_button = Button(self, image=self.gym_photo,
                                                 command=self.gym, height=70, width=275,
                                                 borderwidth=0, activebackground="#97c7f1")
        self.gym_button.pack()
        self.gym_button.config(bg="#97c7f1")

        # This spacer provides a gap between the 'Use the Gym' button and the 'Use the Swimming Pool' button.
        self.spacer1 = Label(self, text="")
        self.spacer1.pack()
        self.spacer1.config(bg="#97c7f1")

        # 'Use the Swimming Pool' button so members can access the swimming pool if they so desire.
        self.swimming_photo = PhotoImage(file="Images/Swimming Button.png")
        self.swimming_button = Button(self, image=self.swimming_photo,
                                                 command=self.swimming, height=70, width=500,
                                                 borderwidth=0, activebackground="#97c7f1")
        self.swimming_button.pack()
        self.swimming_button.config(bg="#97c7f1")

        # This spacer provides a gap between the 'Use the Swimming Pool' button and the 'Leave the Centre' button.
        self.spacer2 = Label(self, text="")
        self.spacer2.pack()
        self.spacer2.config(bg="#97c7f1")

        # This button allows members to exit the facility once they have finished their workout session at Crook Log.
        self.exit_photo = PhotoImage(file="Images/Exit Centre Button.png")
        self.exit_button = Button(self, image=self.exit_photo,
                                                 command=self.exit_centre, height=70, width=450,
                                                 borderwidth=0, activebackground="#97c7f1")
        self.exit_button.pack()
        self.exit_button.config(bg="#97c7f1")

        # This spacer allows for a gap between the 'Website' button and the 'Cancel Subscription' button.
        self.spacer3 = Label(self, text="")
        self.spacer3.pack()
        self.spacer3.config(bg="#97c7f1")

        # This segment implements the 'Website' button which allows signed in members to access Crook Log's website.
        self.website_photo = PhotoImage(file="Images/Website Button.png")
        self.website_button = Button(self, image=self.website_photo, command=InternalMenu.link, height=70, width=200, borderwidth=0, activebackground="#97c7f1")
        self.website_button.pack()
        self.website_button.config(bg="#97c7f1")

        # Spacer that allows for a gap between the 'Website' button and the 'Cancel Subscription' button.
        self.spacer4 = Label(self, text="")
        self.spacer4.pack()
        self.spacer4.config(bg="#97c7f1")

        # The 'Cancel Subscription' button when pressed redirects members to the 'Cancel Subscription' page.
        self.cancel_subscription_photo = PhotoImage(file="Images/Cancel Subscription Button.png")
        self.cancel_subscription_button = Button(self, image=self.cancel_subscription_photo,
                                                 command=lambda: controller.show_frame("Cancel"), height=70, width=450,
                                                 borderwidth=0, activebackground="#97c7f1")
        self.cancel_subscription_button.pack()
        self.cancel_subscription_button.config(bg="#97c7f1")

    # The 'gym' method is executed when a member presses the 'Use the Gym' button.
    # Once the button is clicked, the methods then signs the member out of the system and redirects them back
    # to the 'Welcome' page.
    def gym(self):
        connection.connect(user="root", password="")
        query = ("SELECT User_ID FROM logged_in_users WHERE Logged_Out_Time IS NULL;")
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            query1 = "INSERT INTO live_session (User_ID, Entry_Time, Activity_Type) VALUES (%s, CURRENT_TIMESTAMP, 'Gym');"
            cursor.execute(query1, [result[0][0],])
            connection.commit()
            connection.close()
            self.sign_out()

    # The 'swimming' method is executed when a member presses the 'Use the Swimming Pool' button.
    # The method then signs the logged in member out of the system and redirects them back to the 'Welcome' page.
    def swimming(self):
        connection.connect(user="root", password="")
        query = ("SELECT User_ID FROM logged_in_users WHERE Logged_Out_Time IS NULL;")
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            query1 = "INSERT INTO live_session (User_ID, Entry_Time, Activity_Type) VALUES (%s, CURRENT_TIMESTAMP, 'Swimming');"
            cursor.execute(query1, [result[0][0],])
            connection.commit()
            connection.close()
            self.sign_out()

    # The 'sign_out' method is executed when a member presses the 'Sign Out' button, due to them desiring to log out
    # of the system.
    def sign_out(self):
        connection.connect(user="root", password="")
        query = "UPDATE logged_in_users SET Logged_Out_Time = CURRENT_TIMESTAMP WHERE Logged_Out_Time is NULL;"
        cursor.execute(query)
        connection.commit()
        connection.close()
        self.controller.show_frame("ThankYou")

    # The 'exit_centre' method is executed when a member presses the 'Leave the Centre' button.
    def exit_centre(self):
        connection.connect(user="root", password="")
        query = ("SELECT User_ID FROM logged_in_users WHERE Logged_Out_Time IS NULL;")
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            query1 = "UPDATE live_session SET Exit_Time = CURRENT_TIMESTAMP WHERE User_ID = %s;"
            cursor.execute(query1, [result[0][0],])
            connection.commit()
            connection.close()
            self.sign_out()

    # The 'link' function is executed when a logged in member presses the 'Website' button.
    def link():
        webbrowser.open('http://www.leisurecentre.com/crook-log-leisure-centre/TimeTable')