import os
'''

input format in standard form:
	x1 x2 .. xn s1 s2 .. sm RHS
z
s1
s2
..
sm

'''
def divide(A,k):
	for j in range(len(A)):
		A[j]/=float(k)

def sub(A,B):
	for j in range(len(A)):
		A[j]-=B[j]

def mult(A,k):
	for j in range(len(A)):
		A[j]*=float(k)

def tableau(M):
	rows = len(M)
	columns = len(M[0])
	minR=M[0][0]
	colIndex=0
	for i in range(1,columns):
		if(M[0][i] < minR):
			minR=M[0][i]
			colIndex=i

	#print colIndex

	minratio = 99999
	rowIndex = 0
	for i in range(1,rows):
		if(M[i][colIndex] != 0 ):
			ratio = M[i][columns-1] / float(M[i][colIndex])
			if (ratio > 0 and ratio < minratio):
				minratio =ratio
				rowIndex=i

	#print rowIndex

	divide(M[rowIndex],M[rowIndex][colIndex])

	for i in range(rows):
		if(i!= rowIndex):
			if(M[rowIndex][colIndex] != 0):
				temp = []
			for t in range(columns):
				temp.append(M[rowIndex][t])
			mult(temp,M[i][colIndex])
			sub(M[i],temp)

	#print M


M=[]
#getting input
f = open(os.getcwd()+'/input5.txt', 'r')
for line in f:
        C=[]
        line=line.split(",")
        for word in line:
        	C.append(float(word))
        M.append(C)
f.close()

for i in range(len(M[0])):
	if(M[0][i] < 0):
		tableau(M)

print M
print "Max value is: "
print M[0][len(M[0])-1]


