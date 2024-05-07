from MainApp import *
from Live_Information import *
import webbrowser


class ExternalMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Configures the options menu window to have the selected background colour.
        self.config(bg="#97c7f1")

        # Displays the External Menu banner.
        self.external_menu_photo = PhotoImage(file="Images/External Menu.png")
        self.external_menu_title = Label(self, image=self.external_menu_photo, height=90, width=715, borderwidth=0, activebackground="#97c7f1")
        self.external_menu_title.pack(anchor=E)
        self.external_menu_title.config(bg="#97c7f1")

        # Allows for a gap between the title and the back button.
        self.spacer = Label(self, text="", font=("", 35))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This section implements a back button which allows a user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=lambda: controller.show_frame("Welcome"),
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This block implements the "Sign In" button to allow users to access the "Sign In" window.
        self.sign_in_photo = PhotoImage(file="Images/Sign In Button.png")
        self.sign_in_button = Button(self, image=self.sign_in_photo, command=lambda: controller.show_frame("SignIn"),
                        height=65, width=200, borderwidth=0, activebackground="#97c7f1")
        self.sign_in_button.pack()
        self.sign_in_button.config(bg="#97c7f1")

        # This segment allows for a space between the "Sign In" button and the "Join Crook Log Leisure Centre" button.
        self.spacer1 = Label(self, text="", font=("", 17))
        self.spacer1.pack()
        self.spacer1.config(bg="#97c7f1")

        # Implements "Join Crook Log Leisure Centre" button to the window.
        self.sign_up_photo = PhotoImage(file="Images/Sign Up Button.png")
        self.sign_up_button = Button(self, image=self.sign_up_photo, command=lambda: controller.show_frame("MemberSignUpPage"),
                        height=65, width=655, borderwidth=0, activebackground="#97c7f1")
        self.sign_up_button.pack()
        self.sign_up_button.config(bg="#97c7f1")

        # Allows for a space between the "Join Crook Log Leisure Centre" button and the "Live Information" button.
        self.spacer2 = Label(self, text="", font=("", 17))
        self.spacer2.pack()
        self.spacer2.config(bg="#97c7f1")

        # This segment allows for the implementation of the "Live Information" button to the menu window.
        self.live_information_photo = PhotoImage(file="Images/Live Information Button.png")
        self.live_information_button = Button(self, image=self.live_information_photo, command=lambda: controller.show_frame("LiveInformation"),
                        height=65, width=400, borderwidth=0, activebackground="#97c7f1")
        self.live_information_button.pack()
        self.live_information_button.config(bg="#97c7f1")

        # This spacer allows for a gap between the 'Live Information' button and the 'Website' button.
        self.spacer3 = Label(self, text="", font=("", 17))
        self.spacer3.pack()
        self.spacer3.config(bg="#97c7f1")

        # This segment implements the 'Website' button which allows users to access Crook Log's website.
        self.website_photo = PhotoImage(file="Images/Website Button.png")
        self.website_button = Button(self, image=self.website_photo, command=ExternalMenu.link, height=70, width=200, borderwidth=0, activebackground="#97c7f1")
        self.website_button.pack()
        self.website_button.config(bg="#97c7f1")

        # This spacer allows for a gap between the 'Website' button and the 'Reactivate Membership' button.
        self.spacer4 = Label(self, text="", font=("", 17))
        self.spacer4.pack()
        self.spacer4.config(bg="#97c7f1")

        # This block implements the "Reactivate Membership" button which allows the user to
        # redirect to the "Reactivate Membership" window.
        self.reactivate_membership_photo = PhotoImage(file="Images/Reactivate Membership Button.png")
        self.reactivate_membership_button = Button(self, image=self.reactivate_membership_photo, command=lambda: controller.show_frame("ReactivateMembership"),
                        height=65, width=600, borderwidth=0, activebackground="#97c7f1")
        self.reactivate_membership_button.pack()
        self.reactivate_membership_button.config(bg="#97c7f1")

    # This function executes Crook Log's website. It is only executed when a user presses the 'Website' button.
    def link():
        webbrowser.open('http://www.leisurecentre.com/crook-log-leisure-centre/TimeTable')

