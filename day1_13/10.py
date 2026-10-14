# employees = {}
# n = int(input("How many employees? "))
# for i in range(n):
#     emp_id = input(f"Enter employee {i+1} ID: ")
#     name = input("Enter employee name: ")
#     basic = float(input("Enter basic salary: "))
#     hra = float(input("Enter HRA: "))
#     da = float(input("Enter DA: "))
#     gross = basic + hra + da
#     employees[emp_id] = {
#         "name": name,
#         "basic_salary": basic,
#         "hra": hra,
#         "da": da,
#         "gross_salary": gross
#     }
# print("\nAll Employee Details:")
# print(employees)




# gross_salary = float(input("Enter gross salary: "))
# pf = gross_salary * 0.10
# professional_tax = gross_salary*0.08
# other_deductions = gross_salary*0.05
# net_salary = gross_salary - pf - professional_tax - other_deductions
# print("Gross Salary:", gross_salary)
# print("PF:", pf)
# print("Professional Tax:", professional_tax)
# print("Other Deductions:", other_deductions)
# print("Net Salary:", net_salary)



# emp_id = input("Enter employee ID: ")
# name = input("Enter employee name: ")
# basic = float(input("Enter basic salary: "))
# hra = float(input("Enter HRA: "))
# da = float(input("Enter DA: "))
# pf = float(input("Enter PF deduction: "))
# professional_tax = float(input("Enter professional tax: "))
# other_deductions = float(input("Enter other deductions: "))
# gross_salary = basic + hra + da
# total_deductions = pf + professional_tax + other_deductions
# net_salary = gross_salary - total_deductions
# payslip = {
#     "Employee ID": emp_id,
#     "Employee Name": name,
#     "Basic Salary": basic,
#     "HRA": hra,
#     "DA": da,
#     "Gross Salary": gross_salary,
#     "PF": pf,
#     "Professional Tax": professional_tax,
#     "Other Deductions": other_deductions,
#     "Total Deductions": total_deductions,
#     "Net Salary": net_salary
# }
# print("\n========== MONTHLY PAYSLIP ==========")
# for key, value in payslip.items():
#     print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")
# print("=====================================")



# name = input("Enter employee name: ")
# monthly_salary = float(input("Enter monthly salary: "))
# overtime_hours = float(input("Enter overtime hours worked: "))
# overtime_rate = float(input("Enter overtime rate per hour: "))
# overtime_pay = overtime_hours * overtime_rate
# total_salary = monthly_salary + overtime_pay
# print("\n--- Salary Details ---")
# print("Employee Name:", name)
# print("Monthly Salary:", monthly_salary)
# print("Overtime Pay:", overtime_pay)
# print("Total Salary:", total_salary)



# a='aaasssdddfff'
# fre={}
# for i in a:
#   if i in fre:
#     fre[i]+=1
#   else:
#     fre[i]=1
# print(fre)



# s="hello"
# s.sort()
# print(s)