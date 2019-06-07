annual_salary = int(input("Type annual salary here: "))
portion_saved = float(input("Type the portion you want to save as a decimal: "))
total_cost = float(input("Type the cost of your dream house here: "))

r = 0.04
portion_down_payment = 0.25 
current_savings = 0
month = 0

while current_savings < (total_cost * portion_down_payment):
    month = month + 1
    current_savings = (current_savings) + (portion_saved*annual_salary/12) + (current_savings*r/12)
   
print(month)
