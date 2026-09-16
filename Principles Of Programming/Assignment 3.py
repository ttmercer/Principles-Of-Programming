#Question 1
def number_nature():
    number = int(input("Enter a number: "))
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

#Question 2
def leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

#Question 3
def student_grade():
    score = int(input("Enter the student's score (0-100): "))
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
#Question 4
def largest_of_three():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    
    print(f"The largest number is: {largest}")

#Question 5
def grade_convert():
    score = int(input("Enter a score (0-100): "))
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    else:
        grade = "F"
    
    print(f"The student's grade is: {grade}")

#Question 6
def even_numbers():
    for num in range(1, 21):
        if num % 2 == 0:
            print(num)

#Question 7
def multiplication_table():
    i=1
    number=int(input("Enter a number to print its multiplication table: "))
    while i<=10:
        print(f"{number} x {i} = {number * i}")
        i += 1

#Question 8
def question_8():
    for i in range(1,101):
        if i % 7 == 0:
            print(f"The first number divisible by 7 is: {i}")
            break

#Question 9
def question_9():
    i=0
    while i<=15:
        i+=1
        if i % 3 == 0:
            continue
        print(i)

#Question 10
def question_10():
    count = 0
    while True:
        user_input = input("Enter a number (or type 'done' to quit): ")
        if user_input.lower() == "done":
            break
        count += 1
    print(f"Total numbers entered: {count}")


print(number_nature())
print(leap_year())
print(student_grade())
print(largest_of_three())
print(grade_convert())
print(even_numbers())
print(multiplication_table())
print(question_8())
print(question_9())
print(question_10())

