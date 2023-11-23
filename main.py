from Payments import *

hani = Admin("11", "12", "13")

print("welcome to lancer educational institutions")
print("now let's see are you admin or not?")
user_input = input("if you are admin press 1 and if you are visitor press 0: ")
if user_input == "1":
    print("congrats now tell me your username,password")
    username1 = str(input("username : "))
    password1 = str(input("password : "))
    keycode1 = str(input("keycode : "))
    hani.login(username1, password1, keycode1)
    while not user_input == "0000" and hani.active:
        if hani.active:
            print("WOW! correct user and pass. you are admin for sure. let's move on...")
            print(
                "you can do wide range of activities such as edit, delete, review and etc. with people's data and "
                "course's data")
            print("11.show_info/add/edit/delete students info")
            print("12.show_info/add/edit/delete teachers info")
            print("13.show_info/add/edit/delete supervisors info")
            print("14.show_info/add/edit/delete departments info")
            print("15.show_info/add/edit/delete courses info")
            print("16.show_info/add/edit/delete classes info")
            print("17.show_info sessions info")
            print("21.student to lancer payment")
            print("22.lancer to teacher payment")
            print("23.daily expenses")
            print("24.unexpected expenses")
            print("type down 0000 to exit the program whenever you want")
            user_input = str(input("now what you wanna do honey? tell me by entering the number you want : "))
            if user_input == "11":
                print("student area:")
                print("111.show student's info")
                print("112.edit student's info")
                print("113.add student")
                print("114.delete student")
                user_input = str(input("tell me what you wanna do : "))
                if user_input == "111":
                    user_input = input("tell me student's name : ")
                    user_input2 = input("tell me student's sirname : ")
                    hani.show_info_student(user_input, user_input2)
                elif user_input == "112":
                    user_input = input("tell me student's name : ")
                    user_input2 = input("tell me student's sirname : ")
                    hani.edit_student(user_input, user_input2)
                elif user_input == "113":
                    print("type down student's info down here for me....")
                    name = str(input("name: "))
                    sirname = str(input("sirname: "))
                    age = str(input("age: "))
                    username = str(input("username: "))
                    password = str(input("password: "))
                    department = str(input("department: "))
                    id_no = str(input("id_no: "))
                    print(name, sirname, age, username, password, department, id_no, sep="\n")
                    print("are you sure about student's data ?")
                    user_input = input("if it's ok press y and if not press n")
                    if user_input == "y":
                        hani.add_student(name, sirname, age, username, password, department, id_no)
                    elif user_input == "n":
                        print("go back to previous step and change them")
                    else:
                        print("enter something acceptable :(")
                elif user_input == "114":
                    user_input = input("tell me student's name : ")
                    user_input2 = input("tell me student's sirname : ")
                    hani.delete_student(user_input, user_input2)
            elif user_input == "12":
                print("teacher area:")
                print("121.show teacher's info")
                print("122.edit teacher's info")
                print("123.add teacher")
                print("124.delete teacher")
                user_input = str(input("tell me what you wanna do : "))
                if user_input == "121":
                    user_input = input("tell me teacher's name : ")
                    user_input2 = input("tell me teacher's sirname : ")
                    hani.show_info_teacher(user_input, user_input2)
                elif user_input == "122":
                    user_input = input("tell me teacher's name : ")
                    user_input2 = input("tell me teacher's sirname : ")
                    hani.edit_teacher(user_input, user_input2)
                elif user_input == "123":
                    print("type down teacher's info down here for me....")
                    name = input("name: ")
                    sirname = input("sirname: ")
                    age = input("age: ")
                    username = input("username: ")
                    password = input("password: ")
                    department = input("department: ")
                    profession = input("profession : ")
                    tel_no = input("telephone number : ")
                    id_no = input("id_no: ")
                    print(name, sirname, age, username, password, department, id_no, sep="\n")
                    print("are you sure about teacher's data ?")
                    user_input = input("if it's ok press y and if not press n")
                    if user_input == "y":
                        hani.add_teacher(name, sirname, age, username, password, department, profession, tel_no,
                                         id_no)
                    elif user_input == "n":
                        print("go back to previous step and change them")
                    else:
                        print("enter something acceptable :(")
                elif user_input == "124":
                    user_input = input("tell me teacher's name : ")
                    user_input2 = input("tell me teacher's sirname : ")
                    hani.delete_teacher(user_input, user_input2)
                else:
                    print("LOOK AT THE KEYBOARD SO YOU CAN ENTER NUMBERS PROPERLY :(")
            elif user_input == "13":
                print("supervisor area:")
                print("131.show supervisor's info")
                print("132.edit supervisor's info")
                print("133.add supervisor")
                print("134.delete supervisor")
                user_input = str(input("tell me what you wanna do : "))
                if user_input == "131":
                    user_input = input("tell me supervisor's name : ")
                    user_input2 = input("tell me supervisor's sirname : ")
                    hani.show_info_supervisor(user_input, user_input2)
                elif user_input == "132":
                    user_input = input("tell me student's name : ")
                    user_input2 = input("tell me student's sirname : ")
                    hani.edit_supervisor(user_input, user_input2)
                elif user_input == "133":
                    print("type down supervisor's info down here for me....")
                    name = input("name: ")
                    sirname = input("sirname: ")
                    age = input("age: ")
                    username = input("username: ")
                    password = input("password: ")
                    department = input("department: ")
                    profession = input("profession : ")
                    level = input("level : ")
                    tel_no = input("telephone number : ")
                    id_no = input("id_no: ")
                    print(name, sirname, age, username, password, department, id_no, sep="\n")
                    print("are you sure about teacher's data ?")
                    user_input = input("if it's ok press y and if not press n")
                    if user_input == "y":
                        hani.add_supervisor(name, sirname, age, username, password, department, profession, level,
                                            tel_no, id_no)
                    elif user_input == "n":
                        print("go back to previous step and change them")
                    else:
                        print("enter something acceptable :(")
                elif user_input == "134":
                    user_input = input("tell me supervisor's name : ")
                    user_input2 = input("tell me supervisor's sirname : ")
                    hani.delete_supervisor(user_input, user_input2)
                else:
                    print("LOOK AT THE KEYBOARD SO YOU CAN ENTER NUMBERS PROPERLY :(")
            elif user_input == "14":
                print("department area:")
                print("141.show department's info")
                print("142.edit department's info")
                print("143.add department")
                print("144.delete department")
                if user_input == "141":
                    print("1411.find department by name")
                    print("1412.find department by id_no")
                    print("1413find departments by supervisor")
                    print("1414.find all departments")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1411":
                        user_input = input("tell me department's name : ")
                        print(Department.find_department_by_name(user_input))
                    elif user_input == "1412":
                        user_input = input("tell me department's id number : ")
                        print(Department.find_department_by_id_no(user_input))
                    elif user_input == "1413":
                        user_input = input("tell me departments' supervisor : ")
                        print(Department.find_department_by_supervisor(user_input))
                    else:
                        print("enter something acceptable :(")
                elif user_input == "142":
                    print("1421. edit department by name")
                    print("1422. edit department by id number")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1421":
                        user_input = input("tell me department's name : ")
                        part_name = Department.find_department_by_name(user_input)
                        part_name.edit_department_by_name(part_name)
                    elif user_input == "1422":
                        user_input = input("tell me department's name : ")
                        part_name = Department.find_department_by_id_no(user_input)
                        part_name.edit_department_by_id(part_name)
                elif user_input == "143":
                    print("type down department's info down here for me....")
                    name = input("name : ")
                    supervisor = input("supervisor : ")
                    id_no = input("id number : ")
                    status = input("status : ")
                    print(name, supervisor, id_no, status, sep="\n")
                    user_input = input("if it's ok press y and if not press n :")
                    if user_input == "n":
                        hani.add_department(name, supervisor, id_no, status)
                        print("department added successfully!")
                    elif user_input == "n":
                        print("go back to previous step and change them")
                    else:
                        print("enter something acceptable :(")
                elif user_input == "144":
                    print("1441. delete department by name")
                    print("1442. delete department by id number")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1441":
                        user_input = input("tell me department's name : ")
                        part_name = Department.find_department_by_name(user_input)
                        part_name.delete_department_by_name(part_name)
                    elif user_input == "1442":
                        user_input = input("tell me department's id number : ")
                        part_name = Department.find_department_by_id_no(user_input)
                        part_name.delete_department_by_id(part_name)
                    else:
                        print("enter something acceptable :(")
                else:
                    print("LOOK AT THE KEYBOARD SO YOU CAN ENTER NUMBERS PROPERLY :(")

            elif user_input == "15":
                print("course area:")
                print("151.show course's info")
                print("152.edit course's info")
                print("153.add course")
                print("154.delete course")
                if user_input == "151":
                    print("1511.show course data by name ")
                    print("1512.show course data by id number")
                    print("1513.show course data by level")
                    print("1514.show course data by supervisor")
                    print("1515.show course data by department")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1511":
                        user_input = input("tell me course's name : ")
                        print(Course.find_course_by_name(user_input))
                    elif user_input == "1512":
                        user_input = input("tell me course's id number : ")
                        print(Course.find_course_by_id_no(user_input))
                    elif user_input == "1513":
                        user_input = input("tell me course's level : ")
                        print(Course.find_course_by_level(user_input))
                    elif user_input == "1514":
                        user_input = input("tell me course's supervisor : ")
                        print(Course.find_course_by_supervisor(user_input))
                    elif user_input == "1515":
                        user_input = input("tell me course's id dpartment : ")
                        print(Course.find_course_by_department(user_input))
                    else:
                        print("enter something acceptable :(")
                elif user_input == "152":
                    print("1521.edit course by name ")
                    print("1522.edit course by id number")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1521":
                        user_input = input("tell me course's name : ")
                        print(Course.edit_course_by_name(user_input))
                    elif user_input == "1522":
                        user_input = input("tell me course's id number : ")
                        print(Course.edit_course_by_id_no(user_input))
                elif user_input == "153":
                    print("type down course's info down here for me....")
                    name = input("name : ")
                    department = input("department : ")
                    supervisor = input("supervisor : ")
                    id_no = input("id number : ")
                    level = input("level : ")
                    print(name, department, supervisor, id_no, level, sep="\n")
                    user_input = input("if it's ok press y and if not press n :")
                    if user_input == "n":
                        hani.add_course(name, department, supervisor, id_no, level)
                        print("course added successfully!")
                    elif user_input == "n":
                        print("go back to previous step and change them")
                    else:
                        print("enter something acceptable :(")
                elif user_input == "154":
                    print("1541.delete course by name")
                    print("1542. delete course by id number")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1541":
                        user_input = input("tell me course's name : ")
                        part_name = Course.delete_course_by_name(user_input)
                    elif user_input == "1542":
                        user_input = input("tell me course's id number : ")
                        part_name = Course.delete_course_by_id(user_input)
                    else:
                        print("enter something acceptable :(")
                else:
                    print("LOOK AT THE KEYBOARD SO YOU CAN ENTER NUMBERS PROPERLY :(")
            elif user_input == "16":
                print("class area:")
                print("161.show class's info")
                print("162.edit class's info")
                print("163.add class")
                print("164.delete class")
                if user_input == "161":
                    print("1611.show class data by name ")
                    print("1612.show class data by id number")
                    print("1613.show class data by start date")
                    print("1614.show class data by end date")
                    print("1615.show class data by sessions")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1611":
                        user_input = input("tell me class's name : ")
                        print(Class.find_class_by_name(user_input))
                    elif user_input == "1612":
                        user_input = input("tell me class's id number : ")
                        print(Class.find_class_by_id_no(user_input))
                    elif user_input == "1613":
                        user_input = input("tell me class's start date : ")
                        print(Class.find_class_by_start_date(user_input))
                    elif user_input == "1614":
                        user_input = input("tell me class's end date : ")
                        print(Class.find_class_by_end_date(user_input))
                    elif user_input == "1615":
                        user_input = input("tell me class's sessions : ")
                        print(Class.find_class_by_sessions(user_input))
                    else:
                        print("enter something acceptable :(")
                elif user_input == "162":
                    print("1621.edit class by name ")
                    print("1622.edit class by id number")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1621":
                        user_input = input("tell me class's name : ")
                        print(Class.edit_class_by_name(user_input))
                    elif user_input == "1622":
                        user_input = input("tell me class's id number : ")
                        print(Class.edit_class_by_id(user_input))
                    else:
                        print("enter something acceptable :(")
                        user_input = "162"
                elif user_input == "163":
                    print("type down class's info down here for me....")
                    name = input("name : ")
                    id_no = input("id number : ")
                    student_limit = input("student limit : ")
                    start_date = input("start date : ")
                    end_date = input("sessions date : ")
                    sessions = input("level : ")
                    print(name, id_no, student_limit, start_date, end_date, sessions, sep="\n")
                    user_input = input("if it's ok press y and if not press n :")
                    if user_input == "n":
                        hani.add_class(name, id_no, student_limit, start_date, end_date, sessions)
                        print("course added successfully!")
                    elif user_input == "n":
                        print("go back to previous step and change them")
                        user_input = "163"
                    else:
                        print("enter something acceptable :(")
                        user_input = "163"
                elif user_input == "164":
                    print("1641.delete class by name")
                    print("1642. delete class by id number")
                    user_input = str(input("tell me what you wanna do : "))
                    if user_input == "1641":
                        user_input = input("tell me class's name : ")
                        part_name = Class.delete_class_by_name(user_input)
                    elif user_input == "1642":
                        user_input = input("tell me class's id number : ")
                        part_name = Class.delete_class_by_id_no(user_input)
                    else:
                        print("enter something acceptable :(")
                        user_input = "164"
                elif user_input == "21":
                    print("students payment to lancer")
                    sender_name = input("tell me students name : ")
                    amount = input("amount : ")
                    department = input("department : ")
                    receiver_name = "lancer"
                    Payment.student_to_lancer_payments_money(sender_name, receiver_name, amount, department)
                    print("transaction completed successfully!")
                elif user_input == "22":
                    print("lancer to teachers payments")
                    receiver_name = input("tell me teacher's name : ")
                    amount = input("amount : ")
                    department = input("department : ")
                    sender_name = "lancer"
                    Payment.lancer_to_teachers(sender_name, receiver_name, amount, department)
                    print("transaction completed successfully!")
                elif user_input == "23":
                    print("daily expenses")
                    amount = input("amount : ")
                    info = input("description : ")
                    Payment.daily_expenses(amount, info)
                    print("transaction completed successfully!")
                elif user_input == "24":
                    print("unexpected expenses")
                    amount = input("amount : ")
                    info = input("description : ")
                    Payment.unexpected_expenses(amount, info)
                    print("transaction completed successfully!")
                else:
                    print("LOOK AT THE KEYBOARD SO YOU CAN ENTER NUMBERS PROPERLY :(")
        elif user_input == "0":
            print("hezar mashala. enter correct info")

        else:
            print("enter something valid (1 or 2)")
elif user_input == "0":
    print("ok! now i find out that you are visitor, lets continue to courses and services we have available in "
          "lancer ")
    print("thanks for your visit"
          "our servers are down right now "
          "please retry later")
else:
    print("sweet heart open your eyes and enter 1 or 2. nothing else isn't accepted :(")
