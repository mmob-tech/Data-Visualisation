from re import I
from turtle import fd
from xml.etree.ElementTree import tostring
from matplotlib import pyplot as plt
from matplotlib import text
from task1 import *
from datetime import date

# Getting date
today = date.today()
dateToString = today.strftime("%d/%m/%Y")


def barChartOrders():
    print("loading...")

    # creating empty lists
    tpp = []
    numOfOrders = []

    # Adding data to lists
    for item in result:
        tpp.append(item[0])
        numOfOrders.append(item[1])

    # Making graph more readable
    plt.figure(figsize=(15, 4))

    # Assigning values to the table
    plt.bar(tpp, numOfOrders, color=["black", "red", "green", "blue", "cyan"])
    plt.subplots_adjust(bottom=0.4, top=0.85)

    title = "# of orders placed by TPP's"
    env = mmob_environment
    fDate = dateToString
    # Graph title
    plt.title(
        "{0} - {1} - {2}".format(title, env, fDate),
        size=16,
        fontname="Times New Roman",
        fontweight="bold",
    )

    # Labelling x axis
    plt.xlabel("TPP's", fontname="Times New Roman", size=12)

    # Rotating x labels
    plt.xticks(rotation=90)

    # Labelling y axis
    plt.ylabel("# of orders placed", fontname="Times New Roman", size=12, labelpad=10)

    # Display graph
    plt.show()


barChartOrders()
