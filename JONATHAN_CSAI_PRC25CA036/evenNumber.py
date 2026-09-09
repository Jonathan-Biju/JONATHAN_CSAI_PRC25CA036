n=int(input("Enter the value of n:"))

nums=[]

for i in range(n):
    num=int(input(f"Enter the {i+1}th number:"))
    nums.append(num)

evenNums=[]

for num in nums:
    if num%2==0:

        evenNums.append(num)

print(f"Original list of numbers:\n{nums}")
print(f"Even numbers in the given list:\n{evenNums}")
