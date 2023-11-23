from Users import *
from Payments import *


class Department:
    departments = []

    def __init__(self, name, supervisor, id_no, status):
        self.name = name
        self.supervisor = supervisor
        self.id_no = id_no
        self.status = status
        self.income = 0
        self.department = {"name": self.name, "supervisor": self.supervisor, "id": self.id_no, "status": self.status,
                           "income": self.income}
        self.departments.append(self.department)

    def edit(self):
        user_input = None
        while not user_input == "exit":
            print("department's info:")
            print(self.department)
            element = input("which element you wanna edit?")
            new_value = input("tell me the new value for the element:")
            self.department[element] = new_value
            user_input = input("if you want to edit more press 1 or if you are done type exit to close the program")

    @staticmethod
    def find_department_by_name(name):
        return [department for department in Department.departments if department[name] == name][0]

    @staticmethod
    def find_department_by_supervisor(name):
        return [supervisor for supervisor in Supervisor.supervisors if supervisor[name] == name][0]

    @staticmethod
    def find_department_by_id_no(id_no):
        return [code for code in Department.departments if code[id_no] == id_no][0]

    @staticmethod
    def get_all_departments():
        return Department.departments

    @staticmethod
    def edit_department_by_name(name):
        department_data = Department.find_department_by_name(name)
        user_input = None
        while not user_input == "exit":
            print("department's info:")
            print(department_data)
            element = input("which element you wanna edit?")
            new_value = input("tell me the new value for the element:")
            department_data[element] = new_value
            user_input = input("if you want to edit more press 1 or if you are done type exit to close the program")

    @staticmethod
    def edit_department_by_id(id_no):
        department_data = Department.find_department_by_id_no(id_no)
        user_input = None
        while not user_input == "exit":
            print("department's info:")
            print(department_data)
            element = input("which element you wanna edit?")
            new_value = input("tell me the new value for the element:")
            department_data[element] = new_value
            user_input = "if you want to edit more press 1 or if you are done type exit to close the program"

    @staticmethod
    def delete_department_by_name(name):
        departman = Department.find_department_by_name(name)
        departman["status"] = False


    @staticmethod
    def delete_department_by_id(id_no):
        departman = Department.find_department_by_id_no(id_no)
        departman["status"] = False

    @staticmethod
    def departments_total_income(name):
        part = Department.find_department_by_name(name)
        return part["income"]


class Course:
    courses = []

    def __init__(self, name, department, supervisor, id_no, level):
        self.name = name
        self.department = department
        self.supervisor = supervisor
        self.id_no = id_no
        self.level = level
        self.income = 0
        self.course = {"name": self.name, "department": self.department, "supervisor": self.supervisor,
                       "id": self.id_no, "level": self.level, "income": self.income}
        self.courses.append(self.course)

    @staticmethod
    def find_course_by_name(name):
        ccourse = [dore for dore in Course.courses if dore["name"] == name][0]
        return ccourse

    @staticmethod
    def find_course_by_id_no(id_no):
        ccourse = [dore for dore in Course.courses if dore["id"] == id_no][0]
        return ccourse

    @staticmethod
    def find_course_by_level(level):
        ccourse = [dore for dore in Course.courses if dore["level"] == level][0]
        return ccourse

    @staticmethod
    def find_course_by_supervisor(supervisor):
        ccourse = [dore for dore in Course.courses if dore["supervisor"] == supervisor][0]
        return ccourse

    @staticmethod
    def find_course_by_department(department):
        ccourse = [dore for dore in Course.courses if dore["name"] == department][0]
        return ccourse

    @staticmethod
    def edit_course_by_name(name):
        ccourse = Course.find_course_by_name(name)
        user_input = None
        while not user_input == "exit":
            print("course's info:")
            print(ccourse)
            element = input("which element you wanna edit?")
            new_value = input("tell me the new value for the element:")
            ccourse[element] = new_value
            user_input = "if you want to edit more press 1 or if you are done type exit to close the program"

    @staticmethod
    def edit_course_by_id_no(id_no):
        ccourse = Course.find_course_by_id_no(id_no)
        user_input = None
        while not user_input == "exit":
            print("course's info:")
            print(ccourse)
            element = input("which element you wanna edit?")
            new_value = input("tell me the new value for the element:")
            ccourse[element] = new_value
            user_input = "if you want to edit more press 1 or if you are done type exit to close the program"

    @staticmethod
    def delete_course_by_name(name):
        ccourse = Course.find_course_by_name(name)
        ccourse["status"] = False
        print("course deleted successfully!")

    @staticmethod
    def delete_course_by_id(id_no):
        ccourse = Course.find_course_by_id_no(id_no)
        ccourse["status"] = False
        print("course deleted successfully!")

    @staticmethod
    def courses_total_income(name):
        course = Course.find_course_by_name(name)
        return course["income"]


class Class:
    classes_list = []

    def __init__(self, name, id_no, student_limit, start_date, end_date, sessions):
        self.name = name
        self.id_no = id_no
        self.student_limit = student_limit
        self.start_date = start_date
        self.end_date = end_date
        self.sessions = sessions
        self.classes = {"name": self.name, "id": self.id_no, "limit": self.student_limit,
                        "start_date": self.start_date, "end_date": self.end_date, "sessions": self.sessions}
        self.classes_list.append(self.classes)

    @staticmethod
    def find_class_by_name(name):
        cclass = [klass for klass in Class.classes_list if klass["name"] == name][0]
        return cclass

    @staticmethod
    def find_class_by_id_no(id_no):
        cclass = [klass for klass in Class.classes_list if klass["id"] == id_no][0]
        return cclass

    @staticmethod
    def find_class_by_start_date(start_date):
        cclass = [klass for klass in Class.classes_list if klass["start_date"] == start_date][0]
        return cclass

    @staticmethod
    def find_class_by_end_date(end_date):
        cclass = [klass for klass in Class.classes_list if klass["end_date"] == end_date][0]
        return cclass

    @staticmethod
    def find_class_by_sessions(sessions):
        cclass = [klass for klass in Class.classes_list if klass["sessions"] == sessions][0]
        return cclass

    @staticmethod
    def edit_class_by_name(name):
        cclass = Class.find_class_by_name(name)
        print("class's info:")
        print(cclass)
        user_input = None
        while not user_input == "exit":
            element = input("which element you wanna edit?")
            new_value = input("tell me the new value for the element:")
            cclass[element] = new_value
            user_input = "if you want to edit more press 1 or if you are done type exit to close the program"

    @staticmethod
    def edit_class_by_id(id_no):
        cclass = Class.find_class_by_id_no(id_no)
        print("class's info:")
        print(cclass)
        user_input = None
        while not user_input == "exit":
            element = input("which element you wanna edit?")
            new_value = input("tell me the new value for the element:")
            cclass[element] = new_value
            user_input = "if you want to edit more press 1 or if you are done type exit to close the program"

    @staticmethod
    def delete_class_by_name(name):
        cclass = Class.find_class_by_name(name)
        cclass["status"] = False
        print("class deleted successfully!")

    @staticmethod
    def delete_class_by_id_no(id_no):
        cclass = Class.find_class_by_id_no(id_no)
        cclass["status"] = False
        print("class deleted successfully!")


class Session:
    sessions = []

    def __init__(self, start_time, end_time, duration, no):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.no = no
        self.status = True
        self.session = {"start_time": self.start_time, "end_time": self.end_time,
                        "duration": self.duration, "session_no": self.no, "status": True}

    @staticmethod
    def find_sessions_by_start_time(start_time):
        ssessions = [jalase for jalase in Session.sessions if jalase["start_time"] == start_time]
        return ssessions

    @staticmethod
    def find_sessions_by_end_time(end_time):
        ssessions = [jalase for jalase in Session.sessions if jalase["end_time"] == end_time]
        return ssessions

    @staticmethod
    def find_sessions_by_start_duration(duration):
        ssessions = [jalase for jalase in Session.sessions if jalase["duration"] == duration]
        return ssessions

    @staticmethod
    def find_sessions_by_start_session_no(session_no):
        ssessions = [jalase for jalase in Session.sessions if jalase["session_no"] == session_no]
        return ssessions
