from load_csv import load

def main():
    """
    Main function to test the load function.
    """

    print("File:")
    print(load("life_expectancy.csv"))
    print()

    print("Type:")
    print(load(None))
    print(load(1))
    print()

    print("Valid:")
    print(load("life_expectancy_years.csv"))
    print()


if __name__ == "__main__":
    main()
