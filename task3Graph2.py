from turtle import color
from unicodedata import name
from matplotlib import pyplot as plt
from task3 import *
import numpy as np
from task1 import mmob_environment
from datetime import date

# Getting date
today = date.today()
dateToString = today.strftime("%d/%m/%Y")

# Dictionary
tppData = []

# Turning results into list of dictionaries
dictionary = {}
for item in postcodeEnteredResult:
    # Assigning values in the tuple list into the dictionary
    dictionary["CP Name"] = item[0]
    dictionary["# of users who entered postcode"] = item[1]
    # Looping through the orders placed tuple list
    for element in totalUsersResult:
        # Checking the names match
        if element[0] != item[0]:
            # If it doesn't - loop through until it does otherwise ignore
            continue
        else:
            # Append the dictionary with total users
            dictionary["Total users"] = element[1]
            # Copy the information into a second dictionary
            dictionaryCopy = dictionary.copy()
            # Append the list with the data retrieved
            tppData.append(dictionaryCopy)

# Getting list of names
names = []
for item in tppData:
    names.append(item["CP Name"])

# Getting list of users who enter postcode
percentageList = []
for item in tppData:
    percentage = ((item["# of users who entered postcode"]) / (item["Total users"])) * 100
    percentageList.append(percentage)

# Getting list of total users
total = []
for item in tppData:
    total.append(item["Total users"])


def BarChart():

    # Making graph more readable
    plt.figure(figsize=(15, 4))
    x_pos = np.arange(len(names))

    # Assigning values to the table
    plt.bar(
        x_pos,
        (percentageList),
        color=["green", "blue", "Red", "Cyan"],
    )

    # Rotating x labels
    plt.xticks(x_pos, names, rotation=90)

    # Adjusting positioning of graph
    plt.subplots_adjust(bottom=0.4, top=0.85)

    # Graph title
    title = "% of users who entered their postcode"
    env = "environment: " + mmob_environment
    fDate = dateToString
    plt.title(
        "{0} - {1} - {2}".format(title, env, fDate),
        size=18,
        fontname="Times New Roman",
        fontweight="bold",
    )

    # Labelling x axis
    plt.xlabel("CP's'", fontname="Times New Roman", fontsize=16)

    # Labelling y axis
    plt.ylabel("Percentage (%)", fontname="Times New Roman", fontsize=16)
    plt.ylim(0, max(percentageList) * 1.2)

    # Display graph
    plt.show()


BarChart()
