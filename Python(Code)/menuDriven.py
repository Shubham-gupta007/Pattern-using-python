def add(x, y):
	return x + y
def sub(x, y):
	return x - y

print("Select operation")
print("1.add")
print("2.sub")

choice = input("Enter choice 1 & 2:")

num1 = int(input("Enter the value of x :"))
num2 = int(input("Enter the value of y :"))

if choice == '1':
	print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
	print(num1, "-", num2, "=", sub(num1,num2))

else:
	print("invalid input")
