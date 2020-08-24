score = int(input("Enter your score Here:"))
if 100>score and score>= 90:#標準寫法，通常這樣寫才過
    print("Aaa")
elif 90>score >= 80:#非標準寫法，可能只在蟒蛇限用
    print("Bbb")
elif 80>score >= 70:
    print("Ccc")
elif 70>score >= 60:
    print("Ddd")
elif 0<=score < 60:
    print("Eee")
else:
    print("不要亂來")
    