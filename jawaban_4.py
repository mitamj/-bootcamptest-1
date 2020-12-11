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

df = pd.read_sql("SELECT \"Country\" , \"Year\" , max(\"AvgTemperature\"), min(\"AvgTemperature\") FROM bootcamp_test_mita WHERE (\"Country\" = 'Canada' or \"Country\" = 'Malaysia' or \"Country\"='Turkey') and \"Year\" = 2018 GROUP BY \"Country\", \"Year\"",conn)
    
print(df)
