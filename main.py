from calculator import calculate_installment, quota_formatter, show_schedule
from decimal import Decimal

def main():
    try:
        quota = Decimal('100000')
        interest = Decimal('3.5')
        number_of_installments = Decimal('12')

        installment = calculate_installment(quota, interest, number_of_installments)

        print(f'Loan quota: {quota_formatter(quota)}')
        print(f'Monthly installment quota: {quota_formatter(installment)}')
        show_schedule(quota, interest, number_of_installments, installment)

    except Exception as e:
        print(f'Unexpected error: {e}')


if __name__ == '__main__':
    main()
