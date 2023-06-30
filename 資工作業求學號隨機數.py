import random

# 寫一自訂模組程式
# 1. 由鍵盤輸入學號
# 2. 求得學號後兩碼至後五碼間隨機取得由使用者輸入 n 為隨機整數奇數 m 為隨機整數偶數

# 寫一自訂模組程式
# 1. 由鍵盤輸入學號
# 2. 求得學號後兩碼至後五碼間隨機取得由使用者輸入 n 為隨機整數奇數 m 為隨機整數偶數


def ccc():
    a = int(input("請輸入學號")) # 911111003
    c = int(input("請輸入數字偶數: "))
    s = int(input("請輸入數字奇數: "))
    while True:
        number = input("m/n: ")
        if number == "m":
            for a in range(c):
                a = random.randrange(0, 11003, 2)
                print("偶數",a)            
        elif number == "n":
            for a in range(s):
                a = random.randrange(1, 11003, 2)
                print("奇數",a) 

        else:
            break   
ccc()





        



   







    
    