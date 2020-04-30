from Week_2.Chapter_11.section_3_11.mytime import MyTime

tim1 = MyTime(2, 40, 30)
tim2 = MyTime(3, 21, 15)
target = MyTime (2, 59, 31)

print(target.between(tim1, tim2))