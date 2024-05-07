from Database import *
from datetime import date
from Sign_Up_Page import *


class User:

    def __init__(self, title, first_name, last_name, dob_year, dob_month, dob_date, email, gender, address, post_code, city, membership_type, password):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.dob_year = dob_year
        self.dob_month = dob_month
        self.dob_date = dob_date
        self.email = email
        self.gender = gender
        self.address = address
        self.post_code = post_code
        self.city = city
        self.membership_type = membership_type
        self.password = password

    def db_user_write(self):
        connection.connect(user="root", password="")
        user_query = ("INSERT INTO users"
               "(Title, First_Name, Last_Name, DOB, Email, Gender, Address, Post_Code, City, Membership_Type, Password)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        user_data = [self.title, self.first_name, self.last_name, date(self.dob_year, self.dob_month, self.dob_date), self.email, self.gender, self.address, self.post_code, self.city, self.membership_type, self.password]
        cursor.execute(user_query, user_data)
        connection.commit()
        id_query = ("SELECT User_ID FROM users WHERE Email = %s")
        cursor.execute(id_query, (self.email,))
        result = cursor.fetchall()
        connection.close()
        return result[0][0]

    def db_user_role_write(self, role):
        connection.connect(user="root", password="")
        query = ("INSERT INTO user_roles (User_ID, Role_Type_ID) VALUES (%s, %s)")
        cursor.execute(query, (self, role))
        connection.commit()
        connection.close()