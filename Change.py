def calculate_due_amount(bill_amount, amount_paid):
    return amount_paid - bill_amount

bill = 8.45
paid = 10.00

change = calculate_due_amount(bill, paid)

print(f"The shopkeeper should return ${change:.2f}")