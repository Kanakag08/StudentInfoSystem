class Teacher(DBConnection,Exception):
    def __int__(self, teacher_id, first_name, last_name, email, expertise):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.expertise = expertise

    def createTeacher(self):
        try:
            self.open()
            self.stmt.execute('''teacher_id INT PRIMARY KEY,
                                    first_name VARCHAR(50),
                                    last_name VARCHAR(50),
                                    email VARCHAR(100) UNIQUE
                                ) ''')
            self.close()
            print("Table created successfully: ")
        except Exception as e:
            print(e)