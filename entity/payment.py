class Payment(DBConnection,Exception):
    def __int__(self, payment_id: int, student_id: int, amount: int, payment_date: str):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date

    def createPayment(self):
        try:
            self.open()
            self.stmt.execute('''payment_id INT PRIMARY KEY,
                                    student_id INT,
                                    amount DECIMAL(10, 2),
                                    payment_date DATE,
                                    FOREIGN KEY (student_id) REFERENCES Student(student_id) ''')
            self.close()
            print("Table created successfully: ")
        except Exception as e:
            print(e)