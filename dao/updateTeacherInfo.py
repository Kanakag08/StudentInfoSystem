from util.DBConnection import DBConnection

def UpdateTeacherInfo(self):
    try:
        self.teacher_id = int(input("Enter teacher id: "))
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.email = input("Enter email: ")
        self.expertise = input("Enter Expertise: ")
        data = [(self.first_name, self.last_name, self.email, self.expertise, self.teacher_id)]
        self.open()
        self.stmt.executemany(
            f"update Teacher set first_name=%s, last_name=%s, email=%s, expertise=%s where teacher_id=%s ", data)
        self.conn.commit()
        self.close()
    except Exception as e:
        print(f"Error: {e}")