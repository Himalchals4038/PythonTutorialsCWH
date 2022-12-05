'''
Write a program to display the train name, booking types, train status, fare of a train registered under IRCTC.
Keep 10 seats booked for Old Age people which cannot be booked by normal people.
'''

class Train :
    company = "IRCTC"
    def __init__(self, name, booking_types, status, fare, seats) :
        self.name = name
        self.booking_types = booking_types
        self.status = status
        self.fare = fare
        self.seats = seats
        print("Request Generated")
    
    def getDetails(self) :
        print(f"The name of the train is {self.name}")
        print(f"The booking types of {self.name} are {self.booking_types} ")
        print(f"The status of {self.name} is {self.status}")
        print(f"The number of seats of {self.name} is {self.seats}")
        
    def fareInfo(self) :
        print(f"The fares of {self.name} are {self.fare}")    
    
    def bookTicket(self) :
        if (self.seats>10) :
            print(f"Your Ticket has been booked. Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else :
            print("Sorry this train is full. Please try in Tatkal")
    
    def cancelTicket(self) :
        print("Your train ticket has been sucessfully cancelled.")
        self.seats = self.seats + 1
        
Rajdhani = Train("Rajdhani Express: KOAA to NDL", "1st AC, 2nd AC, 3rd AC", "Available", "5600 for 1st AC, 4200 for 2nd AC, 2900 for 3rd AC", 12)
Rajdhani.getDetails()
Rajdhani.fareInfo()
Rajdhani.bookTicket()
Rajdhani.bookTicket()
Rajdhani.bookTicket()
Rajdhani.getDetails()
Rajdhani.cancelTicket()
Rajdhani.bookTicket()
Rajdhani.getDetails()