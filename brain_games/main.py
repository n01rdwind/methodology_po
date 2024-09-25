from engine import run_game
import games.gcd_game as gcd_game
import games.progression_game as progression_game


def main():
    print("Choose a game:")
    print("1. Least Common Multiple (LCM)")
    print("2. Geometric Progression")
    choice = input("Enter the number of the game: ")
    if choice == '1':
        run_game(gcd_game)
    elif choice == '2':
        run_game(progression_game)
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
