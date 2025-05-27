"""ДЗ. Завдання №1"""

from datetime import datetime, date

# def get_days_from_today (date):
#     try:
#         input_date = datetime.strptime(date,'%Y-%m-%d')
#         diffrence = datetime.today()-input_date
#         return diffrence.days
#     except ValueError:
#         print('input date format: "YYYY-MM-DD')


# print(get_days_from_today("2026-12-27"))

"""ДЗ. Завдання №2"""
# from random import sample

# def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
 
#     if not (isinstance(min_value, int) and isinstance(max_value, int) and isinstance(quantity, int)):
#         return []

#     if min_value <= 0 or max_value >= 1001:
#         return []

#     if quantity <= 0 or quantity > (max_value - min_value + 1):
#         return []

#     return sorted(sample(range(min_value, max_value + 1), k=quantity))

# try:
#     min_val = int(input("min: "))
#     max_val = int(input("max: "))
#     quantity = int(input("quantity: "))

#     result = get_numbers_ticket(min_val, max_val, quantity)
#     if result:
#         print("Згенеровані числа:", result)
#     else:
#         print("Некоректні вхідні дані.")
# except ValueError:
#     print("Будь ласка, введіть цілі числа.")

import re

def normalize_phone(phone_numb):
    l = []
    l = re.split(r'\D',phone_numb)
    str_number=''.join(l)
    index_0 = str_number.find('0')
    str_number=str_number[index_0:]
    str_number='+38'+str_number

    return str_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
