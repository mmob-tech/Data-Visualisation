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
postcodeEntered = []
for item in tppData:
    postcodeEntered.append(item["# of users who entered postcode"])

# Getting list of total users
total = []
for item in tppData:
    total.append(item["Total users"])


def BarChart():

    fig, ax = plt.subplots()
    # aranging bars
    x = np.arange(len(names))
    # width
    width = 0.35

    # Characteristics of the bars
    bar1 = ax.bar(
        x - width / 2,
        postcodeEntered,
        width,
        label="Users who entered their postcode",
        color="Blue",
    )
    bar2 = ax.bar(x + width / 2, total, width, label="Total users", color="Red")

    # Labels
    title = "# of users who entered their postcode"
    env = "environment: " + mmob_environment
    fDate = dateToString
    ax.set_title(
        "{0} - {1} - {2}".format(title, env, fDate), fontname="Times New Roman", fontweight="bold"
    )
    ax.set_xticks(x, names)
    ax.set_ylim([0, max(total) * 1.15])

    # adjusting positioning of the graph
    plt.subplots_adjust(bottom=0.4, top=0.88)

    # legend
    ax.legend()

    ax.bar_label(bar1, padding=3)
    ax.bar_label(bar2, padding=3)

    # Rotating x values
    plt.xticks(rotation=90)
    plt.xlabel("CP's", fontname="Times New Roman", fontsize=13)
    plt.ylabel("# of users", fontname="Times New Roman", fontsize=13)
    plt.show()


BarChart()
