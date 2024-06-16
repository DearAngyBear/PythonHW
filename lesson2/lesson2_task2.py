Year = int(input("Введите год для проверки "))
def is_year_leap (x):
    if (x % 4 == 0):
        result = True
    else:
        result = False   
    return result

result = is_year_leap(Year)

print('Год', Year, ':', result)