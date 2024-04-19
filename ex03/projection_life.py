
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def plot_gdp_life_expectancy(
        gdp: pd.DataFrame,
        life_expectancy: pd.DataFrame,
        year: str
        ):
    """Plot the GDP and life expectancy trends of all countries."""

    try:
        # Data
        series_gdp = gdp[year]
        series_life_expectancy = life_expectancy[year]

        # Plot
        plt.scatter(series_gdp, series_life_expectancy)
        plt.xlabel('Gross Domestic Product')
        plt.ylabel('Life Expectancy')
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.title(year)
        plt.show()

    # occurs if terminate the script prematurely, by pressing Ctrl+C
    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(f"Error processing data: {e}")


def main():
    """Load GDP and life expectancy data and display for year 1900."""

    df_life_expectancy = load("life_expectancy_years.csv")
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    try:
        assert df_life_expectancy is not None and df_gdp is not None

    except AssertionError:
        print("Failure to load data.")
        return

    plot_gdp_life_expectancy(df_gdp, df_life_expectancy, '1900')


if __name__ == "__main__":
    main()
