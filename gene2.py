

def solution(A, D):
    def calculate_final_balance(income, card_payments):
        total_fee = 0
        for month_payments in card_payments.values():
            total_fee -= 5 if month_payments >= 100 else 5 * 12
        return income + total_fee

    total_income = 0
    card_payments = (int)

    for amount, date in zip(A, D):
        year, month, _ = map(int, date.split("-"))
        if amount >= 0:
            total_income += amount
        else:
            card_payments[(year, month)] += abs(amount)

    return calculate_final_balance(total_income, card_payments)

