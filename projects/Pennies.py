# Salary of a penny doubles each day for days given
# 9/29/26
# Jonathan Pyatak

# Input
idays = int(input("Enter the number of days: "))

# Calculations and Output
cpennies = 1
ctotal_pennies = 0

print("\nDay    Salary")
print("----------------")

for day in range(1, idays + 1):
    csalary = cpennies / 100
    print(f"{day}\t${csalary:,.2f}")

    ctotal_pennies = ctotal_pennies + cpennies
    cpennies *= 2

# Display total
ctotal_pay = ctotal_pennies / 100
print("----------------")
print(f"Total pay: ${ctotal_pay:,.2f}")