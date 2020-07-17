# Ask for user input
annual_salary = float(input('What is your annual salary?: '))
portion_saved = float(input('What portion of your salary is saved each month?:'))
total_cost = float(input('What is the total cost of your dream house?: '))

# Given Parameters
yearly_r = 0.04
portion_down_payment = 0.25
current_savings = 0

monthly_salary = annual_salary/12
total_down_payment = total_cost*portion_down_payment
monthly_r = 0.04/12

number_of_months = 0
while current_savings < total_down_payment:
    number_of_months += 1
    current_savings += current_savings * monthly_r
    current_savings += monthly_salary*portion_saved

print('it will take {} months to save for your dream house'.format(number_of_months))


