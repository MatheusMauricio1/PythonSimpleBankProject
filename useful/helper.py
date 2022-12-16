from datetime import date
from datetime import datetime


def date_to_str(date1: date) -> str:
    return date1.strftime('%d/%m/%Y')


def str_to_date(date1: str) -> date:
    return datetime.strptime(date1, '%d/%m/%Y')


def format_float_to_currency(num: float) -> float:
    return f'$''{:.2f}'.format(num)




