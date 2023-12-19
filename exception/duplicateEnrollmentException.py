class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student is already enrolled in the course"):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def is_duplicate_enrollment(student_id, course_id, conn, stmt):
        stmt.execute('''SELECT 1 FROM Enrollment 
                        WHERE student_id = %s AND course_id = %s''', (student_id, course_id))
        return bool(stmt.fetchone())