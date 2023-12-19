class Student(DBConnection,Exception):
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def createStudent(self):
        try:
            self.open()
            self.stmt.execute('''create table if not exists Student(student_id int primary key,
                                                                    first_name varchar(20),
                                                                    last_name varchar(20), 
                                                                    date_of_birth date, 
                                                                    email varchar(50),
                                                                    phone_number int) ''')
            self.close()
            print("Table created successfully: ")
        except Exception as e:
            print(e)