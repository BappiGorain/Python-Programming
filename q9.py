try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        if num2 == 0:
                print("Cannot divide by zero")
        else:
		print(num1 / num2)
except ValueError:
	print("Enter interger values")
