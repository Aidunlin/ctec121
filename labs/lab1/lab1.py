# lab1.py
# Aidan Linerud

LOCAL_TAX_RATE = 0.10
MEDICAL_RATE = 0.12

# Change: removes magic numbers
FULL_TIME_HOURS = 40
OVERTIME_BONUS_RATE = 1.5

# Input

name = input("Enter name: ")
hourly_wage = float(input("Enter hourly wage: "))
hours_worked = float(
    input("Enter the number of hours worked during the week: "))

# Calculations

if hours_worked > FULL_TIME_HOURS:
    # Change: makes overtime calculation more readable
    wages = FULL_TIME_HOURS * hourly_wage
    overtime_hours = hours_worked - FULL_TIME_HOURS
    overtime_wages = overtime_hours * hourly_wage * OVERTIME_BONUS_RATE
else:
    wages = hours_worked * hourly_wage
    overtime_wages = 0

total_wages = wages + overtime_wages
taxes = total_wages * LOCAL_TAX_RATE
medical = total_wages * MEDICAL_RATE
net_pay = total_wages - taxes - medical

# Output

print()
print(f"Name: {name}")
print(f"Hourly wage: ${hourly_wage:.2f}")
print(f"Local taxes: ${taxes:.2f}")
print(f"Medical insurance: ${medical:.2f}")
print(f"Overtime pay: ${overtime_wages:.2f}")
print(f"Total gross earnings: ${total_wages:.2f}")
print(f"Net pay: ${net_pay:.2f}")
