for i in range (0,80):
    print(i)
    if i == 10:
        break
else:
    print("Done")

# If Done print is inside the else part then it will not be printed in result.
# This is because when the break sequence gets acivated Python aborts the process then and there.