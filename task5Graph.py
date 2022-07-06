from datetime import date
from matplotlib import pyplot as plt
import numpy as np
from task5 import *
from task1 import mmob_environment

# Getting date
today = date.today()
dateToString = today.strftime("%d/%m/%Y")

# Creating empty lists
initData = []
broadbandData = []
energyData = []
remaindersData = []
cpNoProducts = []
# Turning results into list of dictionaries
dictionary = {}

# Create list of dictionaries for all CP's that have credit users
for item in creditResult:
    dictionary["CP name"] = item[0]
    dictionary["Broadband users"] = 0
    dictionary["Credit users"] = item[1]
    dictionary["Energy users"] = 0
    dictionaryCopy = dictionary.copy()
    initData.append(dictionaryCopy)

# Create list of dictionaries for all CP's that have Broadband users
for item in broadbandResult:
    dictionary["CP name"] = item[0]
    dictionary["Credit users"] = 0
    dictionary["Broadband users"] = item[1]
    dictionary["Energy users"] = 0
    dictionaryCopy = dictionary.copy()
    broadbandData.append(dictionaryCopy)

# Create list of dictionaries for all CP's that have Energy users
for item in energyResult:
    dictionary["CP name"] = item[0]
    dictionary["Credit users"] = 0
    dictionary["Broadband users"] = 0
    dictionary["Energy users"] = item[1]
    dictionaryCopy = dictionary.copy()
    energyData.append(dictionaryCopy)

# Checks whether the CP name occurs already in the init data
for broadband_cp in broadbandData:
    init_data_cp = [item for item in initData if item.get("CP name") == broadband_cp.get("CP name")]
    if init_data_cp == []:
        # Create new dictionary
        new_cp = {}
        new_cp["CP name"] = broadband_cp.get("CP name")
        new_cp["Broadband users"] = broadband_cp.get("Broadband users")
        new_cp["Credit users"] = 0
        new_cp["Energy users"] = 0
        # Append initData with the new CP
        initData.append(new_cp)

# Checks the CP name is the same - if so update broadband users with the new data
for item in initData:
    for name in broadbandData:
        if item["CP name"] == name["CP name"]:
            item["Broadband users"] = name["Broadband users"]

# Checks there is an occurence of CP name if so update
for energy_cp in energyData:
    init_data_cp = [item for item in initData if item.get("CP name") == item.get("CP name")]
    if init_data_cp == []:
        # Create new dictionary to append to initData
        new_cp = {}
        new_cp["CP name"] = energy_cp.get("CP name")
        new_cp["Energy users"] = energy_cp.get("Energy Users")
        new_cp["Broadband users"] = 0
        new_cp["Credit users"] = 0
        initData.append(new_cp)

for item in initData:
    for name in energyData:
        if name["CP name"] == item["CP name"]:
            item["Energy users"] = name["Energy users"]

# List of names for graph
names = []
for item in initData:
    names.append(item["CP name"])

# List of broadband users for graph
broadbandUsers = []
for item in initData:
    broadbandUsers.append(item["Broadband users"])

# List of credit users for graph
creditUsers = []
for item in initData:
    creditUsers.append(item["Credit users"])

# List of Energy users for graph
energyUsers = []
for item in initData:
    energyUsers.append(item["Energy users"])


# # CREATING GRAPH
fig, ax = plt.subplots()
# width
barWidth = 0.25
# position of bars
pos1 = np.arange(len(names))
pos2 = [x + barWidth for x in pos1]
pos3 = [x + barWidth for x in pos2]

# Characteristics of the bars
bar1 = ax.bar(
    pos1,
    broadbandUsers,
    width=barWidth,
    label="Broadband users",
    color="#2d7f5e",
)
bar2 = ax.bar(pos2, creditUsers, width=barWidth, label="Credit users", color="#7f6d5f")
bar3 = ax.bar(pos3, energyUsers, width=barWidth, label="Energy users", color="#557f2d")

# Labels
title = "Popularity of products"
env = "environment: " + mmob_environment
fDate = dateToString
ax.set_title(
    "{0} - {1} - {2}".format(title, env, fDate), fontname="Times New Roman", fontweight="bold"
)
plt.xticks([r + barWidth for r in range(len(bar1))], names)
# ax.set_ylim([0, max(energyUsers) * 1.2])

# adjusting positioning of the graph
plt.subplots_adjust(bottom=0.4, top=0.88)
ax.set_ylim([0, max(broadbandUsers) * 1.15])

# legend
ax.legend()

ax.bar_label(bar1, padding=3)
ax.bar_label(bar2, padding=3)
ax.bar_label(bar3, padding=3)

# Rotating x values
plt.xticks(rotation=90)
plt.xlabel("CP's", fontname="Times New Roman", fontsize=13)
plt.ylabel("# of users", fontname="Times New Roman", fontsize=13)
plt.show()
