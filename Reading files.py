
employee_file = open("employee.txt", "r")

for employee in employee_file.readline():
    print(employee)

print(employee_file.readable())

employee_file.close()
