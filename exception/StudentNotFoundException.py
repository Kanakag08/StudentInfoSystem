class StudentNotFoundException(Exception):
    def __init__(self, message="Student not found"):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def is_student_exists(student_id, conn, stmt):
        stmt.execute('SELECT 1 FROM Course WHERE CourseID = %s', (student_id,))
        return bool(stmt.fetchone())