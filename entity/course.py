

class Course(DBConnection):
    def __int__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name

    def createCourse(self):
        try:
            self.open()
            self.stmt.execute('''create table if not exists Course(course_id int primary key,
                                course_name varchar(20), course_code varchar(30), instructor_name varchar(50)) ''')
            self.close()
            print("Table created successfully: ")
        except Exception as e:
            print(e)