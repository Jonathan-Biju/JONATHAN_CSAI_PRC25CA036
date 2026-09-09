text=input("Enter the text:")

uniqueCh=set()

for ch in text:
    uniqueCh.add(ch)

print(f"The unique characters are:\n{uniqueCh}")