def gcd(x, y):
	while(y):
		x, y = y, x% y
	return x
def lcm(x, y):
	lcm = (x*y)//gcd(x, y)
	return lcm

num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))

print("num1:",num1, "num2", num2,"lcm is:",lcm(num1, num2))
print("num1:",num1, "num2", num2,"gcd is:",gcd(num1, num2))
