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

health_and_education_cess = 0.04

print('-' * 35)
print('%-17s %s' %('Salary_Range', 'Tax_Percentage'))
print('-' * 35)
print('%7d - %7d %3d%%' %(0, 300000, 0))
print('%7d - %7d %3d%%' %(300001, 600000, 5))
print('%7d - %7d %3d%%' %(600001, 900000, 10))
print('%7d - %7d %3d%%' %(900001, 1200000, 15))
print('%7d - %7d %3d%%' %(1200001, 1500000, 20))
print('%7d - %7s %3d%%' %(1500001, 'Or More', 30))