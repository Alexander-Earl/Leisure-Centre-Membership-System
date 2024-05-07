######################################################
# AQA A-Level Computer Science - Non-Exam Assessment #
# Centre Name - Haberdashers Aske's Crayford Academy #
# Centre Number - 14114                              #
# Title - Crook Log Leisure Centre Membership System #
# Programmer - Alexander Earl                        #
# Candidate Number - 2047                            #
######################################################

from SignIn import *
from External_Menu import *
from Sign_Up_Page import *
from Internal_Menu import *
from Spacer import *
from Staff import *
from Report import *
from WelcomePage import *
from Admin import *
from Live_Information import *
from Cancel import *
from ViewMemberContents import *
from Thank_You import *
from ReactivateMembership import *
from Member_Anonymise import *
from Member_Search import *


class App(Frame):

    def __init__(self):
        root = Tk()
        root.title("Crook Log Leisure Centre")
        root.state('zoomed')
        root.config(bg="#97c7f1")
        root.attributes("-fullscreen", True)

        Frame.__init__(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["Spacer"] = Spacer(parent=container, controller=self)
        self.frames["Welcome"] = Welcome(parent=container, controller=self)
        self.frames["ExternalMenu"] = ExternalMenu(parent=container, controller=self)
        self.frames["MemberSignUpPage"] = MemberSignUpPage(parent=container, controller=self)
        self.frames["SignIn"] = SignIn(parent=container, controller=self)
        self.frames["InternalMenu"] = InternalMenu(parent=container, controller=self)
        self.frames["Staff"] = Staff(parent=container, controller=self)
        self.frames["Report"] = Report(parent=container, controller=self)
        self.frames["Admin"] = Admin(parent=container, controller=self)
        self.frames["LiveInformation"] = LiveInformation(parent=container, controller=self)
        self.frames["Cancel"] = Cancel(parent=container, controller=self)
        self.frames["ViewMemberContents"] = ViewMemberContents(parent=container, controller=self)
        self.frames["ThankYou"] = ThankYou(parent=container, controller=self)
        self.frames["ReactivateMembership"] = ReactivateMembership(parent=container, controller=self)
        self.frames["MemberAnonymise"] = MemberAnonymise(parent=container, controller=self)
        self.frames["MemberSearch"] = MemberSearch(parent=container, controller=self)
        self.frames["StaffSignUpPage"] = StaffSignUpPage(parent=container, controller=self)

        self.frames["Spacer"].grid(row=0, column=1, sticky="nsew")
        self.frames["Welcome"].grid(row=0, column=2, sticky="nsew")
        self.frames["ExternalMenu"].grid(row=0, column=2, sticky="nsew")
        self.frames["MemberSignUpPage"].grid(row=0, column=2, sticky="nsew")
        self.frames["SignIn"].grid(row=0, column=2, sticky="nsew")
        self.frames["InternalMenu"].grid(row=0, column=2, sticky="nsew")
        self.frames["Staff"].grid(row=0, column=2, sticky="nsew")
        self.frames["Report"].grid(row=0, column=2, sticky="nsew")
        self.frames["Admin"].grid(row=0, column=2, sticky="nsew")
        self.frames["LiveInformation"].grid(row=0, column=2, sticky="nsew")
        self.frames["Cancel"].grid(row=0, column=2, sticky="nsew")
        self.frames["ViewMemberContents"].grid(row=0, column=2, sticky="nsew")
        self.frames["ThankYou"].grid(row=0, column=2, sticky="nsew")
        self.frames["ReactivateMembership"].grid(row=0, column=2, sticky="nsew")
        self.frames["MemberAnonymise"].grid(row=0, column=2, sticky="nsew")
        self.frames["MemberSearch"].grid(row=0, column=2, sticky="nsew")
        self.frames["StaffSignUpPage"].grid(row=0, column=2, sticky="nsew")

        self.show_frame("Welcome")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    main = App()
    main.mainloop()

