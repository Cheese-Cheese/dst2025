name = input("Enter employee name: ")
id = int(input("Enter employee ID: "))
monthly_basic_salary = float(input("Enter monthly basic salary: "))
monthly_allowances = float(input("Enter monthly allowances: "))
bonus_percentage = float(input("Enter bonus percentage: "))

monthly_gross_salary = monthly_basic_salary + monthly_allowances
annual_bonus = (monthly_gross_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (monthly_gross_salary * 12) + annual_bonus

'''
print("Employee ID = ", id)
print("Employee Name = ", name)
print("Monthly Gross Salary = ", monthly_gross_salary)
print("Annual Gross Salary = ", annual_gross_salary)
'''

print('%-6s %-15s %-7s %-15s %-15s ' %('ID', 'NAME', 'BONUS', 'MONTHLY_SALARY', 'ANNAUL_SALARY'))
print('-' * 80)
print('%-6d %-15s %-6.2f%% %14.2f %14.2f' %(id, name, bonus_percentage, monthly_gross_salary, annual_gross_salary))