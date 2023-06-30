#寫一程式使用含數計算加、減、乘、除及回傳絕對值

import math

a = int(input("輸入數字: "))
b = int(input("輸入數字: "))
m = input("請輸入數字符號: ")

def mid(a, b, m):
    if m == "+":
        return a + b
    elif m == "-":
        return a - b
    elif m == "*":
        return a * b
    elif m == "/":
        return a / b
    
print("計算結果轉成絕對值: ", math.fabs(mid(a, b, m)))



     
