from Users import *
import datetime


class Payment:
    all_payments = []
    all_payments_money = 0
    student_to_lancer_payments = []
    student_to_lancer_payments_money = 0
    lancer_to_student_payments = []
    lancer_to_student_payments_money = 0
    lancer_to_teachers_payments = []
    lancer_to_teachers_payments_money = 0
    lancer_daily_expenses = []
    lancer_daily_expenses_money = 0
    lancer_unexpected_expenses = []
    lancer_unexpected_expenses_money = 0

    date_time = datetime.datetime.today()

    @staticmethod
    def student_to_lancer(sender_name, receiver_name, amount, department):
        data = {"type": "STL", "sender": sender_name, "receiver": receiver_name, "department": department,
                "amount": amount,
                "date_time": Payment.date_time}
        Department.income = Department.income + amount
        Payment.student_to_lancer_payments.append(data)
        Payment.student_to_lancer_payments_money = Payment.student_to_lancer_payments_money + amount
        Payment.all_payments.append(data)
        Payment.all_payments_money = Payment.all_payments_money + amount

    @staticmethod
    def lancer_to_teachers(sender_name, receiver_name, amount, department):
        data = {"type": "LTT", "sender": sender_name, "receiver": receiver_name, "department": department,
                "amount": amount,
                "date_time": Payment.date_time}
        Teacher.income = Teacher.income + amount
        Payment.lancer_to_teachers_payments.append(data)
        Payment.lancer_to_teachers_payments_money = Payment.lancer_to_teachers_payments_money - amount
        Payment.all_payments.append(data)
        Payment.all_payments_money = Payment.all_payments_money - amount

    @staticmethod
    def daily_expenses(amount, info):
        data = {"type": "DE", "description": info, "amount": amount, "date": Payment.date_time}
        Payment.lancer_daily_expenses.append(data)
        Payment.lancer_daily_expenses_money = Payment.lancer_daily_expenses_money - amount
        Payment.all_payments.append(data)
        Payment.all_payments_money = Payment.all_payments_money - amount

    @staticmethod
    def unexpected_expenses(info, amount):
        data = {"type": "UE", "description": info, "amount": amount, "date": Payment.date_time}
        Payment.lancer_unexpected_expenses.append(data)
        Payment.lancer_unexpected_expenses = Payment.lancer_unexpected_expenses_money - amount
        Payment.all_payments.append(data)
        Payment.all_payments_money = Payment.all_payments_money - amount

    @staticmethod
    def show_transactions_list():
        for payment in Payment.all_payments:
            return payment

    @staticmethod
    def show_department_income(name):
        part = Department.departments_total_income(name)
        return part["income"]

    @staticmethod
    def show_teachers_income(name):
        teacher = Teacher.teachers_total_income(name)
        return teacher["income"]

    @staticmethod
    def show_supervisor_income(name):
        supervisor = Supervisor.supervisors_total_income(name)
        return supervisor["income"]

    @staticmethod
    def show_total_income():
        return Payment.all_payments_money
