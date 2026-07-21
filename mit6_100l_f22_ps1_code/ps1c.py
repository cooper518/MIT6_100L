## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
amount_saved = 0.0
high = 1.0
low = 0.0
r = 0.5
amount_needed = 200_000.0
months = 36
epsilon = 100.0
steps = 0
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while abs(amount_needed-amount_saved) > epsilon:
	amount_saved = initial_deposit*(1+(r/12))**months
	if r>0.99:
		r = None
		break
	if amount_saved < amount_needed:
		low = r
	else:
		high = r
	r = (high+low)/2.0
	steps += 1
print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')
