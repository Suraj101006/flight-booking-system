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
        if a == flight['From'].lower():
            if b == flight['To'].lower():
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
    with open("book (1).csv", "r") as file:
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
        return False, None , None

    print("\nFlight status:")
    for seat in seats:
        if seat['FlightNo'] == d:
            print(seat['FlightNo'] + " | " + seat['SeatNo'] + " | " + seat['Status'] + " | " + seat['type'])

    e = input("Enter a seat no to book: ")
    booked = False
    for seat in seats:
        if seat['FlightNo'] == d:
            if seat['SeatNo'] == e:
                if seat['Status'] == 'Available':
                    seat['Status'] = 'Booked'
                    booked = True
                    print("Seat booked successfully")
                    with open("book (1).csv", "w", newline="") as file:
                        fieldnames = ['FlightNo', 'SeatNo', 'Status', 'type']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(seats)
                    return True, d,e
                else:
                    print("Seat is already booked.")
                break
    if not booked:
        print("Invalid seat number or not available.")
    return False, None ,None

class Info:
    def __init__(self, FlightNo,SeatNo):
        self.FlightNo = FlightNo
        self.SeatNo = SeatNo
        self.name = input("Enter Your Full Name: ")
        while True:
            self.age = input("Enter your age: ")
            if self.age.isdigit():
                self.age = int(self.age)
                if 18 <= self.age <= 120:
                    break
            print("Invalid age. Please enter a number between 18 and 120.")
        while True:
            self.mobile = input("Enter your mobile no: ")
            if self.mobile.isdigit():
                if len(self.mobile) == 10:
                   break
            else:
                   print("Invalid mobile number. Please enter a 10-digit number.")
        while True:           
         self.dob = input("Enter the date of birth (dd/mm/yyyy): ")
         if self.dob.isdigit():
             break
         else:
             print("Invalid Input")
        self.gender = input("Enter your gender: ")

    def show(self):
        print("\nPassenger Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)
        print("DOB:", self.dob)
        print("Gender:", self.gender)
        print("Flight No:", self.FlightNo)
        print("Seat No:", self.SeatNo)

    def save(self):    
        with open("book.csv", "a", newline="") as file:
            fieldnames = ['Name', 'Age', 'Mobile', 'DOB', 'Gender', 'FlightNo', 'SeatNo' ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({
                'Name': self.name,
                'Age': self.age,
                'Mobile': self.mobile,
                'DOB': self.dob,
                'Gender': self.gender,
                'FlightNo': self.FlightNo,
                'SeatNo': self.SeatNo,
            })
def cancel():
    seats = book()
    flight_no = input("Enter your Flight Number to cancel booking: ")
    seat_no = input("Enter your Seat Number to cancel: ")
    found = False

    for seat in seats:
        if seat['FlightNo'] == flight_no and seat['SeatNo'] == seat_no:
            found = True
            if seat['Status'] == 'Booked':
                print("Booking found.")
                confirm = input("Do you want to cancel your booking? (yes/no): ").lower()
                if confirm == 'yes':
                    seat['Status'] = 'Available'
                    with open("book (1).csv", "w", newline="") as file:
                        fieldnames = ['FlightNo', 'SeatNo', 'Status', 'type']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(seats)
                    print("Booking cancelled successfully.")
                else:
                    print("Cancellation aborted.")
            else:
                print("This seat is already available. Nothing to cancel.")
            break

    if not found:
        print("No such booking found")
flights = flightsdata()
details = None

while True:
    print("\n========= Flight Booking System Menu =========")
    print("1. Show All Flights")
    print("2. Search Flights")
    print("3. Sort Flights by Price ")
    print("4. Book Ticket")
    print("5. Show details of booking")
    print("6. Cancel booking")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        show()
    elif choice == '2':
        search()
    elif choice == '3':
        sort()
    elif choice == '4':
        success, flight_no, Seat_no = bookticket()
        if success:
            passenger = Info(flight_no, Seat_no)
            passenger.save()
            details= passenger  
        print("\nTicket booked successfully!")
    elif choice == '5':
        if details:
            details.show()
        else:
            print("No booking found.  book a ticket first.")   
    elif choice == '6':
        cancel()
    elif choice == '7':
        print("Thank you for using the Flight Booking System!")
        break
    else:
        print("Invalid choice. Please enter 1-7.")