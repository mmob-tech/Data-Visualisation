import mysql.connector

mmob_environment = "dev"
# connecting to database
mmob_db = mysql.connector.connect(
    host="mmob-db-dev.cluster-cipvwwzhdkxi.eu-west-2.rds.amazonaws.com",
    user="mmob_stag_db",
    password="BAvbpNHikRw4QidDM9yiZzF4bHeR!cnvVGrNDqF",
    database="platform_db",
)

# creating cursor
cursor = mmob_db.cursor()

# running query for tpp and order placed
cursor.execute(
    """select customers.name , count(ev.created) 
        from event ev left join tpp customers
        on ev.tpp = customers.id
        where event_type = 'tpp_order_created'
        AND tpp is not null
        GROUP BY tpp;"""
)

result = cursor.fetchall()
print("DATABASE SUCCESSFULLY ACCESSED")
mmob_db.close()
