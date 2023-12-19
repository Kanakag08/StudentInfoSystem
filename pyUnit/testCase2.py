import unittest
from dao.course import course

class TestStudentInformationSystem(unittest.TestCase):

    def setUp(self):
        self.SIS = TestStudentInformationSystem()
        self.SIS.create_course("Introduction to Computer Science", "CS101", "Dr. Smith", 50)

    def tearDown(self):
        pass

    def test_get_course_successfully(self):
        course_code = "CS101"
        course = self.SIS.get_course(course_code)

        # Assert
        self.assertIsNotNone(course)
        self.assertEqual(course['course_id'], 1)
        self.assertEqual(course['course_code'], course_code)
        self.assertEqual(course['course_name'], "Introduction to Computer Science")
        self.assertEqual(course['instructor'], "Dr. Smith")
        self.assertEqual(course['max_students'], 50)

if __name__ == '__main__':
    unittest.main()
