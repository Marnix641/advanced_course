from Week_2.Chapter_11.section_3_11.mytime import MyTime

starting_time = MyTime(2, 40, 30)
shift_in_time = MyTime(0, 21, 15)


print(starting_time.add_time(shift_in_time))