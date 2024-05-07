from tkinter import *
from Database import *


class ViewMemberContents(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")
        self.controller = controller

        # Displays the 'Member Contents' banner.
        self.database_contents_photo = PhotoImage(file="Images/View Member Contents Title.png")
        self.database_contents_title = Label(self, image=self.database_contents_photo, height=80, width=742, borderwidth=0, activebackground="#97c7f1")
        self.database_contents_title.pack(anchor=E)
        self.database_contents_title.config(bg="#97c7f1")

        # This section implements a back button which allows the user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=lambda: controller.show_frame("Staff"),
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This spacer allows for a gap between the banner and the returned answer/s.
        self.spacer = Label(self, text="", font=("", 40))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This 'answer' label widget is used to output the returned Database contents to the staff associate via the graphical interface.
        self.answer = Label(self, text="", font=("", 7))
        self.answer.pack()
        self.answer.config(bg="#97c7f1")

        # This statement runs the 'view_content' method as soon as the 'ViewMemberContents' class is called.
        self.view_content()

    # The 'view_content' method has been created so staff associates can view all of the contents of the 'users' table
    # via the graphical interface.
    def view_content(self):
        connection.connect(user="root", password="")
        query = "SELECT * FROM users"
        cursor.execute(query)
        results = cursor.fetchall()
        text = ""
        for result in results:
            text = text + "\n\n" + str(result) + "\n"
        self.answer.config(text=text)
