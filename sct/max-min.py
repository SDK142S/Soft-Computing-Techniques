R=[]
S=[]
r1=int(input("enter the row of first matrix:"))
c1=int(input("enter the column of first matrix:"))
r2=int(input("enter the row of second matrix:"))
c2=int(input("enter the column of second matrix:"))
print("Relation R")
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(float(input("enter the value : ")))
    R.append(a)
print("Relation S")
for i in range(r2):
    a=[]
    for j in range(c2):
        a.append(float(input("enter the value : ")))
    S.append(a)

result=[]
for i in range(r1):
    result.append([])
    for j in range(c2):
        result2=[]
        for k in range(r2):
            result2.append(min(R[i][k],S[k][j]))
        result[i].append(max(result2))
    print("\n")
for i in range(r1):
    for j in range(c2):
        print(result[i][j],end=" ")
    print("\n")


