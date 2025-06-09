from calculator import calculate_installment, quota_formatter, show_schedule
from decimal import Decimal

def main():
    try:
        input_quota = float(input("Enter quota: "))
        input_interest = float(input("Enter interest: "))
        input_number_of_installments = int(input("Enter number of installments: "))

        quota = Decimal(input_quota)
        interest = Decimal(input_interest)
        number_of_installments = Decimal(input_number_of_installments)

        installment = calculate_installment(quota, interest, number_of_installments)

        print(f'Loan quota: {quota_formatter(quota)}')
        print(f'Real loan quota: {quota_formatter(number_of_installments * installment)}')
        print(f'Monthly installment quota: {quota_formatter(installment)}')
        show_schedule(quota, interest, number_of_installments, installment)

    except Exception as e:
        print(f'Unexpected error: {e}')


if __name__ == '__main__':
    main()
