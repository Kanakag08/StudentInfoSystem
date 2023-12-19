from util.DBConnection import DBConnection
class Enrollment(DBConnection):
    def __int__(self, enrollment_id, student_id, course_id, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

        def createEnrollment(self):
            try:
                self.open()
                self.stmt.execute('''enrollment_id INT PRIMARY KEY,
                                    student_id INT,
                                    course_id INT,
                                    enrollment_date DATE,
                                    FOREIGN KEY (student_id) REFERENCES Student(student_id),
                                    FOREIGN KEY (course_id) REFERENCES Course(course_id) ''')
                self.close()
                print("Table created successfully: ")
            except Exception as e:
                print(e)