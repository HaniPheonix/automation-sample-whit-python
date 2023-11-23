from Departments import Department, Class, Course


class User:
    def __init__(self, name, family_name, age, username, password, id_no):
        self.status = True
        self.name = name
        self.family_name = family_name
        self.age = age
        self.username = username
        self.password = password
        self.id_no = id_no


class Teacher(User):
    teachers = []

    def __init__(self, name, family_name, age, username, password, department, profession, tel_no,
                 id_no):
        super().__init__(name, family_name, age, username, password, id_no)
        self.department = department
        self.profession = profession
        self.tel_no = tel_no
        self.income = 0
        self.teacher = {"name": self.name, "sirname": self.family_name, "age": self.age, "username": self.username,
                        "password": self.password, "department": self.department, "profession": self.profession,
                        "tel_no": self.tel_no}
        self.teachers.append(self.teacher)

    @staticmethod
    def find_info_teacher(name):
        teacher_data = [ostad for ostad in Teacher.teachers if ostad["name"] == name][0]
        return teacher_data

    @staticmethod
    def teachers_total_income(name):
        part = Teacher.find_info_teacher(name)
        return part["income"]


class Student(User):
    students = []

    def __init__(self, name, family_name, age, username, password, department, id_no):
        super().__init__(name, family_name, age, username, password, id_no)
        self.department = department
        self.id_no = id_no
        self.student = {"name": self.name, "sirname": self.family_name, "age": self.age, "username": self.username,
                        "password": self.password, "department": self.department, "id_no": self.id_no}
        self.students.append(self.student)

    @staticmethod
    def find_info_student(name):
        student_data = [student for student in Student.students if student["name"] == name][0]
        return student_data


class Supervisor(User):
    supervisors = []

    def __init__(self, name, family_name, age, username, password, department, profession, level,
                 tel_no, id_no):
        super().__init__(name, family_name, age, username, password, id_no)
        self.department = department
        self.profession = profession
        self.level = level
        self.tel_no = tel_no
        self.supervisor = {"name": self.name, "sirname": self.family_name, "age": self.age,
                           "username": self.username, "password": self.department, "profession": self.profession,
                           "telephone": self.tel_no, "id": self.id_no}
        self.supervisors.append(self.supervisor)

    @staticmethod
    def find_info_supervisor(name):
        supervisor_data = [supervisor for supervisor in Supervisor.supervisors if supervisor["name"] == name][0]
        return supervisor_data

    @staticmethod
    def supervisors_total_income(name):
        part = Supervisor.find_info_supervisor(name)
        return part["income"]


class Admin:
    def __init__(self, username, password, keycode):
        self.username = username
        self.password = password
        self.keycode = keycode
        self.active = False

    def login(self, input_username, input_password, input_keycode):
        if (input_username == self.username) and (input_password == self.password) and (input_keycode == self.keycode):
            self.active = True
            print("login successful")

    def add_teacher(self, name, family_name, age, username, password, department, profession, tel_no, id_no):
        if self.active:
            print("teacher's info:")
            Teacher(name, family_name, age, username, password, department, profession, tel_no, id_no)
            print("teacher added successfully")
        else:
            print("login first!")

    def show_info_teacher(self, name, sirname):
        if self.active:
            teacher_data = \
                [ostad for ostad in Teacher.teachers if ostad["name"] == name and ostad["sirname"] == sirname][0]
            print("teachers info:")
            print(teacher_data)
        else:
            print("login first!")

    def edit_teacher(self, name, sirname):
        if self.active:
            teacher_data = \
                [ostad for ostad in Teacher.teachers if ostad["name"] == name and ostad["sirname"] == sirname][0]
            user_input = None
            while not user_input == "exit":
                print("teacher's info:")
                print(teacher_data)
                element = input("which element you wanna edit?")
                new_value = input("tell me the new value for the element:")
                teacher_data[element] = new_value
                user_input = "if you want to edit more press 1 or if you are done type exit to close the program"
        else:
            print("login first!")

    def delete_teacher(self, name, sirname):
        if self.active:
            teacher_data = \
                [ostad for ostad in Teacher.teachers if ostad["name"] == name and ostad["sirname"] == sirname][0]
            teacher_data["status"] = False
            print("teacher deleted successfully")
        else:
            print("login first!")

    def add_student(self, name, family_name, age, username, password, department, id_no):
        if self.active:
            print("student's info:")
            Student(name, family_name, age, username, password, department, id_no)
            print("student added successfully")
        else:
            print("login first!")

    def show_info_student(self, name, sirname):
        if self.active:
            student_data = \
                [shagerd for shagerd in Student.students if shagerd["name"] == name and shagerd["sirname"] == sirname][
                    0]
            print("students info")
            print(student_data)
        else:
            print("login first!")

    def edit_student(self, name, sirname):
        if self.active:
            student_data = \
                [shagerd for shagerd in Student.students if shagerd["name"] == name and shagerd["sirname"] == sirname][
                    0]
            user_input = None
            while not user_input == "exit":
                print("students's info:")
                print(student_data)
                element = input("which element you wanna edit?")
                new_value = input("tell me the new value for the element:")
                student_data[element] = new_value
                user_input = "if you want to edit more press 1 or if you are done type exit to close the program"
        else:
            print("login first!")

    def delete_student(self, name, sirname):
        if self.active:
            student_data = \
                [shagerd for shagerd in Student.students if shagerd["name"] == name and shagerd["sirname"] == sirname][
                    0]
            student_data["status"] = False
            print("student deleted successfully")
        else:
            print("login first!")

    def add_supervisor(self, name, family_name, age, username, password, department, profession, level,
                       tel_no, id_no):
        if self.active:
            print("supervisor's info:")
            Supervisor(name, family_name, age, username, password, department, profession, level,
                       tel_no, id_no)
            print("supervisor added successfully")
        else:
            print("login first!")

    def show_info_supervisor(self, name, sirname):
        if self.active:
            supervisor_data = \
                [admin for admin in Supervisor.supervisors if admin["name"] == name and admin["sirname"] == sirname][0]
            print("supervisor info")
            print(supervisor_data)
        else:
            print("login first!")

    def edit_supervisor(self, name, sirname):
        if self.active:
            supervisor_data = \
                [admin for admin in Supervisor.supervisors if admin["name"] == name and admin["sirname"] == sirname][0]
            user_input = None
            while not user_input == "exit":
                print("supervisor's info:")
                print(supervisor_data)
                element = input("which element you wanna edit?")
                new_value = input("tell me the new value for the element:")
                supervisor_data[element] = new_value
                user_input = "if you want to edit more press 1 or if you are done type exit to close the program"
        else:
            print("login first!")

    def delete_supervisor(self, name, sirname):
        if self.active:
            supervisor_data = \
                [admin for admin in Supervisor.supervisors if admin["name"] == name and admin["sirname"] == sirname][0]
            supervisor_data["status"] = False
            print("supervisor deleted successfully")
        else:
            print("login first!")

    @staticmethod
    def add_department(name, supervisor, id_no, status):
        Department(name, supervisor, id_no, status)
        print("department added successfully")

    @staticmethod
    def add_course(name, department, supervisor, id_no, level):
        Course(name, department, supervisor, id_no, level)
        print("course added successfully")

    @staticmethod
    def add_class(name, id_no, student_limit, start_date, end_date, sessions):
        Class(name, id_no, student_limit, start_date, end_date, sessions)
        print("class added successfully")
