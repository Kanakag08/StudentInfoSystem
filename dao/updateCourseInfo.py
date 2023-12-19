from util.DBConnection import DBConnection

def UpdateCourseInfo(self):
    try:
        self.course_id = int(input("Enter the course id: "))
        self.course_name = input("Enter the course name: ")
        self.course_code = input("Enter the course code: ")
        self.instructor_name = input("Enter The Instructor name: ")
        self.open()
        data = [(self.course_id, self.course_name, self.course_code, self.instructor_name)]
        self.stmt.executemany(
            f'''Update Course Set course_id = %s,course_name=%s, course_code=%s, instructor_name=%s ''', data)
        self.conn.commit()
        self.close()
    except Exception as e:
        print(f"Error: {e}")