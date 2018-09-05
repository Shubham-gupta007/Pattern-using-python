matrix = [[1,  2,  3],
          [4,  5,  6],
          [7,  8,  9]]
upper = []
lower = []
for i in xrange(0, len(matrix)):
    for j in xrange(0, len(matrix)):
        if i<=j:
            upper.append(matrix[i][j])
	    print(upper)
        elif i>=j:
            lower.append(matrix[i][j])
	    print(lower)
        else:
            pass
upperSum = sum(upper)
lowerSum = sum(lower)
print(upperSum)
print(lowerSum)
