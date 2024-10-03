import csv

def month_from_number(num):
    while True:
        if num == 1:
            return 'January'
            break
        elif num == 2:
            return 'February'
            break
        elif num == 3:
            return 'March'
            break
        elif num == 4:
            return 'April'
            break
        elif num == 5:
            return 'May'
            break
        elif num == 6:
            return 'June'
            break
        elif num == 7:
            return 'July'
            break
        elif num == 8:
            return 'August'
            break
        elif num == 9:
            return 'Septemeber'
            break
        elif num == 10:
            return 'October'
            break
        elif num == 11:
            return 'November'
            break
        elif num == 12:
            return 'December'
            break
        else:
            return 'Month must be 1-12.'
            break

def read_in_file(file_name):
    list = []
    file = open(file_name, encoding="utf-8")
    file_csv = csv.reader(file)
    for line in file_csv:
        contents = line
        list.append(contents)
    return list
    file.close()

def create_reported_date_dict(lst):
    dict = {}
    for item in lst[1:]:
        reported_date = item[1]
        if reported_date in dict:
            dict[reported_date] += 1
        else:
            dict[reported_date] = 1
    return dict

def create_reported_month_dict(lst):
    dict = {}
    for item in lst[1:]:
        date_str = item[1]
        month = int(date_str.split('/')[0])
        if month in dict:
            dict[month] += 1
        else:
            dict[month] = 1
    return dict

def create_offense_dict(lst):
    dict = {}
    for item in lst[1:]:
        crime = item[7]
        if crime in dict:
            dict[crime] += 1
        else:
            dict[crime] = 1
    return dict

def create_offense_by_zip(lst):
    dict = {}
    for sublist in lst[1:]:
        offense = sublist[7]
        zip_code = sublist[13]
        if offense not in dict:
            dict[offense] = {}
        if zip_code not in dict[offense]:
            dict[offense][zip_code] = 0
        dict[offense][zip_code] += 1
    return dict
    
    
while True:    
    try:
        input_file_name = input('Enter the name of the file: ')
        input_file = open(input_file_name, 'r')
        break
    except IOError:
        print(f'Could not open file {input_file_name}')
        print()

data = read_in_file(input_file_name)
offenses_by_month = create_reported_month_dict(data)
offenses_by_type = create_offense_dict(data)
offenses_by_zip = create_offense_by_zip(data)
max_month = max(offenses_by_month, key = offenses_by_month.get)
max_offense = max(offenses_by_type, key = offenses_by_type.get)
print(f'The month with the highest number of crimes is {month_from_number(int(max_month))} with {offenses_by_month[max_month]} offenses.')
print(f'The offense with the highest number of crimes is {max_offense} with {offenses_by_type[max_offense]} offenses.')

offense = input('Enter an offense: ')
while offense not in offenses_by_type:
    print('Offense not found, enter offense: ')
    offense = input('Enter an offense: ')

print(f'{offense} offenses by ZIP Code:')
print()
print(f'Zip Code          Number of Offenses')
print('======================================')
for zip_code, num_offenses in offenses_by_zip[offense].items():
    print(f'{zip_code}            {num_offenses}')

