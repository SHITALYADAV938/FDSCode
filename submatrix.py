#for addition of matrix
row=int(input("enter no of row "))
col=int(input("enter no of col "))
matrixa=[]
matrixb=[]
resultmatrix=[]
print("enter matrix  entries row wise:")
print("Enter entries for matrix a:")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrixa.append(a)
print(matrixa)
#for printig matrix a
for i in range (row):
    for j in range(col):
        print(format(matrixa[i][j],"<3"),end=" ")
    print()
    
#for input matrix b
print("Enter entries for matrix B:")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrixb.append(a)
print(matrixb)
#for printing matrix b
for i in range(row):
    for j in range(col):
        print(format(matrixb[i][j],"<3"),end="")
    print()
#for addition
for i in range(row):
    a=[]
    for j in range(col):
        a.append(matrixa[i][j]-matrixb[i][j])
    resultmatrix.append(a)
print(resultmatrix)
#for printing matrix 
for i in range(row):
    for j in range(col):
        print(format(resultmatrix[i][j],"<3"),end="")
    print()
