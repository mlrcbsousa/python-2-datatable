
from matplotlib import pyplot as plt
from load_csv import load


def main():
    '''Load the life expectancy data and plot for Belgium.'''

    df = load("life_expectancy_years.csv")

    try:
        assert df is not None, "Failure to load data."
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    try:
        # Get the data for Belgium
        country_data = df[df['country'] == 'Belgium']
        years = df.columns[1:]
        life_expectancy = country_data.iloc[0, 1:]

        # Plot the data
        plt.plot(years, life_expectancy)
        plt.xticks(['1800', '1840', '1880', '1920',
                    '1960', '2000', '2040', '2080'])
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title('Belgium Life Expectancy Projections')
        plt.show()

    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
