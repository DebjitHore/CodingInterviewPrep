a = input("Please enter a number:")
try:
    b = int(float(a))
    print("The integer typecast value is", b)
except ValueError:
    print("Please type an integer")
