
# Employee Payroll and Deduction Analysis System

print("===== EMPLOYEE PAYROLL SYSTEM =====")
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: Rs. "))
overtime_hours = float(input("Enter overtime hours: "))
incentives = float(input("Enter incentives: Rs. "))


if basic < 0 or overtime_hours < 0 or incentives < 0:

    print("Invalid Input! Values cannot be negative.")

else:

  
    allowances = basic * 0.20

  
    overtime = overtime_hours * 200

    
    gross = basic + allowances + overtime + incentives

    # Progressive deduction calculation
    if gross <= 10000:
        deduction = 0

    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05

    elif gross <= 40000:
        deduction = (10000 * 0.05) + (gross - 20000) * 0.10

    else:
        deduction = (10000 * 0.05) + (20000 * 0.10) + (gross - 40000) * 0.15

    
    net_salary = gross - deduction

    
    print("\n===================================")
    print("       EMPLOYEE SALARY STATEMENT")
    print("===================================")

    print("Employee Name       :", name)
    print("Employee ID         :", emp_id)

    print("-----------------------------------")
    print("Basic Pay           : Rs.", round(basic, 2))
    print("Allowances (20%)    : Rs.", round(allowances, 2))
    print("Overtime Payment    : Rs.", round(overtime, 2))
    print("Incentives          : Rs.", round(incentives, 2))

    print("-----------------------------------")
    print("Gross Salary        : Rs.", round(gross, 2))
    print("Total Deduction     : Rs.", round(deduction, 2))
    print("-----------------------------------")
    print("NET SALARY          : Rs.", round(net_salary, 2))
    print("===================================")

    print("Salary calculation completed!")

