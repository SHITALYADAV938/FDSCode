#for multilpication
row1=int(input("enter number of rows: "))
col1=int(input("enter number of cols: "))
c=0
matrixa=[]
matrixb=[]
resultmatrix=[]
print("enter matrix  entries row wise:")
#for matrix a
print("Enter entries for matrix A:")
for i in range(row1):
    a=[]
    for j in range(col1):
        a.append(int(input()))
    matrixa.append(a)
print(matrixa)
#for printig matrix
for i in range (row1):
    for j in range(col1):
        print(format(matrixa[i][j],"<3"),end=" ")
    print()

    
#for input matrix b
row2=int(input("enter number of rows: "))
col2=int(input("enter number of cols:"))

print("Enter entries for matrix B:")
for i in range(row2):
    a=[]
    for j in range(col2):
        a.append(int(input()))
    matrixb.append(a)
print(matrixb)
#for printing matrix b
for i in range(row2):
    for j in range(col2):
            print(format(matrixb[i][j],"<3"),end=" ")
    print()
#for multilpication
for i in range(row1):
    a=[]
    for j in range(col2):
        for k in range(row2):
            c=c+matrixa[i][j]*matrixb[i][j]
        a.append(c)
        c=0
    resultmatrix.append(a)
print("result matrix:")
#for printing result
for i in range(row1):
    for j in range(col2):
        print(format(resultmatrix[i][j],"<3"),end=" ")
    print()
