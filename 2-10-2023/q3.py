def calculate_tax(bill, tax_rate):
    tax_amount = (bill * tax_rate) / 100.00
    print('Total Tax:', tax_amount)
    return tax_amount

calculate_tax(175.00, 15)
calculate_tax(164.33, 22)
