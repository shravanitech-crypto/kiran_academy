
from abc import ABC, abstractmethod


# Abstract Base Class
class Passenger(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


# Regular Passenger
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0.0

    def get_type(self):
        return "Regular"


# Student Passenger
class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10

    def get_type(self):
        return "Student"


# Flight Class
class Flight:
    def __init__(self, code, airline, source, destination,
                 available_seats, base_fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self._available_seats = available_seats
        self.base_fare = base_fare

    @property
    def available_seats(self):
        return self._available_seats

    def has_seats(self, tickets):
        return tickets <= self._available_seats

    def book_seats(self, tickets):
        if self.has_seats(tickets):
            self._available_seats -= tickets
            return True
        return False

    def display(self):
        print(
            f"{self.code:<10} {self.airline:<15} "
            f"{self.source:<12} {self.destination:<12} "
            f"{self.available_seats:<8} Rs.{self.base_fare}"
        )


# Booking Class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets,
                 subtotal, discount, total):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.total = total

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID:", self.booking_id)
        print("Flight Code:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to",
              self.flight.destination)
        print("Passenger Name:", self.passenger.name)
        print("Passenger Age:", self.passenger.age)
        print("Passenger Type:", self.passenger.get_type())
        print("Number of Tickets:", self.tickets)
        print(f"Base Fare per Ticket: Rs.{self.flight.base_fare:.2f}")
        print(f"Subtotal: Rs.{self.subtotal:.2f}")
        print(
            f"Discount ({self.passenger.get_discount() * 100:.0f}%): "
            f"Rs.{self.discount:.2f}"
        )
        print(f"Final Amount: Rs.{self.total:.2f}")
        print("=====================================")


# Main Application Class
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Kiran Air", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PN303", "Kiran Air", "Pune", "Hyderabad", 15, 3000)
        ]

        self.bookings = []
        self.next_booking_number = 1001

    # Display all available flights
    def display_flights(self):
        print("\n================ AVAILABLE FLIGHTS ================")
        print(
            f"{'Code':<10} {'Airline':<15} {'Source':<12} "
            f"{'Destination':<12} {'Seats':<8} Base Fare"
        )

        for flight in self.flights:
            flight.display()

        print("===================================================")

    # Find a flight using its code
    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    # Validate passenger and booking details
    def validate_booking(self, flight, name, age, tickets):
        if flight is None:
            return "Invalid flight code."

        if not name.strip():
            return "Passenger name cannot be blank."

        if age <= 0:
            return "Age must be greater than zero."

        if tickets <= 0:
            return "Number of tickets must be greater than zero."

        if not flight.has_seats(tickets):
            return "Not enough seats available."

        return None

    # Calculate ticket fare
    def calculate_fare(self, flight, passenger, tickets):
        subtotal = flight.base_fare * tickets
        discount = subtotal * passenger.get_discount()
        total = subtotal - discount

        return subtotal, discount, total

    # Book a flight
    def book_flight(self):
        self.display_flights()

        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Booking failed: Age and ticket count must be integers.")
            return

        passenger_type = input(
            "Passenger type (Regular/Student): "
        ).strip().lower()

        if passenger_type == "regular":
            passenger = RegularPassenger(name, age)
        elif passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            print("Booking failed: Invalid passenger type.")
            return

        # Validate everything before updating seat counts
        error = self.validate_booking(flight, name, age, tickets)

        if error:
            print("Booking failed:", error)
            print("No booking was created. Seat counts remain unchanged.")
            return

        # Calculate fare
        subtotal, discount, total = self.calculate_fare(
            flight, passenger, tickets
        )

        # Update seats only after validation succeeds
        if not flight.book_seats(tickets):
            print("Booking failed: Not enough seats available.")
            return

        # Save confirmed booking
        booking = Booking(
            f"BK{self.next_booking_number}",
            flight,
            passenger,
            tickets,
            subtotal,
            discount,
            total
        )

        self.bookings.append(booking)
        self.next_booking_number += 1

        print("\nBooking confirmed!")
        booking.display_summary()

    # Display the latest confirmed booking
    def view_booking(self):
        if not self.bookings:
            print("\nNo confirmed bookings found.")
            return

        self.bookings[-1].display_summary()

    # Main menu
    def run(self):
        print("\nWelcome to Kiran Air Booking!")

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Create an application object and start the program
if __name__ == "__main__":
    app = FlightBookingSystem()
    app.run()
