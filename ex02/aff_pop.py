import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def parse_population(value) -> float | None:
    """Parse population from strings with k, M, or B into float in millions."""

    if 'k' in value:
        return float(value.replace('k', '')) / 1000
    elif 'M' in value:
        return float(value.replace('M', ''))
    elif 'B' in value:
        return float(value.replace('B', '')) * 1000

    try:
        return float(value)
    except ValueError:
        return None


def test_parse_population():
    """Test the parse_population function."""

    assert parse_population('1.0') == 1.0
    assert parse_population('1.0k') == 0.001
    assert parse_population('1.0M') == 1.0
    assert parse_population('1.0B') == 1000.0
    assert parse_population('1.0T') is None
    assert parse_population('abc') is None


def get_population(
        df_country: pd.DataFrame,
        years: list[str]
        ) -> np.ndarray[float | None]:
    """Get the population data for a given country and years."""

    return df_country[years].map(parse_population).values.flatten()


def plot_population(df: pd.DataFrame, country1: str, country2: str):
    """Plot the population trends of two countries."""

    try:
        # Data
        df_country1 = df[df['country'] == country1]
        df_country2 = df[df['country'] == country2]

        # Years
        years = [str(year) for year in range(1800, 2051)]
        pop_country1 = get_population(df_country1, years)
        pop_country2 = get_population(df_country2, years)

        # Plot
        max_pop: float = max(max(pop_country1), max(pop_country2))
        pop_range = range(int(max_pop // 20) + 1)  # floor division

        plt.plot(years, pop_country1, label=country1)
        plt.plot(years, pop_country2, label=country2)
        plt.xticks(['1800', '1840', '1880', '1920',
                    '1960', '2000', '2040'])
        plt.yticks([i * 20 for i in pop_range],
                   [f'{i * 20}M' for i in pop_range])
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.legend(loc='lower right')
        plt.show()

    # occurs if terminate the script prematurely, by pressing Ctrl+C
    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(f"Error processing data: {e}")


def main():
    """Load population data and display a plot for specified countries."""

    df = load("population_total.csv")

    try:
        assert df is not None

    except AssertionError:
        print("Failure to load data.")
        return

    plot_population(df, 'Belgium', 'France')


if __name__ == "__main__":
    test_parse_population()
    main()
