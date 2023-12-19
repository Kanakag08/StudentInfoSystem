from util.DBConnection import DBConnection

def UpdateStudentInfo(self):
    try:
        self.student_id = int(input("Enter the student id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.date_of_birth = input("Enter DOB: ")
        self.email = input("Enter the email: ")
        self.phone_number = input("Enter the Phone Number: ")
        data = [(self.first_name, self.last_name, self.date_of_birth, self.email, self.phone_number, self.student_id)]
        self.open()
        self.stmt.executemany(
            f"update Student set first_name=%s ,last_name= %s, date_of_birth = %s, email = %s, phone_number = %s Where student_id= %s",
            data)
        self.conn.commit()
        print("Student Updated: ")
        self.close()

    except Exception as e:
        print(f"Error During Upadting: {e}")