import datetime
date = datetime.date.today()

def moneyCollection():
    amount = input("Please enter the amount: ")
    print("Today", date.strftime("%x"), "you collected:", amount)

moneyCollection()