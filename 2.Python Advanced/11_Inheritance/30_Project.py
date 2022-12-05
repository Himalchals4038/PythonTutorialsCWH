'''
Write a program to allow a buyer to see the number of motorcycles available in current stock.
Each motorcycle costs 5 and thus display the buyer the amount according to number of units he wants to buy.
If the number of units requested by the buyer is more than the current stock, show error appropiately.
'''




class Motorcycle :

    try :
    
        def __init__ (self, stock, price) : 
            self.stock = stock
            self.price = price

        @property
        def startInterface(self) :

            while True :

                print ('''
                1 --> Display Available Stocks
                2 --> Place Order and Show Cost 
                3 --> Exit
                ''')

                choice = int(input("Enter your Choice: "))

                if choice == 1 :
                    print('The Number of Available Units are: ', self.stock)

                elif choice == 2 :
                    c = int(input("Enter number of units you want to buy: "))

                    if c <= self.stock :
                        print(f"The total cost is {c*self.price}")

                        d = str(input("Do you want to place your order ? (Yes/No): "))

                        if d == 'Yes' :
                            self.stock = self.stock - c
                            print("Your Order has been placed successfully !!")
                            print("Units Left: ", self.stock)

                        elif d == 'No' :
                            print("Ok thanks for using !!")
                            pass

                        else :
                            print("Wrong Choice, Please Try Again !!")

                    else :
                        print("Request amount exceeded stock amount. Please enter a lower value.")

                elif choice == 3 :
                    break   

                else :
                    print('Wrong Choice !!') 
    except :
        print ("Error in data recieved from Server !!")

z = Motorcycle(150, 14)
z.startInterface

            