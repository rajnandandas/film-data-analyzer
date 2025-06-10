import pandas as pd
from colorama import Fore, Style

def load_data():
    return pd.read_csv("movies.csv")

def top_movies_by_year(data, year):
    filtered = data[data["Year"] == year]
    sorted_data = filtered.sort_values(by="Rating", ascending=False)
    print(Fore.CYAN + f"\nTop movies from {year}:\n" + Style.RESET_ALL)
    print(sorted_data[["Title", "Genre", "Rating"]])

def top_movies_by_genre(data, genre):
    filtered = data[data["Genre"].str.lower() == genre.lower()]
    sorted_data = filtered.sort_values(by="Rating", ascending=False)
    print(Fore.GREEN + f"\nTop {genre} movies:\n" + Style.RESET_ALL)
    print(sorted_data[["Title", "Year", "Rating"]])

def main():
    data = load_data()
    while True:
        print("\n" + "-"*40)
        print("Film Data Analyzer - Menu")
        print("1. Top Movies by Year")
        print("2. Top Movies by Genre")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            year = int(input("Enter year: "))
            top_movies_by_year(data, year)
        elif choice == "2":
            genre = input("Enter genre: ")
            top_movies_by_genre(data, genre)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
