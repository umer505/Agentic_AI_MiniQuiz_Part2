movie_dictionary = {
    "the monster":{"showtime": 30, "price": 10.00},
    "the ghost":{"showtime": 20, "price": 12.00},
    "the witch":{"showtime": 10, "price": 15.00},
    "the vampire":{"showtime": 23, "price": 20.00},
    "the zombie":{"showtime": 23, "price": 18.00},
    "the werewolf":{"showtime": 23, "price": 22.00},
    "the mummy":{"showtime": 23, "price": 25.00},
    "twilight":{"showtime": 23, "price": 30.00},
    "the exorcist":{"showtime": 23, "price": 28.00},
    "the conjuring":{"showtime": 23, "price": 35.00},
    "final destination":{"showtime": 23, "price": 40.00},
    "the cabin in the woods":{"showtime": 23, "price": 45.00},
    "a quiet place":{"showtime": 23, "price": 50.00},
    "it":{"showtime": 23, "price": 55.00},
    "the wheel of time":{"showtime": 23, "price": 60.00},
    "game of thrones":{"showtime": 23, "price": 65.00},
    "the walking dead":{"showtime": 23, "price": 70.00},
    "stranger things":{"showtime": 23, "price": 75.00},
    "avengers endgame":{"showtime": 23, "price": 80.00},
    "spiderman no way home":{"showtime": 23, "price": 85.00},
    "batman the dark knight":{"showtime": 23, "price": 90.00},
    "attack on titan":{"showtime": 23, "price": 95.00},
    "death note":{"showtime": 23, "price": 100.00},

}

#Store booking in new dictionary
booking_dictionary = {
    "the monster": {"showtime": 0},
    "the ghost": {"showtime" : 0},
    "the witch": {"showtime" : 0},
    "the vampire": {"showtime" : 0},
    "the zombie": {"showtime" : 0},
    "the werewolf": {"showtime" : 0},
    "the mummy": {"showtime" : 0},
    "twilight": {"showtime" : 0},
    "the exorcist": {"showtime" : 0},
    "the conjuring": {"showtime" : 0},
    "final destination": {"showtime" : 0},
    "the cabin in the woods": {"showtime" : 0},
    "a quiet place": {"showtime" : 0},
    "it": {"showtime" : 0},
    "the wheel of time": {"showtime" : 0},
    "game of thrones": {"showtime" : 0},
    "the walking dead": {"showtime" : 0},
    "stranger things": {"showtime" : 0},
    "avengers endgame": {"showtime" : 0},
    "spiderman no way home": {"showtime" : 0},
    "batman the dark knight": {"showtime" : 0},
    "attack on titan": {"showtime" : 0},
    "death note": {"showtime" : 0}
}

def main():
    print("Welcome to the Movie Ticket Booking System!")

    while True:
        print("\nMenu:")
        print("1. View Available Movies")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Show Booking Summary")
        print("5. Exit")

        choice = input("\nPlease select an option (1-5): ")

        if choice == '1':
            print("\nAvailable Movies:")
            for movie in movie_dictionary:
                print(f"{movie.upper()}: Showtime - {movie_dictionary[movie]['showtime']} seats available, Price - ${movie_dictionary[movie]['price']:.2f}")

        elif choice == '2':
            print("\nBook tickets for available movies/seats")
            movie = input("Enter the movie name: ").lower()
            if movie in movie_dictionary:
                available = movie_dictionary[movie]["showtime"]
                price = movie_dictionary[movie]["price"]
                print(f"Available seats for {movie}: {available} seats, Price: ${price:.2f}")
                num_seats = input("Enter the number of seats to book: ")
                if num_seats.isdigit():
                    num_seats = int(num_seats)
                    if 0 < num_seats <= available:
                        movie_dictionary[movie]["showtime"] -= num_seats
                        booking_dictionary[movie]["showtime"] += num_seats
                        total_price = num_seats * price
                        print(f"Ticket(s) booked successfully for {movie}! Total price: ${total_price:.2f}")
                    else:
                        print("Not enough seats available or invalid seat count!")
                else:
                    print("Invalid number.")
            else:
                print("Movie not available.")

        elif choice == '3':
            print("\nCancel ticket for booked movies/seats")
            movie = input("Enter the movie name: ").lower()
            if movie in booking_dictionary:
                booked = booking_dictionary[movie]["showtime"]
                if booked == 0:
                    print("You have not booked any seats for this movie.")
                    continue
                print(f"You have booked {booked} seat(s) for {movie}.")
                num_seats = input("Enter the number of seats to cancel: ")
                if num_seats.isdigit():
                    num_seats = int(num_seats)
                    if 0 < num_seats <= booked:
                        booking_dictionary[movie]["showtime"] -= num_seats
                        movie_dictionary[movie]["showtime"] += num_seats
                        print(f"Cancelled {num_seats} seat(s) for {movie}.")
                    else:
                        print("You cannot cancel more seats than you have booked!")
                else:
                    print("Invalid number.")
            else:
                print("Movie not available.")

        elif choice == '4':
            print("\nBooking Summary:")
            any_booked = False
            for movie in booking_dictionary:
                booked = booking_dictionary[movie]["showtime"]
                if booked > 0:
                    price = movie_dictionary[movie]["price"]
                    print(f"{movie.upper()}: {booked} seat(s) booked, Price per seat: ${price:.2f}")
                    any_booked = True
            if not any_booked:
                print("No bookings yet.")

        elif choice == '5':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()