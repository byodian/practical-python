# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

#while principal > 0:
#    principal = principal * (1 + rate/12) - payment
#    total_paid = total_paid + payment

#print('Total paid', total_paid)

# Exercise 1.8:Extra payments
extra_payment = 1000
extra_months = 12

while principal > 0:
    if extra_months > 0:
        principal = principal * (1 + rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment
    
    extra_months = extra_months - 1

print('Total Paid', total_paid)
