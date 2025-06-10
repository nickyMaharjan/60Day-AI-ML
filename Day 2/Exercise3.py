def tax_to_pay(salary):
    if salary <= 20000:
        tax_amount = salary * 0.1
    elif salary <= 30000:
        remaining_salary = salary - 20000
        tax_amount = (20000 * 0.1) + remaining_salary * 0.2
    elif salary <= 40000:
        remaining_salary = salary - 30000
        tax_amount = (20000 * 0.1) + (10000 * 0.2) + remaining_salary * 0.3
    else:
        remaining_salary = salary - 40000
        tax_amount = (20000 * 0.1) + (10000 * 0.2) + (10000 * 0.3) + remaining_salary * 0.4

    return tax_amount

print(tax_to_pay(15000))
print(tax_to_pay(35000))
print(tax_to_pay(42000))
print(tax_to_pay(55000))