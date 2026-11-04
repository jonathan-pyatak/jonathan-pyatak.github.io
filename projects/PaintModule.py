# Paint Job Estimator
# Page 340, #7
# 10/6/26
# Jonathan Pyatak

# Variable Declaration


# Function to calculate gallons of paint
def calculate_gallons(square_feet):
    gallons = square_feet / 112
    return gallons


# Function to calculate hours of labor
def calculate_hours(square_feet):
    hours = (square_feet / 112) * 8
    return hours


# Function to calculate paint cost
def calculate_paint_cost(gallons, paint_price):
    paint_cost = gallons * paint_price
    return paint_cost


# Function to calculate labor cost
def calculate_labor_cost(hours):
    labor_cost = hours * 35
    return labor_cost


# Function to display the results
def display_results(gallons, hours, paint_cost, labor_cost):
    total_cost = paint_cost + labor_cost

    print()
    print("Gallons of paint required:", round(gallons, 2))
    print("Hours of labor required:", round(hours, 2))
    print("Cost of paint: $", format(paint_cost, ".2f"))
    print("Labor charges: $", format(labor_cost, ".2f"))
    print("Total cost of paint job: $", format(total_cost, ".2f"))
    print()


# Main program
def main():

    another_job = "y"

    while another_job == "y" or another_job == "Y":

        # Input
        square_feet = float(input("Enter the square feet of wall space: "))
        paint_price = float(input("Enter the price of paint per gallon: "))

        # Calculations
        gallons = calculate_gallons(square_feet)
        hours = calculate_hours(square_feet)
        paint_cost = calculate_paint_cost(gallons, paint_price)
        labor_cost = calculate_labor_cost(hours)

        # Output
        display_results(gallons, hours, paint_cost, labor_cost)

        # Ask if another job should be entered
        another_job = input("Do you have another job to enter? (y/n): ")

main()