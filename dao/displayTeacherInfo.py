from util.DBConnection import DBConnection

def DisplayTeacherInfo(self):
    try:
        self.open()
        self.stmt.execute('''select * from Teacher''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(f"Error: {e}")