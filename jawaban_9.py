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

df = pd.read_sql('SELECT "Region", "Country", "AvgTemperature" FROM (SELECT "Region","Country" ,"AvgTemperature", RANK ()OVER (PARTITION BY "Country" ORDER BY "AvgTemperature") as region from bootcamp_test_mita WHERE "AvgTemperature" >100) as t2 WHERE region = 1 ORDER BY "Region", "Country"',conn)
    
print(df)
