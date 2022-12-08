def is_leap_year(years):
    if  years % 100 == 0:
        if years % 400 == 0:
            return True
        else:
            return False
    else:
        if years % 4 == 0:
            return True
        else:
            return False

def split(date):
    days = int(date[0:2])
    months = int(date[3:5])
    years = int(date[6:8])

def is_format(date):
    k = len(date)
    if k == 8:
        return True
    else:
        return False
