num = int(input("Enter your desired number: "))
table = [num*i for i in range (1,21)]
print(table)

with open ('tables.txt', 'a') as f :
    f.write(f"The table of {num} is \n")
    f.write(str(table))
    f.write('\n')
