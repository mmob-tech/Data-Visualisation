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
postcodes = []
for item in cpData:
    postcodes.append(item["Postcode"])

# Getting first call
firstCall = []
for item in cpData:
    firstCall.append(item["first call"])
# Getting cached calls
cachedCalls = []
for item in cpData:
    cachedCalls.append(item["second call"])

# CREATING GRAPH
fig, ax = plt.subplots()
# aranging bars
x = np.arange(len(postcodes))
# width
width = 0.35
# x labels positioning
plt.tick_params(axis="x", which="major", labelsize=6)
# Characteristics of the bars
bar1 = ax.bar(
    x - width / 2,
    firstCall,
    width,
    label="First call",
    color="Blue",
)
bar2 = ax.bar(x + width / 2, cachedCalls, width, label="Cached calls", color="green")

# Labels
title = "Cached homebox calls"
env = "environment: " + mmob_environment
fDate = dateToString
ax.set_title(
    "{0} - {1} - {2}".format(title, env, fDate), fontname="Times New Roman", fontweight="bold"
)
ax.set_xticks(x, postcodes)
ax.set_ylim([0, max(cachedCalls) * 1.15])

# adjusting positioning of the graph
plt.subplots_adjust(bottom=0.4, top=0.88)

# legend
ax.legend()

# Rotating x values
plt.xticks(rotation=90)
plt.xlabel("CP's", fontname="Times New Roman", fontsize=13)
plt.ylabel("Cached homebox calls", fontname="Times New Roman", fontsize=13)
plt.show()

# Display graph
plt.show()
