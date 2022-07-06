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

# running query for number of users who have these event types
print("Checking Data...")

creditInit = """
select name, count(cp_user)
from event left join cp
    on event.cp = cp.id
where event_type = 'credit_card_init'
group by name;
"""

broadbandInit = """
select name, count(cp_user)
from event left join cp
    on event.cp = cp.id
where event_type = 'broadband_init'
group by name;
"""

energyInit = """
select name, count(cp_user)
from event left join cp
    on event.cp = cp.id
where event_type = 'energy_init'
group by name;
"""
# running first query
exec1 = cursor.execute(creditInit)
creditResult = cursor.fetchall()
print("first query complete...")
# running second query
exec2 = cursor.execute(broadbandInit)
broadbandResult = cursor.fetchall()
print("second query complete...")
# running fourth query
exec3 = cursor.execute(energyInit)
energyResult = cursor.fetchall()
print("third query complete...")

cursor.close()
print("DATABASE SUCCESSFULLY ACCESSED")
