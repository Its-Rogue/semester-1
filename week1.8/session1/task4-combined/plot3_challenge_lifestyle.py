from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def average_bar_chart(data):
    columns = [column for column in data.columns if column.endswith("_Hours_Per_Day")]
    averages = data[columns].mean()
    averages.plot(kind="bar")
    plt.title("Average Hours per Day")
    plt.ylabel("Hours")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def hours_histogram(data, column_name):
    if column_name not in data:
        print(f"Unknown column: {column_name}")
        return
    data[column_name].hist(bins=15)
    plt.title(column_name)
    plt.xlabel("Hours")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()


def hours_pie_chart(data, student_id):
    if student_id < 0 or student_id >= len(data):
        print("Student ID out of range")
        return
    student = data.iloc[student_id]
    columns = [column for column in data.columns if column.endswith("_Hours_Per_Day")]
    student[columns].plot(kind="pie", autopct="%1.1f%%")
    plt.title(f"Hours breakdown for Student {student_id}")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def total_hours_per_stress_level(data, stress_level):
    filtered = data[data["Stress_Level"].str.lower() == stress_level.lower()]
    if filtered.empty:
        print(f"No students have stress level {stress_level}")
        return
    columns = [column for column in filtered.columns if column.endswith("_Hours_Per_Day")]
    totals = filtered[columns].sum()
    totals.plot(kind="bar")
    plt.title(f"Total Hours for {stress_level.title()} Stress")
    plt.ylabel("Total Hours")
    plt.tight_layout()
    plt.show()


def display_menu():
    print("Student Lifestyle Data Analysis")
    print("1 - view average hours per day")
    print("2 - view specific activity")
    print("3 - view per-student breakdown")
    print("4 - view per stress level breakdown")
    print("Q - quit")
    choice = ""
    while choice not in ["1", "2", "3", "4", "Q"]:
        choice = input("Select option: ").upper()
    return choice


data = pd.read_csv(Path(__file__).with_name("lifestyle_data.csv"))

def main():
    while True:
        choice = display_menu()
        match choice:
            case "Q":
                break
            case "1":
                average_bar_chart(data)
            case "2":
                col = input("Enter Hours Per column to analyse: ")
                hours_histogram(data, col)
            case "3":
                stid = int(input("Enter student ID: "))
                hours_pie_chart(data, stid)
            case "4":
                stress_level = input("Enter stress level: ").title()
                total_hours_per_stress_level(data, stress_level)


if __name__ == "__main__":
    main()
