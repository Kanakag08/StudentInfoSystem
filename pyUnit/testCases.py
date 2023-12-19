import unittest
from dao.course import course
class TestStudentInformationSystem(unittest.TestCase):

    def setUp(self):
        self.sis = StudentInformationSystem()

    def tearDown(self):
        pass

    def test_create_course_successfully(self):
        course_id=1
        course_name = "Introduction to Computer Science"
        course_code = "CS101"
        instructor_name = "Dr. Smith"

        result = self.sis.create_course(course_id,course_name, course_code, instructor_name)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
