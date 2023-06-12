import csv

# Read departments.csv file
departments = {}
with open('departments.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        departments[row['ID']] = row['NAME']

# Read employees.csv file
employees = {}
with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees[row['ID']] = row['DEPT ID']

# Read salaries.csv file
salaries = {}
with open('salaries.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        emp_id = row['EMP_ID']
        amt = float(row['AMT (USD)'])
        if emp_id not in salaries:
            salaries[emp_id] = []
        salaries[emp_id].append(amt)

# Calculate average salaries
avg_salaries = {}
for emp_id, amt_list in salaries.items():
    avg_salaries[emp_id] = sum(amt_list) / len(amt_list)

# Calculate average department salaries
dept_avg_salaries = {}
for emp_id, dept_id in employees.items():
    if dept_id not in dept_avg_salaries:
        dept_avg_salaries[dept_id] = []
    if emp_id in avg_salaries:
        dept_avg_salaries[dept_id].append(avg_salaries[emp_id])

# Calculate top 3 average monthly salary departments
top_departments = sorted(dept_avg_salaries.items(
), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)[:3]

# Display results on console
print("DEPT_NAME   AVG_MONTHLY_SALARY")
for dept_id, avg_salaries in top_departments:
    dept_name = departments[dept_id]
    avg_monthly_salary = sum(avg_salaries) / len(avg_salaries)
    print(f"{dept_name:<12} {avg_monthly_salary:.2f}")

# Write results to a new CSV file
headers = ['DEPT_NAME', 'AVG_MONTHLY_SALARY']
rows = []
for dept_id, avg_salaries in top_departments:
    dept_name = departments[dept_id]
    avg_monthly_salary = sum(avg_salaries) / len(avg_salaries)
    rows.append([dept_name, round(avg_monthly_salary, 2)])

with open('top_departments.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("Results have been saved to top_departments.csv file.")
