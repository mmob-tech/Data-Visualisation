from turtle import color
from unicodedata import name
from matplotlib import pyplot as plt
from task4 import *
import numpy as np
from task1 import mmob_environment
from datetime import date

# Getting date
today = date.today()
dateToString = today.strftime("%d/%m/%Y")

# creating dictionary
cpData = []
# Turning results into list of dictionaries
dictionary = {}
for item in firstResponseResult:
    # Assigning values in the tuple list into the dictionary
    dictionary["Postcode"] = item[0]
    dictionary["first call"] = item[1]
    # Looping through the cached homebox calls result
    for element in secondResponseResult:
        # Checking the postcodes match
        if element[0] != item[0]:
            # If it doesn't - loop through until it does otherwise ignore
            continue
        else:
            # Append the dictionary with number of cached calls
            dictionary["second call"] = element[1]
            # Copy the information into a second dictionary
            dictionaryCopy = dictionary.copy()
            # Append the list with the data retrieved
            cpData.append(dictionaryCopy)

# Creating a names list
names = []
for item in cpData:
    names.append(item["Postcode"])

# Getting percentage
cachedCalls = []
for item in cpData:
    cachedCalls.append(item["second call"])

# CREATING GRAPH
# Making graph more readable
plt.figure(figsize=(15, 4))
# x_pos = np.arange(len(names))
plt.tick_params(axis="x", which="major", labelsize=6)

# Assigning values to the table
plt.bar(
    names,
    cachedCalls,
    color=["green", "blue", "Red", "Cyan", "purple", "orange"],
)

# Rotating x labels
plt.xticks(names, rotation=90)

# Adjusting positioning of graph
plt.subplots_adjust(bottom=0.4, top=0.85)

# Graph title
title = "# of cached homebox calls"
env = "environment: " + mmob_environment
fDate = dateToString
plt.title(
    "{0} - {1} - {2}".format(title, env, fDate),
    fontname="Times New Roman",
    size=18,
    fontweight="bold",
)

# Labelling x axis
plt.xlabel("CP Postcode", fontname="Times New Roman", fontsize=16)

# Labelling y axis
plt.ylabel("# of cached calls", fontname="Times New Roman", fontsize=16)
plt.ylim(0, max(cachedCalls) * 1.2)

# Display graph
plt.show()
