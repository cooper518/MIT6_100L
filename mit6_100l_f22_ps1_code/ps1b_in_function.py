def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	return months