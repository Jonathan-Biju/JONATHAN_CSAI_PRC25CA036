n=int(input("Enter the number of elements in the list:"))

my_list=[]

for i in range(n):

    element=input(f"Enter element{i+1}:")
    my_list.append(element)

unique_elements=[]

for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)

print("Original List:",my_list)
print("Unique Elements:",unique_elements)