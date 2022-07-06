from re import I
from matplotlib import pyplot as plt
from task1 import *
import numpy as np
from datetime import date

# Getting date
today = date.today()
dateToString = today.strftime("%d/%m/%Y")


def pieChart():
    print("loading...")
    # creating empty lists
    tpp = []
    numOfOrders = []

    # Putting results into lists
    for item in result:
        tpp.append(item[0])
        numOfOrders.append(item[1])

    # Creating Total orders
    Total = 0
    for item in numOfOrders:
        Total = Total + item

    # Creating 'Other' element
    other = 0
    for item in numOfOrders:
        if item <= Total * 0.02:
            other = other + item
        else:
            continue

    # Removing items in numoforders that are less than 20 and updating the name list
    newTPPList = []
    newOrderList = []
    for name, orders in zip(tpp, numOfOrders):
        if orders > Total * 0.02:
            newTPPList.append(name)
            newOrderList.append(orders)

    # Adding the other variable to the updated list
    newOrderList.append(other)
    newTPPList.append("Other")

    # Creating plot
    pieChart, figure = plt.subplots()
    figure.pie(
        newOrderList,
        labels=newTPPList,
        autopct="%1.1f%%",
        startangle=90,
        textprops={"fontsize": 10},
    )
    figure.axis("equal")
    title = "# of orders placed by TPP's"
    env = "environment: " + mmob_environment
    fDate = dateToString
    plt.title(
        "{0} - {1} - {2}".format(title, env, fDate),
        y=1.08,
        fontname="Times New Roman",
        fontweight="bold",
    )
    # show plot
    plt.show()


pieChart()
