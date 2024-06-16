
def month_to_season(num):
    if num == 3 or num == 4 or num == 5:
        print ('Весна')
    elif num == 6 or num == 7 or num == 8:
        print ('Лето')
    elif num == 9 or num == 10 or num == 11:
        print ('Осень')
    elif num == 12 or num == 1 or num == 2:
        print ('Осень')
    else: 
        print ('Нет такого месяца')

month_to_season (float(input("Введите номер месяца")))