file1 = str(input("Enter name of first file with extension: "))
file2 = str(input("Enter name of second file with extension: "))

with open(file1) as f :
    f1 = f.read()

with open(file2) as f :
    f2 = f.read()

if f1 == f2 :
    print("Both the files are identical.")

else :
    print("Both files are not identical.")