'''Write a program to convert celsius into farenheit and vice versa.'''

def farh(cel):
    p = (cel * (9/5)) + 32
    return p

def cel(farh):
    q = (5/9)*(farh-32)
    return q

z = int(input("Enter 1 if you want to convert celsius into farenheit and 2 for vice-versa: "))

if z == 1 : 
    t = int(input("Enter the temperature in degree celsius: "))
    k = farh(t)
    print("The temperature in farenheit is: ", k)

elif z == 2 :
    t = int(input("Enter the temperature in farenheit: "))
    k = cel(t)
    print("The temperature in degree celsius is: ", k)

else:
    print("Wrong Input !!")