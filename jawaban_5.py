#Tampilkan Negara yg memiliki suhu di antara rentang (20 - 30) dan (50 - 60)

import psycopg2
import pandas as pd
import sys

connection_info = {
    "host"      : "206.189.80.195",
    "database"  : "bootcamp",
    "user"      : "bootcamp",
    "password"  : "Bootcamp*123"
}

print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(**connection_info)

df = pd.read_sql('SELECT "Region" ,"Country" , "AvgTemperature" FROM (SELECT "Region", "Country", "AvgTemperature", "Day", "Month" , "Year" , Rank() over (PARTITION BY "Region" ORDER BY "AvgTemperature") as Region FROM bootcamp_test_mita WHERE "Day" = 1 AND "Month" = 10 AND "Year" = 2012) AS t2 WHERE Region <=5',conn)
    
print(df)
