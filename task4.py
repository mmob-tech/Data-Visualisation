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
firstResponse = """
select DISTINCT postcode, count(cp.id)
from cp_user cp left join event
on cp.id = event.cp_user
where event.event_type = 'homebox_api_response'
and postcode is not null
and postcode <> ''
group by postcode;
"""
# running query for second call
secondResponse = """
select DISTINCT postcode, count(cp.id)
from cp_user cp left join event
on cp.id = event.cp_user
where event.event_type = 'homebox_api_response_cached'
and postcode is not null
and postcode <> ''
group by postcode;
"""

# running first query
exec1 = cursor.execute(firstResponse)
firstResponseResult = cursor.fetchall()

# running second query
exec2 = cursor.execute(secondResponse)
secondResponseResult = cursor.fetchall()


cursor.close()
print("DATABASE SUCCESSFULLY ACCESSED")
