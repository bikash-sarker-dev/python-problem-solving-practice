# Practice Problem 2: Student Grade Calculator
# Task:


student_name = input("Enter student name: ")

math_mark = int(input("Enter Math marks: "))
english_mark = int(input("Enter english marks: "))
python_mark = int(input("Enter pthon marks: "))



if math_mark < 0 or math_mark > 100 or english_mark < 0 or english_mark > 100 or python_mark < 0 or python_mark >100:
    print("this is a invalid marks")

