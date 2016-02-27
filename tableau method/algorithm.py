'''
Name : Ratnesh Chandak
Roll No: CS12B1030
Btech 4th year
file : program of simplex method in tableau form
Note : To run the program change the inputIndex in line 19 for different input file

input format in standard form:
	x1 x2 .. xn s1 s2 .. sm RHS
z
s1
s2
..
sm

'''
import os
#give the input index of file name, i.e input file name is input+inputIndex where inputIndex is an integer
inputIndex=1

def divide(A,k):
	for j in range(len(A)):
		A[j]/=float(k)

def sub(A,B):
	for j in range(len(A)):
		A[j]-=B[j]

def mult(A,k):
	for j in range(len(A)):
		A[j]*=float(k)

def colIndex(M):
	rows = len(M)
	columns = len(M[0])
	minR=M[0][0]
	colIndex=0
	for i in range(1,columns):
		if(M[0][i] < minR):
			minR=M[0][i]
			colIndex=i
	return colIndex

def rowIndex(M,colIndex):
	rows = len(M)
	columns = len(M[0])
	minratio = 99999
	rowIndex = -1
	for i in range(1,rows):
		if(M[i][colIndex] != 0 ):
			ratio = M[i][columns-1] / float(M[i][colIndex])
			if (ratio > 0 and ratio < minratio):
				minratio =ratio
				rowIndex=i
	return rowIndex

def tableau(M,rowIndex,colIndex):
	rows = len(M)
	columns = len(M[0])

	divide(M[rowIndex],M[rowIndex][colIndex])

	for i in range(rows):
		if(i!= rowIndex):
			if(M[rowIndex][colIndex] != 0):
				temp = []
			for t in range(columns):
				temp.append(M[rowIndex][t])
			mult(temp,M[i][colIndex])
			sub(M[i],temp)


M=[]
#getting input
f = open(os.getcwd()+'/input'+str(inputIndex)+'.txt', 'r')
for line in f:
        C=[]
        line=line.split(",")
        for word in line:
        	C.append(float(word))
        M.append(C)
f.close()

i=0
#check for checking unboundness 
check =0
count =0;
while(1):
	if(M[0][i] < 0):
		colIn = colIndex(M)
		rowIn = rowIndex(M,colIn)
		if(rowIn == -1):
			check = 1
			break
		else:
			tableau(M,rowIn,colIn)
		i=0
	elif (i==len(M[0])-2):
		break
	else:
		i=i+1

#printing resultant tableau

print "\n",
print M
if(check ==0):
	print "\n",
	print "Max value is: ", 
	print round(M[0][len(M[0])-1],2),
	print "\n"
else:
	print "The problem is unbounded"


