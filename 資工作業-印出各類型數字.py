# 請寫一程式，能依使用者的要求輸入數個字放入串列 若輸入數字大於 10 個 大於十個的數字則會印出 10串列 若輸入數字大於 10 個 大於十個的數字則會印出 10
# 再輸入一個數 始能完成以下
# 輸入1 印出串列每個數整數平方
# 輸入2 印出串列平均值
# 輸入3 印出串列由大到小
# 輸入4 印出串列有幾個偶數 
# 輸入錯誤跳出去


num = int(input("請輸入要輸入幾個數字"))
user = [] # 建立串列
print("請輸入 {} 個數值: ".format(num))

count = 0
for i in range(1, num + 1):
    score = int(input())
    count += 1
    if count > 10:
        score = 10
    user.append(score)

print("輸入完畢")

for i in user:
    print(i, end = " ")
    
print()

print("請輸入數字 1(整數平方) 2(平均值) 3(由大到小列印) 4(輸入串列有幾個偶數)", end = " ")

b = int(input())
if b == 1:
    for i in user:
        print("整數平方值為", i ** 2)

elif b == 2:
    mean = sum(user) / len(user)
    print("平均數", mean)


elif b == 3:
        user.sort(reverse=True)
        print("從大到小的排列 " ,user)


elif b == 4:
    count = 0
    for i in user:
        if i % 2 == 0:
            count += 1
    print("偶數有 %d 個" % (count))

else:
    print("輸入錯誤") 






     



            



 