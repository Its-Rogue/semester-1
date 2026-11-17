import random
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def show_histogram_of_ramen_scores(data):
    data["Stars"].hist(bins=20)
    plt.title("Distribution of Ramen Scores")
    plt.xlabel("Stars")
    plt.ylabel("Number of Ramen")
    plt.show()


def show_bar_chart_stars_per_manufacturer(data):
    averages = data.groupby("Brand")["Stars"].mean().sort_values(ascending=False)
    averages.head(20).plot(kind="bar")
    plt.title("Average Score by Manufacturer")
    plt.xlabel("Manufacturer")
    plt.ylabel("Average Stars")
    plt.tight_layout()
    plt.show()


def show_bar_chart_stars_per_country(data):
    averages = data.groupby("Country")["Stars"].mean().sort_values(ascending=False)
    averages.plot(kind="bar")
    plt.title("Average Score by Country")
    plt.xlabel("Country")
    plt.ylabel("Average Stars")
    plt.tight_layout()
    plt.show()


def find_best_per_country(data, country):
    country_data = data[data["Country"].str.lower() == country.lower()]
    if country_data.empty:
        return None
    return country_data["Stars"].idxmax()


def find_worst_per_country(data, country):
    country_data = data[data["Country"].str.lower() == country.lower()]
    if country_data.empty:
        return None
    return country_data["Stars"].idxmin()


def show_piechart_of_manufacturers_by_country(data, country):
    counts = data[data["Country"].str.lower() == country.lower()]["Brand"].value_counts()
    if counts.empty:
        print(f"No ramen found for {country}")
        return
    counts.plot(kind="pie", autopct="%1.1f%%")
    plt.title(f"Manufacturers in {country}")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def print_ramen_rating(rating):
    print(f"Name: {rating['Variety']}")
    print(f"Type of ramen: {rating['Style']}")
    print(f"Manufacturer: {rating['Brand']}")
    print(f"Country of Origin: {rating['Country']}")
    print(f"Stars: {rating['Stars']}")


def show_top_ten(data):
    top_ten = data.sort_values("Stars", ascending=False).head(10)
    for _, rating in top_ten.iterrows():
        print_ramen_rating(rating)
        print("-" * 40)


def random_ramen_review(data):
    rating = data.iloc[random.randrange(len(data))]
    print_ramen_rating(rating)
    country_average = data[data["Country"] == rating["Country"]]["Stars"].mean()
    manufacturer_average = data[data["Brand"] == rating["Brand"]]["Stars"].mean()
    print(f"Country average: {country_average:.2f}")
    print(f"Manufacturer average: {manufacturer_average:.2f}")


def menu():
    print("~ ramen rating database ~")
    print("1 - See distribution of scores")
    print("2 - see average score per country")
    print("3 - see average score per manufacturer")
    print("4 - Get a breakdown of a specific country")
    print("5 - See the top ten ramens")
    print("6 - See a random Ramen")
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6", "Q"]:
        choice = input("Pick an option: ").upper()
    return choice


ramen_data = pd.read_csv(Path(__file__).with_name("ramen-ratings.csv"))

def main():
    while True:
        choice = menu()
        match choice:
            case "1":
                show_histogram_of_ramen_scores(ramen_data)
            case "2":
                show_bar_chart_stars_per_country(ramen_data)
            case "3":
                show_bar_chart_stars_per_manufacturer(ramen_data)
            case "4":
                country = input("Enter country: ").title()
                best = find_best_per_country(ramen_data, country)
                worst = find_worst_per_country(ramen_data, country)
                if best is not None:
                    print("Best:")
                    print_ramen_rating(ramen_data.loc[best])
                if worst is not None:
                    print("Worst:")
                    print_ramen_rating(ramen_data.loc[worst])
                show_piechart_of_manufacturers_by_country(ramen_data, country)
            case "5":
                show_top_ten(ramen_data)
            case "6":
                random_ramen_review(ramen_data)
            case "Q":
                break


if __name__ == "__main__":
    main()
