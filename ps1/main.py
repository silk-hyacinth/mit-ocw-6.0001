#12/24/2021
#pset 1, attempt 2

semi_annual_raise = 0.07
portion_down_payment = 0.25
total_cost = 1000000
annual_salary = int(input("Enter the starting salary: "))
epsilon = 100
r = 0.04
down_payment = portion_down_payment*total_cost

low = 0
high = 10000
guess = (high + low) / 2
num_guesses = 0
annual = annual_salary
current_savings = 0

while abs(current_savings-down_payment) >= epsilon and guess <= 9999:
    boo = False
    current_savings = 0
    for i in range(36):
        if not boo:
            annual = annual_salary
        if i % 6 == 0 and i > 1:
            annual += annual*semi_annual_raise
            boo = True

        current_savings += current_savings*r/12
        current_savings += (annual/12)*(guess/10000)

        #print(current_savings)

    if (current_savings - portion_down_payment) < down_payment:
        low = guess
        #print(guess)
        #print("current savings is " + str(current_savings))
        if guess >= 9999:
            break

    elif abs(current_savings-down_payment) <= epsilon/10000:
        break
    else:
        high = guess
        #print(guess)
        #print("current savings is " + str(current_savings))

    #int
    #guess = (high + low)//2
    #float
    guess = (high + low) / 2

    num_guesses += 1

interest = guess/10000

if guess < 9999:
    print("Best savings rate: " + str(interest)[0:6])
    print("Steps in search: " + str(num_guesses))
else:
    print("It is not possible to pay the down payment in three years.")
