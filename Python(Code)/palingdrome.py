s = input()
q = s[::-1]
if s == q:
	print("String palingdrome: {}".format(q)) 
else:
	print("Not Palingdrome: {}".format(q))

"""
This is the Python's slice syntax of string, list, or tuple. s[::-1] returns s as reversed order
"""
