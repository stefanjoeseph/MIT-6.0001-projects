user_annual_salary = float(int(input('What is your annual salary?: ')))
annual_salary = user_annual_salary

total_cost = 1000000
semi_annual_raise = 0.07

yearly_r = 0.04
portion_down_payment = 0.25
current_savings = 0
current_month = 0

monthly_salary = annual_salary / 12
# total_down_payment = total_cost*portion_down_payment
total_down_payment = 250000
monthly_r = 0.04 / 12

low = 0
high = 1000

steps_in_search = 0

while True:
    steps_in_search += 1
    # Check if possible to buy in 3 years
    if steps_in_search == 1:

        flag = False
        while current_month < 36:
            current_savings += current_savings * monthly_r
            current_savings += monthly_salary

            if current_month % 6 == 0 and current_month != 0:
                annual_salary *= 1 + semi_annual_raise
                monthly_salary = annual_salary / 12
            current_month += 1

        if (current_savings - 250000) < 0:
            print('it is not possible to save for a house in 3 years')
            flag = True
            break

    # reset necessary variables
    annual_salary = user_annual_salary
    monthly_salary = user_annual_salary / 12
    current_month = 0
    current_savings = 0

    # Make guess
    portion_saved = (high + low) / (2.0)


    while current_month < 36:

        current_savings += current_savings * monthly_r
        current_savings += monthly_salary * portion_saved / 1000

        if current_month % 6 == 0 and current_month != 0:
            annual_salary *= 1 + semi_annual_raise
            monthly_salary = annual_salary / 12
        current_month += 1

    difference = current_savings - 250000

    # Check where to set upper and lower bound of the search or if necessary difference has been reached
    if abs(difference) < 100:
        break

    elif difference > 100:
        high = portion_saved

    elif difference < -100:
        low = portion_saved


if flag == False:
    print('steps in bisection search: ', steps_in_search)
    print('The optimum savings rate is: {}'.format(portion_saved / 1000))





