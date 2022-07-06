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

# running query for number of users who entered their postcode
print("Checking Data...")
postcodeEnteredQuery = """
SELECT name, count(cp_user)
from event left join cp
on event.cp = cp.id
where event_type = 'postcode_entered'
and cp_user is not null
group by name;
"""
# running query for total users
totalUsersQuery = """
SELECT name, count(cp_user)
from event left join cp
on event.cp = cp.id
where cp_user is not null
and name is not null
group by name;
"""

# running first query
exec1 = cursor.execute(postcodeEnteredQuery)
postcodeEnteredResult = cursor.fetchall()

# running second query
exec2 = cursor.execute(totalUsersQuery)
totalUsersResult = cursor.fetchall()


cursor.close()
print("DATABASE SUCCESSFULLY ACCESSED")
