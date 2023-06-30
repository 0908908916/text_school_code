# 寫一個程式能計算一個文字檔內資料, 要求如下
# 請自行建立一個文字檔, 內有中文、英文、數字及大小寫英文字母
# 計算出以下各項
# 1.  文字檔內有多少字?
# 2.  文字檔內有多少英文字? 數字?
# 3.  文字檔內有多少大寫英文字? 小寫英文字?


def count(file_path):
    with open(file_path, "r", encoding="utf-8") as f: #打開讀取這個檔案
        content = f.read() #使用讀取的功能把它讀取
        characters = len(content) # 算總字數的數量
        letters = sum(1 for char in content if char.isalpha()) # 算英文字母的總數量 char 為字元 比如 char(65) 表示 a 這樣為一個字元 所以用它來轉換 英文
        digits = sum(1 for char in content if char.isdigit()) # 算數字的總數量 數字1代表他可以跑一次迴圈執行整行 如果2變成執行兩次
        uppercase = sum(1 for char in content if char.isalpha() and char.isupper()) # 算英文字母大寫的總數量
        lowercase = sum(1 for char in content if char.isalpha() and char.islower()) # # 算英文字母小寫的總數量

        # 去除空格後的字數
        without = content.replace(" ","")
        characters_without = len(without)

        return characters_without, characters, letters, digits, uppercase, lowercase
    



file_path = "文字.txt" # 用函數把打好的文字檔使用 算裡面的字數等....

without_char ,char, letter, digit, uppercase, lowercase = count(file_path) # 在自己設變數 轉成這個函數 以下把他打印出來

print("總字數不含空格:", without_char)
print("總字數:", char)
print("英文字母數量:", letter)
print("數字數量:", digit)
print("大寫英文字母數量: ", uppercase)
print("小寫英文字母數量: ", lowercase)
