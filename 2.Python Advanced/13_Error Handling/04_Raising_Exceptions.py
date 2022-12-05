# Raise function runs the code inside it if python fails to run the previous program. 
# It doesn't allow python to show error code.

def increment(num) :
    try :
        return int(num) + 1
    except :
        raise ValueError("Please enter a correct integer.")

a = increment(16)
print(a)