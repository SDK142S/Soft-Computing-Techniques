X = {}
Y = {}
# No. of inputs by the user
n = int(input('No of inputs in first set: '))

print("Enter the values in first set X:\n")
while n != 0:
    key, value = input().split()
    X[key] = float(value)  # Convert the input value to a float
    n -= 1

m = int(input('No of inputs in second set: '))

print("Enter the values in second set Y:\n")
while m != 0:
    key, value = input().split()
    Y[key] = float(value)  # Convert the input value to a float
    m -= 1

print("Values in the first set X is:\n")
print(X)

print("Values in the second set Y is:\n")
print(Y)

Z = {}

# Calculate the complement of X
complement_X = {}
for key in X:
    complement_X[key] = 1.0 - X[key]

# Calculate the complement of Y
complement_Y = {}
for key in Y:
    complement_Y[key] = 1.0 - Y[key]

print("Complement of X:")
print(complement_X)

print("Complement of Y:")
print(complement_Y)
print("\n")
print("\n")
print("\n")

z={}
print("Demorgans Law\n")
print("***************************\n")
print("First theroam")
print("X compliment intersection y compliment = (X union Y )compliment\n\n")
print("X compliment intersection y compliment :")
for i in complement_X and complement_Y:
    Z[i]=min(complement_X[i],complement_Y[i])
print(Z)
V={}
for i in X and Y:
    if(X[i]>Y[i]):
        V[i]=X[i]
    else:
        V[i]=Y[i]

print("(X union Y )compliment:")
complement_V = {}
for key in V:
    complement_V[key] = 1.0 - V[key]
print(complement_V)
print("\nFirst theoram statisfied\n")

print("***************************\n")
print("Second theroam")
print("X compliment union y compliment = (X intersection Y )compliment\n\n")
print("X compliment union y compliment :")
for i in complement_X and complement_Y:
    Z[i]=max(complement_X[i],complement_Y[i])
print(Z)
V={}
for i in X and Y:
    if(X[i]<Y[i]):
        V[i]=X[i]
    else:
        V[i]=Y[i]

print("(X intersection Y )compliment:")
complement_V = {}
for key in V:
    complement_V[key] = 1.0 - V[key]
print(complement_V)
print("\nSecond theoram statisfied\n")

print("***************************\n")
