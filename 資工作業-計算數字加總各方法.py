# 利用迴圈寫一個程式 
# 1. 輸入 1 印出 1-10之間偶數加總
# 2. 輸入 2 印出 1-10之間奇數加總
# 3. 輸入3 印出 1- 10 之間數 當數字為5 迴圈中止執行
# 4. 輸入E印出姓名及學號 終止執行





while True:
    number = (input("請輸入數字: "))
    if number == "1":
        x = 0
        for i in range(0, 11, 2):
            x += i
        print("x=%d" % x)

    elif number == "2":
        y = 0
        for j in range(1, 11, 2):
            y += j
        print("y=%d" % y)
    elif number == "3":
        for k in range(1, 11):
            print(k)

            if k == 5:
                break
        print()
    elif number == "E":
        print("姓名:  學號: ")

    else:
        print("輸入錯誤終止程式")                            

