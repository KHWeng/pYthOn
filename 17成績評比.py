engscore = int(input("Enter your ENGLISH score Here:"))
mathscore = int(input("Enter your MATH score Here:"))
if engscore>=90 and mathscore>=90:
    print("You got a trophy!")
elif engscore<60 and mathscore<60:
    print("You got some punishment!!")
elif engscore<60 or mathscore<60:
    print("You were safe! Keep practicing!")
elif 90>engscore>=60 or 90>mathscore>=60:
    print("You were safe!")#與11、12行同意 
elif (engscore<90 and engscore>=60) or (mathscore<90 and mathscore>=60):
    print("You were safe!")#與9、10行同意，兩and條件式需括號，與or隔開!