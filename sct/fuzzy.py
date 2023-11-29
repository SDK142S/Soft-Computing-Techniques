'''X={'a':0.7,'b':0.3,'c':0.2}
Y={'a':0.5,'b':0.2,'c':0.4}'''
Z={}
X={}
Y={}
print('enter the fuzzy set X :')
for i in range(1,5):
    X[i]=float(input('enter the element:'))

print('enter the fuzzy set Y :')
for i in range(1,5):
    Y[i]=float(input('enter the element:'))
print(X)
print(Y)

print("union")
for i in X and Y:
    if(X[i]>Y[i]):
        Z[i]=X[i]
    else:
        Z[i]=Y[i]
print(Z)

print("intersection")
for i in X and Y:
    Z[i]=min(X[i],Y[i])
print(Z)

print("Algebraic sum")
for i in X and Y:
    Z[i]=X[i]+Y[i]-(X[i]*Y[i])
print(Z)

print("Bounded sum")
for i in X and Y:
    Z[i]=round(min(1,X[i]+Y[i]),2)
print(Z)

print("Bounded diff")
for i in X and Y:
    Z[i]=round(max(0,X[i]+Y[i]),2)
print(Z)












