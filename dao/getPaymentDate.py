from util.DBConnection import DBConnection

def GetPaymentDate(self):
    try:
        self.open()
        self.stmt.execute('''select payment_date from Payment''')
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        self.conn.commit()
        self.close()
    except Exception as e:
        print(f"Error: {e}")