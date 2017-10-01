import math 

def prod_non_zero_diag(x):
	res = 1
    for i in range(len(x)):
        for j in range(len(x[i])):
            if (i == j) & (x[i][j] != 0):
                res = res * x[i][j]
    return res
	
	
def are_multisets_equal(x,y):
	return set(x).issubset(set(y)) & set(y).issubset(set(x))


def max_after_zero(x):
	res = []
	for i in range(1,len(x)):
		if x[i-1] == 0:
			res.append(x[i])
			print(res)
	return max(res)
	

def convert_image(z, coefs=[0.299, 0.587, 0.114]):
	new_matrix = []
	height = len(z)
	width = len(z[0])
	for i in range(height):
		new_row = []
		for j in range(width):
			new_row.append(z[i][j][0] * coefs[0] + z[i][j][1] * coefs[1] + z[i][j][2] * coefs[2])
		new_matrix.append(new_row)
	return new_matrix
	
	
def run_length_encoding(x):
	cnt = []
	[x.count(i) for i in set(x)]
	for i in set(x):
		cnt.append(x.count(i))
	result = (set(x), cnt)
	return result
	
	
def pairwise_distance(x,y):
    dist_matrix = []
    for i in y:
        row=[]
        for j in x:
            row.append(math.sqrt((j - i) ** 2))
        dist_matrix.append(row)
    return dist_matrix
	

