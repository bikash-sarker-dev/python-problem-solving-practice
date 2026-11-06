# Practice Problem 2: Student Grade Calculator
# Task:


student_name = input("Enter student name: ")

math_mark = int(input("Enter Math marks: "))
english_mark = int(input("Enter english marks: "))
python_mark = int(input("Enter pthon marks: "))



if math_mark < 0 or math_mark > 100 or english_mark < 0 or english_mark > 100 or python_mark < 0 or python_mark > 100:
    print("this is a invalid marks")

else:
    all_subject_mark = math_mark + english_mark + python_mark
    average_mark = all_subject_mark / 3


    print(average_mark)

    if average_mark >= 80:
        # print(f"Final Grade: A+")
        grade = "A+"
    elif average_mark >= 70:
        # print(f"Final Grade: A")
        grade = "A"
    elif average_mark >= 60:
        # print(f"Final Grade: A-")
        grade = "A-"
    elif average_mark >= 50:
        # print(f"Final Grade: B")
        grade = "B"
    elif average_mark >= 40:
        # print(f"Final Grade: C")
        grade = "C"
    else:
        print(f"Final Grade: F")
        grade = "F"


    print(f"Student Name: {student_name}")
    print(f"Average Marks: {round(average_mark, 2)}")
    print(f"Final Grade: {grade}")