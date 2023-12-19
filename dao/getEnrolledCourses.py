from util.DBConnection import DBConnection

def GetEnrolledCourses(self):
    try:
        self.open()
        self.stmt.execute('''Select * from Course''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(f"Error :{e}")