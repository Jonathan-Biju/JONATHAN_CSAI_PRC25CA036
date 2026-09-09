m=int(input("Enter the value of m:"))
n=int(input("Enter the value on n:"))

set_squares=[]

for i in range(m,n+1):
    if i%2==0:
        a=i*i
        set_squares+=[a]

setSquares=tuple(set_squares)

print(f"The set squares of numbers between {m} and {n} are:\n{setSquares}")