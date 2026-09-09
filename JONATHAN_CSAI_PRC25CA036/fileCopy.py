with open("source.txt","w") as f:
    f.write("sample")
with open("source.txt","r") as src, open("destination.txt","w") as dest:
    dest.write(src.read())
print("File copied successfully.")