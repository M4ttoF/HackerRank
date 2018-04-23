import sys

def flippingMatrix(matrix):
	sol=[]
	def findCorners(mat,row,col):
		a=max(mat[row][col], mat[(row*-1)-1][col])
		b=max(mat[row*-1 -1][col*-1 -1], mat[row][(col*-1)-1])
		return max(a,b)


	for i in range(n):
		for j in range(n):
			sol.append(findCorners(matrix,i,j))
	ans=0
	for i in sol:
		ans+=i
	return ans

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        matrix = []
        for matrix_i in range(2*n):
           matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
           matrix.append(matrix_t)
        result = flippingMatrix(matrix)
        print(result)
