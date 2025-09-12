class Movie:
    def __init__(self, title, genre, showtime, seats):
        self.title = title
        self.genre = genre
        self.showtime = showtime
        self.seats = seats

class Booking:
    def __init__(self, movie, user_name, seats_booked):
        self.movie = movie
        self.user_name = user_name
        self.seats_booked = seats_booked

def display_movies(movies):
    print("Available Movies:")
    for i, movie in enumerate(movies):
        print(f"{i + 1}. {movie.title} - {movie.genre} - {movie.showtime} - Seats Available: {movie.seats}")

def book_movie(movies):
    display_movies(movies)
    choice = int(input("Enter the number of the movie you want to book: ")) - 1
    if choice < 0 or choice >= len(movies):
        print("Invalid choice. Please try again.")
        return

    movie = movies[choice]
    user_name = input("Enter your name: ")
    seats_booked = int(input("Enter the number of seats you want to book: "))

    if seats_booked > movie.seats:
        print("Not enough seats available. Please try again.")
        return

    movie.seats -= seats_booked
    booking = Booking(movie, user_name, seats_booked)
    print(f"Booking successful! {seats_booked} seats booked for {movie.title} by {user_name}.")

def main():
    movies = [
        Movie("Inception", "Sci-Fi", "7:00 PM", 50),
        Movie("The Dark Knight", "Action", "9:00 PM", 30),
        Movie("Interstellar", "Sci-Fi", "6:00 PM", 40)
    ]

    while True:
        print("\nMovie Booking System")
        print("1. Display Movies")
        print("2. Book Movie")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_movies(movies)
        elif choice == 2:
            book_movie(movies)
        elif choice == 3:
            print("Thank you for using the Movie Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
