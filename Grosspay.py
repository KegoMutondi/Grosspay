# Function to calculate gross pay
def calculate_gross_pay(hours, rate):
    return hours * rate

# Prompt the user for hours worked and rate per hour
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Calculate gross pay
gross_pay = calculate_gross_pay(hours, rate)

# Print the gross pay
print(f"Gross Pay: {gross_pay:.2f}")
