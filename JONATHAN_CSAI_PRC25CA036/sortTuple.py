n=int(input("Enter the number of tuples:"))
my_list=[]

for i in range(n):

    print(f"Enter the elements of tuples {i+1}:")
    a=int(input("Enter the first element:"))
    b=int(input("Enter the second element:"))
    my_list.append((a,b))

print("\nUnsorted List:")

for t in my_list:
    print(t)
for i in range(n):
    for j in range(0,n-i-1):

        if my_list[j][1]>my_list[j+1][1]:

            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp

print("\nSorted list based on second element:")
for t in my_list:
    print(t)