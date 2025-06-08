from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP, getcontext, InvalidOperation

getcontext().prec = 10

def calculate_installment(quota, interest, number_of_installments, capitalization='monthly'):
    try:
        quota = Decimal(quota)
        interest = Decimal(interest)/Decimal('100')
        number_of_installments = Decimal(number_of_installments)
        periods = {
            'yearly': Decimal('1'),
            'half_yearly': Decimal('2'),
            'quarterly': Decimal('4'),
            'monthly': Decimal('12')
        }

        m = periods[capitalization]
        r = interest / m
        factor = (Decimal('1') + r) ** number_of_installments
        installment = quota * (r * factor)/ (factor - Decimal('1'))

        installment = installment.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return installment

    except ZeroDivisionError:
        return 'Error: Can\'t divide by zero'
    except KeyError:
        return 'Error: Invalid capitalization period'
    except InvalidOperation:
        return 'Error: Invalid input data'


def quota_formatter(quota, currency='PLN'):
    try:
        if isinstance(quota, str):
            return quota

        quota = Decimal(quota)
        quota_str = '{:,.2f}'.format(quota)
        quota_str = quota_str.replace(',', ' ').replace('.', ',')

        return f'{quota_str} {currency}'

    except:
        return 'Error: Can\'t convert quota to decimal'

def show_schedule(quota, interest, number_of_installments, installment):
    left = Decimal(quota)
    print('Payment schedule:')
    print(f"{'interest number':>6} {'Installment':>15} {'Left':>15}")
    print("-"*38)

    for nr in range(1, int(number_of_installments) + 1):
        print(f"{nr:>6} {quota_formatter(quota):>15} {quota_formatter(left):>15}")
        left -= installment
        left = left.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
