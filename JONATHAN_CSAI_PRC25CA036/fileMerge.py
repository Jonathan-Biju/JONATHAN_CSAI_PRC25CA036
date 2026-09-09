with open("file1.txt","w") as f1:
    f1.write("Content of File1\n")
with open("file2.txt","w") as f2:
    f2.write("Content of File2\n")
with open("file1.txt","r") as f1, open("file2.txt","r") as f2:
    Data1=f1.read()
    Data2=f2.read()
with open("merged.txt","w") as m:
    m.write(Data1+Data2)

print("File merged successfully\n")
