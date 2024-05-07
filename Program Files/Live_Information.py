from MainApp import *
from tkinter import *
from Database import *


class LiveInformation(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self)
        # Sets the background colour to the hexadecimal value.
        self.config(bg="#97c7f1")
        self.controller = controller

        # This spacer allows for a gap between the 'Live Information' banner and the live swimming count label widget.
        self.spacer = Label(self, text="", font=("", 125))
        self.spacer.pack()
        self.spacer.config(bg="#97c7f1")

        # This segment implements the 'Live Information' banner onto the window.
        self.live_information_photo = PhotoImage(file="Images/Live Information.png")
        self.live_information_title = Label(self, image=self.live_information_photo, height=55, width=700, borderwidth=0,
                                   activebackground="#97c7f1")
        self.live_information_title.place(x=30, y=12)
        self.live_information_title.config(bg="#97c7f1")

        # This block implements a back button which allows a user to traverse to the previous window.
        self.back_photo = PhotoImage(file="Images/Back Button.png")
        self.back_button = Button(self, image=self.back_photo, command=lambda: controller.show_frame("ExternalMenu"),
                        height=70, width=120, borderwidth=0, activebackground="#97c7f1")
        self.back_button.place(x=-19, y=85)
        self.back_button.config(bg="#97c7f1")

        # This label widget is created so users of the system are aware of the meaning behind the outputted live count
        # of the number of members utilising the swimming facilities.
        self.swimming_label = Label(self, text="Number of Individuals Swimming:", font=("", 30))
        self.swimming_label.pack()
        self.swimming_label.config(bg="#97c7f1")

        # This block creates a label widget which is used to inform the users of the system on
        # the amount of members currently using the Swimming Pool facilities.
        self.live_swimming_count = Label(self, text="0", font=("", 45, "bold italic"))
        self.live_swimming_count.place(x=670, y=180)
        self.live_swimming_count.config(bg="#97c7f1")

        # This spacer creates a gap between the 'Number of Individuals Swimming:' label and the
        # 'Number of Individuals Using the Gym:' label.
        self.space1 = Label(self, text="", font=("", 25))
        self.space1.pack()
        self.space1.config(bg="#97c7f1")

        # This label widget is created so users of the system are aware of the meaning behind the outputted live count
        # of the number of members utilising the gym facilities.
        self.gym_label = Label(self, text="Number of Individuals Using the Gym:", font=("", 30))
        self.gym_label.pack()
        self.gym_label.config(bg="#97c7f1")

        # This block creates a label widget which is used to inform the users of the system on
        # the amount of members currently using the gym facilities.
        self.live_gym_count = Label(self, text="0", font=("", 45, "bold italic"))
        self.live_gym_count.place(x=705, y=275)
        self.live_gym_count.config(bg="#97c7f1")

        # This statement executes the 'swimming_count' method so users of the system are aware of the
        # current number of individuals using the swimming facilities.
        self.swimming_count()

        # This statement executes the 'gym_count' method so users of the system are aware of the current number of
        # individuals using the gym facilities.
        self.gym_count()

    # The 'swimming_count' method calculates the current amount of active members using the swimming facilities in a
    # real-time manner. It then outputs the answer to the users through the use of the label widget.
    def swimming_count(self):
        connection.connect(user="root", password="")
        query = "SELECT COUNT(1) - COUNT(Exit_Time) FROM live_session WHERE Activity_Type = 'Swimming';"
        cursor.execute(query)
        result = cursor.fetchall()
        count = 0
        connection.commit()
        if result != count:
            count = result
            self.live_swimming_count.config(text=result)
        self.live_swimming_count.after(200, self.swimming_count)
        connection.close()

    # The 'gym_count' method calculates the current amount of active members using the gym facilities in a
    # real-time manner. It then outputs the answer to the users through the use of the label widget.
    def gym_count(self):
        connection.connect(user="root", password="")
        query = "SELECT COUNT(1) - COUNT(Exit_Time) FROM live_session WHERE Activity_Type = 'Gym';"
        cursor.execute(query)
        result = cursor.fetchall()
        count = 0
        connection.commit()
        if result != count:
            count = result
            self.live_gym_count.config(text=result)
        self.live_gym_count.after(200, self.gym_count)
        connection.close()

