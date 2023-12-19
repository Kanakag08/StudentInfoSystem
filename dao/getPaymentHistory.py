from util.DBConnection import DBConnection

def GetPaymentHistory(self):
    try:
        self.open()
        self.stmt.execute(f'''select * from Payment''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    except Exception as e:
        print(e)