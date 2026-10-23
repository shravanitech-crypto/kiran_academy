import random

cab_rates = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

routes = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Swargate", "Kothrud", 8),
    3: ("Hinjawadi", "Wakad", 10)
}

while True:
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("\n---------- SELECT CAB TYPE ----------")
        print("1. Auto - Rs. 12/km")
        print("2. Sedan - Rs. 18/km")
        print("3. SUV - Rs. 25/km")

        cab_choice = input("Choose your cab (1-3): ").strip()

        if cab_choice not in ("1", "2", "3"):
            print("Invalid cab choice. Returning to main menu.")
            continue

        cab_name, rate = cab_rates[int(cab_choice)]

        print("\n---------- SELECT ROUTE ----------")
        print("1. Pune Station -> Shivajinagar (5 km)")
        print("2. Swargate -> Kothrud (8 km)")
        print("3. Hinjawadi -> Wakad (10 km)")

        route_choice = input("Choose your route (1-3): ").strip()

        if route_choice not in ("1", "2", "3"):
            print("Invalid route choice. Returning to main menu.")
            continue

        source, destination, distance = routes[int(route_choice)]
        fare = rate * distance

        print("\n========== RIDE DETAILS ==========")
        print("Cab Type:", cab_name)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "per km")
        print("Total Fare: Rs.", fare)

        while True:
            print("\n1. Confirm & Share OTP")
            print("2. Cancel Ride")

            confirm_choice = input("Enter your choice: ").strip()

            if confirm_choice == "1":
                otp = random.randint(1000, 9999)
                print("\nYour ride OTP is:", otp)
                print("Once the OTP is shared, the ride cannot be cancelled.")
                print("Booking confirmed successfully!")
                print("Have a safe journey!")
                break

            elif confirm_choice == "2":
                print("Ride cancelled successfully. No OTP was shared.")
                break

            else:
                print("Invalid choice. Please enter 1 or 2.")

    elif choice == "2":
        print("Thank you for using Cab Booking Chatbot. Goodbye!")
        break

    else:
        print("Invalid menu choice. Please enter 1 or 2.")