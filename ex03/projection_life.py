
import matplotlib.pyplot as plt
from load_csv import load


def main():
    '''displays a scatter plot of with GDP on the x-axis and life expectancy
    on the y-axis
    '''

    try:
        # Data
        df_life_expectancy = load("life_expectancy_years.csv")
        df_gdp = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )

        series_life_expectancy_1900 = df_life_expectancy['1900']
        series_gdp_1900 = df_gdp['1900']

        # Plot
        plt.scatter(series_gdp_1900, series_life_expectancy_1900)
        plt.xlabel('Gross Domestic Product')
        plt.ylabel('Life Expectancy')
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.title('1900')
        plt.show()

    # occurs if terminate the script prematurely, by pressing Ctrl+C
    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(f"Error processing data: {e}")


if __name__ == "__main__":
    main()
