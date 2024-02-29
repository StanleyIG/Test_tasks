# Способ №2 предпочтительнее

# Способ №1
def hours_sec(h1, min1, s1, h2, min2, s2):
    """остаток секунд в дне"""
    seconds_per_day = 24 * 60 * 60
    seconds_day1 = h1 * 60 * 60 + min1 * 60 + s1
    seconds_day2 = h2 * 60 * 60 + min2 * 60 + s2
    return ((seconds_per_day - seconds_day1) - (seconds_per_day - seconds_day2)) % seconds_per_day

def get_days_seconds(y1, month1, d1, h1, min1, s1, y2, month2, d2, h2, min2, s2):
    """функция конвертирует дни в секунды и выводит конечный результат работы 
    get_days_seconds и hours_sec"""
    seconds_per_day = 24 * 60 * 60
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    
    # подсчёт дней по годам
    for _ in range(y1, y2):
        days += 365
    
    # подсчёт дней по месяцам
    for month in range(month1 - 1, month2):
        if month == month1 - 1:   
            days += days_in_month[month] - d1
        elif month == month2 - 1:
            days += d2
        else:
            days += days_in_month[month]
            
    sec = hours_sec(h1, min1, s1, h2, min2, s2)
    # результат округляется автоматичесски в большую или меньшую сторону     
    days = round(((days * seconds_per_day) - sec) / seconds_per_day)
    return days, sec


# date1 = list(map(int, input().split()))
# date2 = list(map(int, input().split()))
# days, seconds = get_days_seconds(*date1, *date2)
# print(days, seconds)


# Способ №2
def date_to_seconds(y, month, d, h, m, s):
    """конвертация даты в секунды"""
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = (y-1) * 365 + sum(months[:month-1]) + (d-1)
    seconds = days * 24 * 60 * 60 + (h-1) * 60 * 60 + (m-1) * 60 + s
    return seconds

def get_days_seconds(date1, date2):
    seconds_per_day = 24 * 60 * 60
    difference = date2 - date1
    # из секунд в дни -> число полных дней
    days = difference // seconds_per_day
    # остаток от разницы, число секунд
    seconds = difference % seconds_per_day
    return days, seconds

date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))
days, secs = get_days_seconds(date_to_seconds(*date1), date_to_seconds(*date2))
print(days, secs)

