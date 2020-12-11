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

df = pd.read_sql('SELECT "Region", COUNT("Country") as TotalCountry FROM (SELECT "Region","Country" FROM bootcamp_test_mita GROUP BY "Region", "Country") as tabel GROUP BY "Region" ',conn)
    
print(df)
