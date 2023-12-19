from util.DBConnection import DBConnection

def GetTeacher(self):
    try:
        self.open()
        self.stmt.execute(f'''select * from Course''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(e)