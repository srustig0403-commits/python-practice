name, monthly_fee, number_of_months, trainer_fee, discount = 'srusti', 500, 5, 300, 100

total_fee = monthly_fee * number_of_months

final_payment = total_fee + trainer_fee - discount

print('Customer Name =', name)
print('Final Payment =', final_payment)
