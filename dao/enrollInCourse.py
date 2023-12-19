from util.DBConnection import DBConnection

def EnrollInCourse(self):
    try:
        self.student_id = int(input("Enter the student id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.date_of_birth = input("Enter DOB: ")
        self.email = input("Enter the email: ")
        self.phone_number = input("Enter the Phone Number: ")
        data = [(self.student_id, self.first_name, self.last_name, self.date_of_birth, self.email, self.phone_number)]
        self.open()
        self.stmt.executemany('''insert into Student(student_id,first_name,last_name,date_of_birth,email,phone_number)
                                                      values(%s,%s,%s,%s,%s,%s)''', data)
        self.conn.commit()
        print("Students Enrolled Successfully ")
        self.close()

    except Exception as e:
        print(e)