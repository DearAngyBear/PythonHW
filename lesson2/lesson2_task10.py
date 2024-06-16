def bank (x,y):
        n = x*(1.1**y)
        print(n)

money = float(input("Введите сумму на счету "))
year = float(input('Введите количество лет '))
bank (money, year)