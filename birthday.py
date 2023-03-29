import datetime as dt

def get_days_until_birthday(month, day):

    today = dt.date.today()

    birthday = dt.date(today.year, month, day)

    if birthday < today:
        birthday += dt.timedelta(years = 1)

    return (birthday - today).days

print(get_days_until_birthday(3,22))