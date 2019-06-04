annual_salary = int(input("Type annual salary here:"))
portion_saved = float(input("Type the portion you want to save (as a decimal):"))
total_cost = float(input("Type the cost of your dream house here:"))

monthly_salary = (annual_salary / 12.0)
portion_down_payment = .25 * total_cost
current_savings = 0
rate = .04/12
monthly_savings = monthly_salary * portion_saved

i = 0
while (current_savings <= portion_down_payment):
    current_savings = current_savings + (monthly_savings) * rate + monthly_savings
    i = i+1
print(i)
