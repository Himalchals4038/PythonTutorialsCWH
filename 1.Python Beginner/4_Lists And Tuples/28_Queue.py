'''
Queue is a linear data struture.
It wotks on FIFO (First-In First-Out) policy.
Enqueue -> Adds an item to the queue.
Dequeue -> Removes an item from the queue.
Front -> Get the front item from queue.
Rear -> Get the last item from queue.
'''

l1 = [20, 6, -9, 33, 42, 7]

while True :
    try :
        a = int(input(
        '''
        1 -> Push Elements
        2 -> Pop First Element
        3 -> First Element 
        4 -> Last Element 
        5 -> Display Stack
        6 -> Exit
        Enter your choice :
        '''
        ))
        if a == 1 :
            b = input("Enter value to be added: ")
            l1.append(b)
            print(l1)
        elif a == 2 :
            if len(l1) == 0:
                print("Empty Queue")
            else :
                del l1[0]
                print(l1)
        elif a == 3 :
            if len(l1) == 0 :
                print("Empty Queue")
            else :
                print(l1[0])
        elif a == 4 :
            if len(l1) == 0 :
                print("Empty Queue")
            else :
                print(l1[-1])
        elif a == 5 :
            if len(l1) == 0 :
                print("Empty Queue")
            else :
                print(l1)
        elif a == 6 :
            break
        else :
            print("Wrong Input")
    except :
        print("Please enter an integer only !!")