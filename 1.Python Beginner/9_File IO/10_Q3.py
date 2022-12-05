'''Write program to make a separate folder which contains the mutiplication tables from 1 to 21 upto 20, all as separate files.'''

for i in range (1, 22) :
    with open(f"tables/Multiplication Table of {i}", 'w') as f :
        for j in range (1, 21) :
            k = i * j
            f.write(f"{i}X{j}={k}\n")
            j = j + 1
i = i + 1