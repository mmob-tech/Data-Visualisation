from matplotlib import pyplot as plt
from task2 import *
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
for item in usersCreatedResult:
    # Assigning values in the tuple list into the dictionary
    dictionary["TPP Name"] = item[0]
    dictionary["Users created"] = item[1]
    # Looping through the orders placed tuple list
    for element in ordersPlacedResult:
        # Checking the names match
        if element[0] != item[0]:
            # If it doesn't - loop through until it does
            continue
        else:
            # Append the dictionary with orders placed
            dictionary["Orders Placed"] = element[1]
            # Copy the information into a second dictionary
            dictionaryCopy = dictionary.copy()
            # Append the list with the data retrieved
            tppData.append(dictionaryCopy)

# getting percentage for each TPP
percentageList = []
for dict in tppData:
    # Calculating percentage of orders placed over users created
    percentages = ((dict["Orders Placed"]) / (dict["Users created"])) * 100
    # Adding result into list
    percentageList.append(percentages)

# Getting names from object
namesList = []
for dict in tppData:
    # Creating names list for graph
    names = dict["TPP Name"]
    namesList.append(names)


def BarChart():

    # Making graph more readable
    plt.figure(figsize=(15, 4))
    x_pos = np.arange(len(namesList))

    # Assigning values to the table
    plt.bar(
        x_pos,
        (percentageList),
        color=["green", "blue", "Red", "Cyan"],
    )

    # Rotating x labels
    plt.xticks(x_pos, namesList, rotation=90)

    # Adjusting positioning of graph
    plt.subplots_adjust(bottom=0.4, top=0.85)

    # Graph title
    title = "Orders placed per TPP per user"
    env = "environment: " + mmob_environment
    fDate = dateToString
    plt.title(
        "{0} - {1} - {2}".format(title, env, fDate),
        size=16,
        fontname="Times New Roman",
        fontweight="bold",
    )

    # Labelling x axis
    plt.xlabel("Names", fontname="Times New Roman", fontsize=14)

    # Labelling y axis
    plt.ylabel("Percentage (%)", fontname="Times New Roman", fontsize=14)

    # Display graph
    plt.show()


BarChart()
