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