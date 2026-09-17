def add_numbers(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        return "Both numbers must be positive."


    #WAP to calculate area of a rectangle

    def area_of_rectangle(length, width):
        if length > 0 and width > 0:
            return length * width
        else:
            return "Length and width must be positive."

    def area_of_circle(radius):
        if radius > 0:
            return 3.14 * radius * radius
        else:
            return "Radius must be positive."æææææ\

    def menu():
        print("Select an option:")
        print("1. Add two numbers")
        print("2. Calculate area of a rectangle")
        print("3. Calculate area of a circle")
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = add_numbers(a, b)
            print(f"Result: {result}")
        elif choice == 2:
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            result = area_of_rectangle(length, width)
            print(f"Area of rectangle: {result}")
        elif choice == 3:
            radius = float(input("Enter radius of circle: "))
            result = area_of_circle(radius)
            print(f"Area of circle: {result}")
        else:
            print("Invalid choice. Please select a valid option.")


    def classify_temperature(temp):
        if temp < 0:
            return "Freezing"
        elif 0 <= temp < 10:
            return "Cold"
        elif 10 <= temp < 20:
            return "Cool"
        elif 20 <= temp < 30:
            return "Warm"
        else:
            return "Hot"

        def classify_temperature(temp):
            temp = float(input("Enter the temperature in Celsius: "))
            if temp < 0:
                print("Freezing")
            elif 0 <= temp < 10:
                print("Cold")
            elif 10 <= temp < 20:
                print("Cool")
            elif 20 <= temp < 30:
                print("Warm")
            else:
                print("Hot")