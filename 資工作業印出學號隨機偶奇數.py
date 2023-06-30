import random

# 寫一自訂模組程式
# 1. 由鍵盤輸入學號
# 2. 求得學號後兩碼至後五碼間隨機取得由使用者輸入 n 為隨機整數奇數 m 為隨機整數偶數

def ccc():
    a = int(input("請輸入學號")) # 911111003
    for a in range(8):
        a = random.randint(3, 11003)
        if a % 2 == 0:
            print("偶數",a)
        else:
            print("奇數:",a)


ccc()





        



   







    
    