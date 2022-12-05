import math
import random

'''
The project here is to make a ledger of the port trading. 
Here different suppliers and consumers come together and trade different items and stocks.
Each type of product has different taxes and service charges applied by 
Government and Supplier which have to be bore by the buyer. 
Make a fully-fledged online program which can be used by 
suppliers, contractors, buyers and transporters together.
'''

port_fee_supplier = 0.9
port_fee_contractor = 0.5
port_fee_buyer = 1.1
port_fee_transporter = 500


gov_tax_list_supplier = {
    'a' : 3.6, 'b' : 4.2, 'c' : 2.1, 'd' : 6.9, 
    'e' : 7.8, 'f' : 4.9, 'g' : 1.6, 'h' : 0.9 
}

gov_tax_list_contractor = {
    'a' : 0.6, 'b' : 0.7, 'c' : 0.1, 'd' : 1.1, 
    'e' : 1.8, 'f' : 0.5, 'g' : 0.3, 'h' : 0.1 
}

gov_tax_list_buyer = {
    'a' : 4.2, 'b' : 4.8, 'c' : 2.7, 'd' : 7.5, 
    'e' : 8.4, 'f' : 5.5, 'g' : 2.2, 'h' : 1.5 
}

stored_goods_supplied = {
    "default" : "null"
}
stored_goods_traded = {
    "default" : "null"
}
stored_goods_sold = {
    "default" : "null"
}

def total_price_func (a, b) :
    
    return a * b

def pay(a, b) :
    
    return a + b

port_tax_dict = {
    1 : "supplier",
    2 : "contractor",
    3 : "buyer",
    4 : "transporter"
}

sold_goods_location = {
    "default" : "null"
}

while True :
    print('''
          Welcome to Online Port Management Portal !!
          All monetary-related transactions and supply requests are processed here.
          Please select one out of the below options to proceed :-
          
          1 -> Supplier Login
          2 -> Contractor Login
          3 -> Buyer Login
          4 -> Transporter Login
          5 -> Exit
          ''')
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1 :
        
        name = str(input("Please enter your name : "))
        
        id = int(input("Please enter your Port ID : "))
        
        print(f"\nWelcome To Haldia Port {name}")
        
        print(f"\nYour Port ID is {id}")
        
        print('''
              Type a : Food Items Degradable
              Type b : Food Items Non-Degradable
              Type c : Timber
              Type d : Medicines
              Type e : Arms and Ammunition
              Type f : Vehicles
              Type g : Electronics
              Type h : Stationery
              ''')
        
        item_type = str(input("Enter the type of product being supplied : "))
        
        item_quantity  = int(input("Enter the quantity of product being supplied : "))
        
        item_price = int(input("Enter your-end price of product : "))
        
        total_price = total_price_func(item_quantity, item_price)
        
        port_tax = total_price * (port_fee_supplier/100)
        
        gov_tax = total_price * (gov_tax_list_supplier.get(f'{item_type}')/100)
        
        total_tax = port_tax + gov_tax
        
        total_tax = math.floor(total_tax)
        
        payment = pay(total_price, total_tax)
        
        print("The total price of supplied items = Rs. " + f'{total_price}')
        
        print("The total tax to be paid is : " + f'{total_tax}')
        
        final_choice = int(input("Enter 1 to confirm the supply order and 2 to reject it."))
        
        if final_choice == 1 :
        
            print(f"Please pay Rs. {payment} at the front desk.")
            
            print("Thanks for using the Online Portal !!")

            update_stored_goods_supplied = {
                f"{item_type}" : { f"{id}" : {'item_quantity' : f"{item_quantity}", 'item_price' :  f"{item_price}"}}
            }

            stored_goods_supplied.update(update_stored_goods_supplied)
            continue
            
            # print(stored_goods_supplied)
            
        elif final_choice == 2 : 
            
            continue
        
        else :
            
            print("Wrong Choice, Supply Order Not Placed !")
            continue
        
        # choice_continue = int(input("Press 1 if you want to continue and 2 if you want to exit : "))
        
        # if choice_continue == 1 :
             
        #     continue
        
        # elif choice_continue == 2 : 
            
        #     break
        
        # else :
            
        #     print("Wrong Choice")
        #     continue
     
     # Enter a price regulation check on contractors so that they can't charge more than 
     # 5% extra on the price of the product of the item being sold by the supplier.
        
    if choice == 2 :
        
        name = str(input("Please enter your name : "))
        
        id = int(input("Please enter your Port ID : "))
        
        print(f"\nWelcome To Haldia Port {name}")
        
        print(f"\nYour Port ID is {id}")
        
        print('''
              Type a : Food Items Degradable
              Type b : Food Items Non-Degradable
              Type c : Timber
              Type d : Medicines
              Type e : Arms and Ammunition
              Type f : Vehicles
              Type g : Electronics
              Type h : Stationery
              ''')
        
        item_type = str(input("Enter the type of product being traded : "))
        
        supplier_id = str(input("Enter the port ID of supplier : "))
        
        try :
            
            max_item_quantity = stored_goods_supplied[item_type][supplier_id]['item_quantity']
            
            max_item_quantity = int(max_item_quantity)

            print(f"Total quantity of goods available : {max_item_quantity}")

            item_quantity  = int(input("Enter the quantity of product being traded : "))

            if item_quantity > max_item_quantity :  

                print("There is a shortage in stocks. Please enter a lesser quantity request.")

            elif item_quantity < max_item_quantity :     

                print("Please enter a higher number as whole stock is to be bought at once.")

            else:    

                print("Product quantity request accepted !!")

            item_price = stored_goods_supplied[item_type][supplier_id]['item_price']
            
            item_price = float(item_price)

            item_price_tr_max = item_price * 1.05

            print(f"The supplier-end price of the product is : {item_price}")

            item_price_tr = float(input("Enter your-end price of product : "))   
            
            if item_price_tr > item_price_tr_max :

                print(f"The max price permissible on this product is {item_price_tr_max}. Please enter a lower value.")

            else :

                print("Price accepted.")   

                total_price = total_price_func(item_quantity, item_price_tr)  
    
                port_tax = total_price * (port_fee_contractor/100)
                
                gov_tax = total_price * (gov_tax_list_contractor.get(f'{item_type}')/100)  
                
                total_tax = port_tax + gov_tax
                
                total_tax = math.floor(total_tax)  
                
                payment = pay(total_price, total_tax)  
    
                print("The total price of tradeable items = Rs. " + f'{total_price}')
    
                print("The total tax to be paid is : " + f'{total_tax}')
    
                final_choice = int(input("Do you want to place trade request ? Press 1 if Yes and 2 if No : "))
    
                if final_choice == 1 :
                
                    print(f"Please pay Rs. {payment} at the front desk.")
    
                    print("Thank You For Using The Online Portal !!")
    
                    del stored_goods_supplied[f"{item_type}"][f"{supplier_id}"]
    
                    update_stored_goods_traded = {
                    f"{item_type}" : { f"{id}" : {'item_quantity' : f"{item_quantity}", 'item_price' :  f"{item_price_tr}"}}
                    }
    
                    stored_goods_traded.update(update_stored_goods_traded)
                    
                    # print(stored_goods_traded)
    
                elif final_choice == 2 : 
                
                    continue
            
                else :

                    print("Wrong Choice, Trade Order Not Placed !")

                    continue
        
        except :
            
            print("The item type is currently out of stock.")
            continue
        
        # choice_continue = int(input("Press 1 if you want to continue and 2 if you want to exit : "))
        
        # if choice_continue == 1 :
            
        #     continue
        
        # elif choice_continue == 2 : 
            
        #     break
        
        # else :  
            
        #     print("Wrong Choice")   
        #     continue
    
    if choice == 3 :
        
        name = str(input("Please enter your name : "))
        
        id = int(input("Please enter your Port ID : "))
        
        print(f"\nWelcome To Haldia Port {name}")
        
        print(f"\nYour Port ID is {id}")
        
        print('''
              Type a : Food Items Degradable
              Type b : Food Items Non-Degradable
              Type c : Timber
              Type d : Medicines
              Type e : Arms and Ammunition
              Type f : Vehicles
              Type g : Electronics
              Type h : Stationery
              ''')
        
        item_type = str(input("Enter the type of product being bought : "))
        trader_id = str(input("Enter the port ID of trader : "))
        
        try :
            
            max_item_quantity = stored_goods_traded[item_type][trader_id]['item_quantity']
            
            max_item_quantity = int(max_item_quantity)

            print(f"Total quantity of goods available : {max_item_quantity}")

            item_quantity  = int(input("Enter the quantity of product being bought : "))

            if item_quantity > max_item_quantity :  

                print("Trader has lesser stocks than requested. Please enter a lower request value.")

            elif item_quantity < max_item_quantity :     

                print("Please enter a higher number as whole stock is to be bought at once.")

            else:    

                print("Product quantity request accepted !!")

            item_price = stored_goods_traded[item_type][trader_id]['item_price']

            item_price = float(item_price)

            print(f"The trader-end price of the product is : {item_price}") 

            total_price = total_price_func(item_quantity, item_price_tr)  

            port_tax = total_price * (port_fee_contractor/100)
            
            gov_tax = total_price * (gov_tax_list_contractor.get(f'{item_type}')/100)  

            total_tax = port_tax + gov_tax
            
            total_tax = math.floor(total_tax)  

            payment = pay(total_price, total_tax)  

            print("The total price of tradeable items = Rs. " + f'{total_price}')

            print("The total tax to be paid is : " + f'{total_tax}')

            final_choice = int(input("Do you want to place buy request ? Press 1 if Yes and 2 if No : "))

            if final_choice == 1 :

                storage_warehouse = random.randint(1, 15)
                warehouse_section = random.randint(1, 50)

                sold_goods_location_update = {
                    f'{id}' : {'storage_warehouse' : f'{storage_warehouse}', 'warehouse_section' : f'{warehouse_section}'}
                }

                sold_goods_location.update(sold_goods_location_update)

                # print(sold_goods_location)

                print(f"Please pay Rs. {payment} at the front desk.")
                
                print(f"Your goods will be stored at Warehouse No. {storage_warehouse} in Section No. {warehouse_section}.")
                
                print("Thank You For Using The Online Portal !!")

                del stored_goods_traded[f"{item_type}"][f"{trader_id}"]

                update_stored_goods_sold = {
                f"{item_type}" : { f"{id}" : {'item_quantity' : f"{item_quantity}", 'item_price' :  f"{item_price}"}}
                }

                stored_goods_sold.update(update_stored_goods_sold)

                # print(stored_goods_sold)

            elif final_choice == 2 : 
                
                continue
            
            else :
                
                print("Wrong Choice, Buy Order Not Placed !")
                continue
        
        except :
            
            print("The item type is currently out of stock.")
            continue
        
        # choice_continue = int(input("Press 1 if you want to continue and 2 if you want to exit : "))
        
        # if choice_continue == 1 :
            
        #     continue
        
        # elif choice_continue == 2 : 
            
        #     break
        
        # else :  
            
        #     print("Wrong Choice")
        #     continue
            
    if choice == 4 :
        
        name = str(input("Please enter your name : "))
        
        id = int(input("Please enter your Port ID : "))
        
        consumer_id = str(input("Enter the port ID of consumer : "))
        
        storage_warehouse_no = sold_goods_location[consumer_id]['storage_warehouse']
        
        warehouse_section_no = sold_goods_location[consumer_id]['warehouse_section']
        
        print(f"Please pay Rs. {port_fee_transporter} at the front desk.")
        
        print(f"Please pick up the goods from Warehouse {storage_warehouse_no}, storage rack {warehouse_section_no}.")
        
        print("Thanks for using the Online Portal !!")
        
        del sold_goods_location[consumer_id]
        continue

        # choice_continue = int(input("Press 1 if you want to continue and 2 if you want to exit : "))
        
        # if choice_continue == 1 :
            
        #     continue
        
        # elif choice_continue == 2 :
            
        #     break
        
        # else :
            
        #     print("Wrong Choice")
        #     break
    
    # if choice == 5 :
        
    #     break
    
    if choice == 59 :
        
        def admin_pass(g) :
            
            if g == 5548 :
                
                print("Welcome to THE ADMIN AREA !!")
                
                print('''
                    1 -> Current Supplied Products in Store
                    2 -> Current Traded Products in Store
                    3 -> All The Products that were sold from this Port
                    4 -> Location Of Currently Present Sold Products
                    5 -> Stop The Online Portal System
                      ''')
                
                k = int(input("Enter your choice : "))
                
                if k == 1 :
                    
                    print(stored_goods_supplied)
                    
                elif k == 2 :
                    
                    print(stored_goods_traded)
                    
                elif k == 3 :
                    
                    print(stored_goods_sold)
                    
                elif k == 4 :
                    
                    print(sold_goods_location)
                    
                else :
                    
                    break
                
            else :
                
                print("Wrong Password !!")



