from util.DBConnection import DBConnection

def DisplayStudentInfo(self):
    try:
        self.open()
        self.stmt.execute('''select * from Student''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(f"Error Displaying: {e}")