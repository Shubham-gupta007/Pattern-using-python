x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y
	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break;
		greater += 1
	return lcm  
print("x:", x ,"y:" , y,"lcm of x and y is:",  lcm(x, y))
