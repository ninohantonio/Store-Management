from datetime import datetime


def get_date_time_to_string() -> str:
    date = datetime.now()
    date = str(date)
    date = date.split('.')
    return date[0]

def get_date_to_string() -> str:
    date = datetime.now()
    date = str(date)
    date = date.split(' ')
    return date[0]

