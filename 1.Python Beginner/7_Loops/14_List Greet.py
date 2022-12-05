'''Write a program to greet all the guests of the list into a party.
Those people whose names start with S will be moved to the VIP section.''' 

L1 = ["Sarveshwar", "Manika", "Champa", "Krishna", "Gopal", "Saksi", "Ganesh"]


for name in L1:

    print("Welcome to the party", name, "have a great time !!")

    if name.startswith("S"):
        print("Please come to the Vip section.")

    else:
        print("Please come into the main hall.")

