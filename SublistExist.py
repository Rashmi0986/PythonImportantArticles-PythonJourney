test_list = [[4, 5, 7], [2, 3, 4], [9, 8, 0]]
check_matr = [[2, 3], [1, 2], [9, 0]]

res = []
for row in check_matr:
	for lst in test_list:
		if set(row).issubset(set(lst)):
			res.append(row)

print("Matrix row subsets: ", res)
