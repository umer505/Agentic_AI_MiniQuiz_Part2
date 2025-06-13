cars_data ={
    "toyota camry": {"available": True, "renter": None},
    "honda accord": {"available": True, "renter": None},
    "honda civic": {"available": True, "renter": "umer"},
    "toyota corolla": {"available": True, "renter": None},
    "ford focus": {"available": True, "renter": "ali"},
    "nissan altima": {"available": True, "renter": None},
    "mercedes benz": {"available": True, "renter": "umer"},
    "bmw 3": {"available": True, "renter": None},
    "audi a4": {"available": True, "renter": "ali"},
    "honda city": {"available": True, "renter": None},
    "toyota yaris": {"available": True, "renter": None},
}

def display_available_cars():
    print("Available Cars:")
    for car, details in cars_data.items():
        if details["available"]:
            print(f"- {car}")

def rent_car(car_name, renter_name):
    if car_name in cars_data:
        if cars_data[car_name]["available"]:
            cars_data[car_name]["available"] = False
            cars_data[car_name]["renter"] = renter_name
            print(f"{car_name} has been rented to {renter_name}.")
        else:
            print(f"Sorry, {car_name} is already rented by {cars_data[car_name]['renter']}.")
    else:
        print(f"Car {car_name} does not exist in the system.")


def return_car(car_name, renter_name):
    if car_name in cars_data:
        if not cars_data[car_name]["available"] and cars_data[car_name]["renter"] == renter_name:
            cars_data[car_name]["available"] = True
            cars_data[car_name]["renter"] = None
            print(f"{car_name} has been returned by {renter_name}.")
        else:
            print(f"Error: {car_name} is not rented by {renter_name}.")
    else:
        print(f"Car {car_name} does not exist in the system.")

def display_rented_cars():
    print("Rented Cars:")
    for car, details in cars_data.items():
        if not details["available"]:
            print(f"- {car} (Rented by: {details['renter']})")

def main():
    while True:
        print("\nCar Rental System")
        print("1. Display Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. View all rentals")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_available_cars()
        elif choice == "2":
            car_name = input("Enter the car name to rent: ").strip().lower()
            renter_name = input("Enter your name: ").strip()
            rent_car(car_name, renter_name)
        elif choice == "3":
            car_name = input("Enter the car name to return: ").strip().lower()
            renter_name = input("Enter your name: ").strip()
            return_car(car_name, renter_name)
        elif choice == "4":
            display_rented_cars()
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()