name = input("Enter employee name: ")
id = int(input("Enter employee ID: "))
monthly_basic_salary = float(input("Enter monthly basic salary: "))
monthly_allowances = float(input("Enter monthly allowances: "))
bonus_percentage = float(input("Enter bonus percentage: "))

monthly_gross_salary = monthly_basic_salary + monthly_allowances
annual_bonus = (monthly_gross_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (monthly_gross_salary * 12) + annual_bonus


standard_deduction = 50000
taxable_income = annual_gross_salary - standard_deduction
print('Taxable income = ', taxable_income)