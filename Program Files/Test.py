from tkinter import *

root = Tk()
root.geometry("2000x2000")

close_photo = PhotoImage(file="backbutton2.png")
close_button = Button(root, image=close_photo, command=root.destroy, height=500, width=500, borderwidth=0,
                      activebackground="#97c7f1")
close_button.place(x=300, y=1)
close_button.config(bg="#97c7f1")

root.mainloop()

#query = "SELECT First_Name FROM users WHERE Email = %s"
#cursor.execute(query, (email_get,))
#first = cursor.fetchall()
#global FIRST1
#FIRST1 = first
#print(FIRST1)

