name = input("Enter your name: ")
age = int(input("Enter your age: "))
mark1,mark2,mark3=0,0,0
mark1 = float(input("Enter your first mark: "))
while mark1 < 0 or mark1 > 100:
    mark1 = float(input("Enter your first mark, it must be between 0 and 100: "))
mark2 = float(input("Enter your second mark: "))
while mark2 < 0 or mark2 > 100:
    mark2 = float(input("Enter your second mark, it must be between 0 and 100: "))
mark3 = float(input("Enter your third mark: "))
while mark3 < 0 or mark3 > 100:
    mark3 = float(input("Enter your third mark, it must be between 0 and 100: "))

average = (mark1+mark2+mark3)/3

if average >= 50 and average <= 100:
    is_passing = True
else:
    is_passing = False

print(
    f"\nHello, {name}, age {age}, has an average mark of {average:.2f}. "
    f'They have {"passed" if is_passing else "failed"} the course.')