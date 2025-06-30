from decimal import Decimal, ROUND_DOWN
from calculator import quota_formatter
import csv

def export_schedule_to_csv(number_of_installments, installment):
    real_quota = installment * number_of_installments
    left = Decimal(real_quota)
    with open('schedule.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Interest number", "Installment", "Left"])
        for nr in range(1, int(number_of_installments) + 1):
            writer.writerow([nr, quota_formatter(installment), quota_formatter(left)])
            left -= installment
            left = left.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
