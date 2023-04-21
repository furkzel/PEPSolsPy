import time

def is_it_leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            return False
        else:
            return True
    else:
        return False

months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def get_day_of_week(day, month, year):
    days_passed = 0
    for i in range(1900, year):
        if is_it_leap_year(i):
            days_passed += 366
        else:
            days_passed += 365
    for i in range(1, month):
        if i == 2 and is_it_leap_year(year):
            days_passed += 29
        else:
            days_passed += months[list(months.keys())[i-1]]
    days_passed += day - 1
    return days[days_passed % 7]

def main():
    result = []

    for i in range(1901, 2000):
        for j in range(1, 13):
            if get_day_of_week(1, j, i) == 'Sunday':
                result.append(('1st of', list(months.keys())[j-1], i, 'is a Sunday'))
    
    return len(result)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Time taken: {} seconds'.format(time.time() - start_time))