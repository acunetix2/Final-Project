
# covid19_global_data_tracker.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data(filepath="owid-covid-data.csv"):
    try:
        df = pd.read_csv(filepath)
        print("✅ Data loaded successfully.")
        return df
    except FileNotFoundError:
        print("❌ File not found. Make sure 'owid-covid-data.csv' is in the working directory.")
        return None

def preprocess_data(df, countries):
    columns = [
        'iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases',
        'total_deaths', 'new_deaths', 'total_vaccinations', 'people_vaccinated',
        'people_fully_vaccinated', 'population'
    ]
    df = df[columns]
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['location'].isin(countries)]
    df = df.sort_values(['location', 'date'])
    df.fillna(method='ffill', inplace=True)
    df.fillna(0, inplace=True)
    return df

def plot_total_cases(df):
    sns.lineplot(data=df, x="date", y="total_cases", hue="location")
    plt.title("Total COVID-19 Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend(title="Country")
    plt.show()

def plot_total_deaths(df):
    sns.lineplot(data=df, x="date", y="total_deaths", hue="location")
    plt.title("Total COVID-19 Deaths Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Deaths")
    plt.show()

def plot_new_cases(df):
    sns.lineplot(data=df, x="date", y="new_cases", hue="location")
    plt.title("Daily New COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.show()

def plot_death_rate(df):
    df['death_rate'] = df['total_deaths'] / df['total_cases']
    sns.lineplot(data=df, x="date", y="death_rate", hue="location")
    plt.title("COVID-19 Death Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Death Rate")
    plt.show()

def plot_vaccinations(df):
    sns.lineplot(data=df, x="date", y="total_vaccinations", hue="location")
    plt.title("Total Vaccinations Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Vaccinations")
    plt.show()

def plot_percent_vaccinated(df):
    df['percent_vaccinated'] = df['people_vaccinated'] / df['population'] * 100
    sns.lineplot(data=df, x="date", y="percent_vaccinated", hue="location")
    plt.title("Percent of Population Vaccinated")
    plt.xlabel("Date")
    plt.ylabel("Percent Vaccinated")
    plt.show()

def main():
    countries = ["Kenya", "India", "United States"]
    df = load_data()
    if df is not None:
        df_countries = preprocess_data(df, countries)
        plot_total_cases(df_countries)
        plot_total_deaths(df_countries)
        plot_new_cases(df_countries)
        plot_death_rate(df_countries)
        plot_vaccinations(df_countries)
        plot_percent_vaccinated(df_countries)

if __name__ == "__main__":
    main()
