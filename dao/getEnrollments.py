from util.DBConnection import DBConnection

def GetEnrollments(self):
    try:
        self.open()
        self.stmt.execute(f'''select Enrollment.enrollment_id, Course.course_id from Course 
                                 join Enrollment 
                                 on Course.course_id=Enrollment.course_id
                                 where course_id=%s''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(e)