# import random

# print(random.randint(3,30))
# print(random.random())
# print(random.randrange(7,77,5))
# list=['1','2','3','4','5','6','7']
# random.shuffle(list)
# print(list)
# print(random.choice(list))
# print(random.choices(list,k=3))
# print(random.sample(list,4))
# print(random.uniform(7,9))
# print(0.1 + 0.2 == 0.3)  # Це повертає False
# print('TestHook'.removesuffix('Test'))
# print('TestHook'.removesuffix('Hook'))

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     print(s,c)
#     MAP[ord(s)] = c
    
#     MAP[ord(s.lower())] = c
    
# result = "34 DF 56 aC".translate(MAP)
# print(result)

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v

# string = "Hello world"

# result = ""

# for ch in string:
#     print(ch)
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)
# print(table_morze_dict)
# import re

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match)
# else:
#     print("Не знайдено.")

# numbers = [1,2,3,4,5]
# head = '|{:^25}|{:^25}|{:^25}|'.format('int','int^2','int^3')
# separator='*'*len(head)
# body=''
# for n in numbers:
#     body+='|{:^25}|{:^25}|{:^25}|\n'.format(n,n**2,n**3)

# table="\n".join([separator,head,separator,body,separator])
# print(table)

# from datetime import datetime, timedelta
# import random 

# def det_birthdays (n):

#     current_time = datetime.now()
#     oldest_birthday = current_time - timedelta(days=77*365)

#     birthday_list=[]

#     for i in range(n):
#         random_year = random.randrange(oldest_birthday.year,current_time.year)
#         random_month = random.randint(1,12)
#         random_date = random.randint(1,31)
#         random_birthday=datetime(year=random_year,month=random_month,day=random_date)
#         if current_time >= random_birthday:
#             birthday_list.append(random_birthday.date())
#     return birthday_list

# print(random.sample(det_birthdays(7),k=3))
# from datetime import datetime, date, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def date_to_string(date_obj):
#     return date_obj.strftime("%Y.%m.%d")


# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         birthday = user["birthday"]
#         if isinstance(birthday, str):
#             birthday = string_to_date(birthday)
#         prepared_list.append({"name": user["name"], "birthday": birthday})
#     return prepared_list


# def find_next_weekday(start_date, weekday):
#     """Повертає наступну вказану дату тижня (0 = понеділок)"""
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)


# def adjust_for_weekend(birthday_date):
#     """Переносить дату на понеділок, якщо вона випадає на суботу або неділю"""
#     if birthday_date.weekday() >= 5:
#         return find_next_weekday(birthday_date, 0)
#     return birthday_date


# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     user_data = prepare_user_list(users)

#     for user in user_data:
#         original_birthday = user["birthday"]

#         # день народження в цьому році
#         try:
#             birthday_this_year = original_birthday.replace(year=today.year)
#         except ValueError:
#             # для 29 лютого — заміна на 28, якщо не високосний
#             birthday_this_year = original_birthday.replace(year=today.year, day=28)

#         # якщо вже пройшов — перевіримо дату наступного року
#         if birthday_this_year < today:
#             try:
#                 birthday_this_year = original_birthday.replace(year=today.year + 1)
#             except ValueError:
#                 birthday_this_year = original_birthday.replace(year=today.year + 1, day=28)

#         # перевірка чи в межах наступних `days` днів
#         delta_days = (birthday_this_year - today).days
#         if 0 <= delta_days <= days:
#             congratulation_date = adjust_for_weekend(birthday_this_year)
#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "congratulation_date": date_to_string(congratulation_date)
#             })

#     return upcoming_birthdays
# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.05.29"},
# ]
# print(get_upcoming_birthdays(users))


form datetime import datetime, date

def string_to_datatime (date):
    try:
        input_date = datatime.strptime(date,'%Y-%m-%d')
        diffrence = (datatime.today()-input_date).day()
        return diffrence
    except ValueError:
        print('input date format: "YYYY-MM-DD')

string = input("input date:")
print(string_to_datatime(string))