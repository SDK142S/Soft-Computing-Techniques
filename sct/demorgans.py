X={}
Y={}
Z={}
C={}
print('enter the fuzzy set X :')
for i in range(1,5):
    X[i]=float(input('enter the element:'))

print('enter the fuzzy set Y :')
for i in range(1,5):
    Y[i]=float(input('enter the element:'))
print(X)
print(Y)
print("\n")
def union(X,Y):
    for i in X and Y:
        Z[i]=round(max(X[i],Y[i]),2)
    return Z
def intersection(X,Y):
    for i in X and Y:
        Z[i]=round(min(X[i],Y[i]),2)
    return Z
    
def compliment(Z):
    for i in Z:
        C[i]=round(1-Z[i],2)
    return C    

if compliment(union(X,Y)) and intersection(compliment(X),compliment(Y)):
    print("demorgan low is verified")
    print("(XUY)'=",compliment(union(X,Y)))
    print("(X'|Y')=",intersection(compliment(X),compliment(Y)))



