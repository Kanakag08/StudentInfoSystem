from dao.displayCourseInfo import displayCourseInfo
from dao.displayStudentInfo import displayStudentInfo
from dao.displayTeacherInfo import displayTeacherInfo
from dao.enrollInCourse import enrollInCourse
from dao.getEnrolledCourses import getEnrolledCourses
from dao.getEnrollments import getEnrollments
from dao.getPaymentAmount import getPaymentAmount
from dao.getPaymentDate import getPaymentDate
from dao.getPaymentHistory import getPaymentHistory
from dao.getTeacher import getTeacher
from dao.updateCourseInfo import updateCourseInfo
from dao.updatestudentInfo import updatestudentInfo
from dao.updateTeacherInfo import updateTeacherInfo
if __name__=="__main__":
    try:
        createTable()
        while True:
            print("Enter 1 to display course info:")
            print("Enter 2 to display student info: ")
            print("Enter 3 to display teacher info: ")
            print("Enter 4 to enroll in course: ")
            print("Enter 5 to get enrolled courses: ")
            print("Enter 6 to get Enrollments: ")
            print("Enter 7 to get payment amount: ")
            print("Enter 8 to get payment date: ")
            print("Enter 9 to get payment history: ")
            print("Enter 10 to get teacher: ")
            print("Enter 11 to update course info: ")
            print("Enter 12 to update student info: ")
            print("Enter 13 to update teacher info: ")
            print("Enter 14 to Exit: ")

            a=input("Enter your choice: ")
            if a == '1':
                displayCourseInfo()
            elif a == '2':
                displayStudentInfo()
            elif a == '3':
                displayTeacherInfo()
            elif a == '4':
                enrollInCourse()
            elif a == '5':
                getEnrolledCourses()
            elif a == '6':
                getEnrollments()
            elif a == '7':
                getPaymentAmount()
            elif a == '8':
                getPaymentDate()
            elif a == '9':
                getPaymentHistory()
            elif a == '10':
                getTeacher()
            elif a == '11':
                updateCourseInfo()
            elif a == '12':
                updatestudentInfo()
            elif a == '13':
                updateTeacherInfo()
            elif a =='14':
                break
            else:
                print("Invalid Choice: ")

    except Exception as e:
        print(f"Error: {e}")