## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0.0
r = 0.05


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
months = 0
# advance each month until amt saved is enough for down pmt
while amount_saved < cost_of_dream_home*portion_down_payment:
	amount_saved += amount_saved*r/12
	amount_saved += yearly_salary/12*portion_saved
	# check for raise month (6, 12, 18, etc.)
	if months > 0 and months%6 == 0:
		yearly_salary *= (1+semi_annual_raise)
	months += 1
print(f'Number of months: {months}')
