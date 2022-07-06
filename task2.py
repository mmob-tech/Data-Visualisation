import mysql.connector

# connecting to database
mmob_db = mysql.connector.connect(
    host="mmob-db-dev.cluster-cipvwwzhdkxi.eu-west-2.rds.amazonaws.com",
    user="mmob_stag_db",
    password="BAvbpNHikRw4QidDM9yiZzF4bHeR!cnvVGrNDqF",
    database="platform_db",
)

# creating cursor
cursor = mmob_db.cursor()

# running query for users created
print("Checking Data...")
createdUsersQuery = """
select customers.name , count(event_type)
        from event ev left join tpp customers
        on ev.tpp = customers.id
        where event_type = 'tpp_user_created'
        AND tpp is not null
        GROUP BY tpp;
"""

# Shows each tpp who have placed an order
ordersPlacedQuery = """
select customers.name , count(event_type)
        from event ev left join tpp customers
        on ev.tpp = customers.id
        where event_type = 'tpp_order_created'
        AND tpp is not null
        GROUP BY tpp;
"""

print("Attempting to execute...")

# running first query
exec1 = cursor.execute(createdUsersQuery)
usersCreatedResult = cursor.fetchall()


# running second query
exec2 = cursor.execute(ordersPlacedQuery)
ordersPlacedResult = cursor.fetchall()

print("DATABASE SUCCESSFULLY ACCESSED")

cursor.close()
