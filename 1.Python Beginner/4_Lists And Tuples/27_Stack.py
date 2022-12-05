'''
Stack is a linear data structure.
It works on the principle of LIFO(Last-In First-Out) or FILO(First-In Last-Out).

Push -> Inserting an Element
Pop -> Deletion Of an Element (Last Element)
Peek -> Display the Last Element
Display -> Display List
'''

l1 = [20, 6, -9, 33, 42, 7]

while True :
    try :
        a = int(input(
        '''
        1 -> Push Elements
        2 -> Pop Elements
        3 -> Peek Elements 
        4 -> Display Stack
        5 -> Exit
        Enter your choice :
        '''
        ))
        if a == 1 :
            b = input("Enter value to be added: ")
            l1.append(b)
            print(l1)
        elif a == 2 :
            if len(l1) == 0:
                print("Empty Stack")
            else :
                b = l1.pop()
                print(b)
                print(l1)
        elif a == 3 :
            if len(l1) == 0 :
                print("Empty Stack")
            else :
                print(l1[-1])
        elif a == 4 :
            if len(l1) == 0 :
                print("Empty Stack")
            else :
                print(l1)
        elif a == 5 :
            break
        else :
            print("Wrong Input")
    except :
        print("Please enter an integer only !!")