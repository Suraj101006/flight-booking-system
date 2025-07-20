import csv

def flightsdata():
    flights = []
    
    with open("newfile.csv", "r") as file:
        read = csv.DictReader(file)
        for row in read:
            flights.append(row)
    
    return flights

def show():
    print("\nAvailable flights")
    print("FlightNo | From     | To       | Date      |   Time  | Price") 
    for flight in flights:
        print(flight['FlightNo'] + " | " + flight['From'] + " | " + flight['To'] + " | " + flight['Date'] + " | " + flight['Time'] + " | ₹" + flight['Price'])

def search():
    a = input("Enter the city you want to depart from: ")
    b = input("Enter the destination city : ")
    found = False
    for flight in flights:
        if a == flight['From']:
            if b == flight['To']:
                print(flight['FlightNo'] + " | " + flight['From'] + " | " + flight['To'] + " | " + flight['Date'] + " | " + flight['Time'] + " | ₹" + flight['Price'])
                found = True
                break
    if not found:
        print("Flight not found")

def sort():
    i = 0
    while i < len(flights):
        j = i + 1
        while j < len(flights):
            if int(flights[j]['Price']) > int(flights[i]['Price']):
                flights[i], flights[j] = flights[j], flights[i]
            j += 1
        i += 1

    print("\nFlights Sorted by Price:")
    print("FlightNo | From     | To       | Date       | Time  | Price")
    i = 0
    while i < len(flights):
        flight = flights[i]
        print(flight['FlightNo'] + " | " + flight['From'] + " | " + flight['To'] + " | " + flight['Date'] + " | " + flight['Time'] + " | ₹" + flight['Price'])
        i += 1
       
def book():
    book = []
    with open ("book (1).csv" , "r")as file:
        read = csv.DictReader(file)
        for row in read:
            book.append(row)
    return book
    
def bookticket():
    seats = book()
    d = input("Enter a flight no: ")
    found = False
    for seat in seats:
        if d == seat['FlightNo']:
            print("Flight is available")
            found = True
            break
    if not found:
        print("Flight not found in seat database")
        return

    print("\nFlight status:")
    for seat in seats:
        if seat['FlightNo'] == d:
            print(seat['FlightNo'] + " | " + seat['SeatNo'] + " | " + seat['Status'] + " | " + seat['type'])

    e = input("Enter a seat no to book: ")
    booked = False
    for seat in seats:
        if seat['FlightNo'] == d :
            if seat['SeatNo'] == e:
                if seat['Status'] == 'Available':
                    seat['Status'] = 'Booked'
                    booked = True
                    print("Seat booked successfully ")
                    return True
                else:
                    print(" Seat is already booked.")
                break

    if not booked:
        print(" Invalid seat number or not available.")
    return False
    
   
    with open("book (1).csv", "w", newline="") as file:
        fieldnames = ['FlightNo', 'SeatNo', 'Status', 'type']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(seats)
        
class Info:
    def __init__(self):
        self.name = input("Enter Your Full Name: ")
        while True:
            self.age = (input("Enter your age: "))
            if self.age.isdigit():
                self.age = int(self.age)
                if 18 <= self.age <= 120:
                     break
            else:
                  print("Invalid age. Please enter age between 18 to 120.")
        while True:
            self.mobile = input("Enter your mobile no: ")
            if self.mobile.isdigit():
                if len(self.mobile)  == 10:
                    break
            else:
                  print(" Invalid mobile number. Please enter a 10-digit number.")
        self.dob = input("Enter the date of birth (dd/mm/yyyy): ")
        self.gender = input("Enter your gender: ")

    def show(self):
        print("\nPassenger Information:")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Mobile : {self.mobile}")
        print(f"DOB    : {self.dob}")
        print(f"Gender : {self.gender}")
    def save(self):    
        with open("book.csv", "w", newline="") as file:
            fieldnames = ['Name', 'Age', 'Mobile', 'DOB', 'Gender']
            writer = csv.DictWriter(file,                                     fieldnames=fieldnames)

            writer.writerow({
            'Name': self.name,
             'Age': self.age,
             'Mobile': self.mobile,
             'DOB': self.dob,
             'Gender': self.gender
    }) 
        

flights = flightsdata()
        
while True:
    print("\n========= Flight Booking System Menu =========")
    print("1. Show All Flights")
    print("2. Search Flights")
    print("3. Sort Flights by Price (High to Low)")
    print("4. Book Ticket")
    print("5. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        show()
    elif choice == '2':
        search()
    elif choice == '3':
        sort()
    elif choice == '4':
          success = bookticket()
          if success:
            passenger = Info()
            passenger.show()
            passenger.save()
        
    elif choice == '5':
        print("Thank you ")
        break
    else:
        print(" Invalid choice. ")
        

    