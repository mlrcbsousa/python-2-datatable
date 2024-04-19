
from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd


def plot_life_expectancy(df: pd.DataFrame, country: str):
    """Plot the life expectancy trends of a country."""

    try:
        # Data
        country_data = df[df['country'] == country]
        years = df.columns[1:]
        life_expectancy = country_data.iloc[0, 1:]

        # Plot
        plt.plot(years, life_expectancy)
        plt.xticks(['1800', '1840', '1880', '1920',
                    '1960', '2000', '2040', '2080'])
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title(f"{country} Life Expectancy Projections")
        plt.show()

    # occurs if terminate the script prematurely, by pressing Ctrl+C
    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(f"Error: {e}")


def main():
    '''Load the life expectancy data and plot for Belgium.'''

    df = load("life_expectancy_years.csv")

    try:
        assert df is not None

    except AssertionError:
        print("Failure to load data.")
        return

    plot_life_expectancy(df, 'Belgium')


if __name__ == "__main__":
    main()
