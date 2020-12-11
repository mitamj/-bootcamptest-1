import psycopg2
import pandas as pd
import sys

connection_info = {
    "host"      : "206.189.80.195",
    "database"  : "bootcamp",
    "user"      : "bootcamp",
    "password"  : "Bootcamp*123"
}
conn = None

try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**connection_info)
    print("Nomor 3")
    print("")
    cursor = conn.cursor()
    cursor.execute('SELECT "Region", COUNT("Country") as TotalCountry FROM (SELECT "Region","Country" FROM bootcamp_test_mita GROUP BY "Region", "Country") as tabel GROUP BY "Region" ')
    data = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(data, columns=['Region','TotalCountry'])
    print(df)

    print("Nomor 4")
    print("")
    cursor = conn.cursor()
    cursor.execute("SELECT \"Country\" , \"Year\" , max(\"AvgTemperature\"), min(\"AvgTemperature\") FROM bootcamp_test_mita WHERE (\"Country\" = 'Canada' or \"Country\" = 'Malaysia' or \"Country\"='Turkey') and \"Year\" = 2018 GROUP BY \"Country\", \"Year\"")
    data1 = cursor.fetchall()
    cursor.close()
    df1 = pd.DataFrame(data1, columns=['Country','Year','Max temperature','Min Temperature'])
    print(df1)

    print("Nomor 5")
    print("")
    cursor = conn.cursor()
    cursor.execute('SELECT "Region" ,"Country" , "AvgTemperature" FROM (SELECT "Region", "Country", "AvgTemperature", "Day", "Month" , "Year" , Rank() over (PARTITION BY "Region" ORDER BY "AvgTemperature") as Region FROM bootcamp_test_mita WHERE "Day" = 1 AND "Month" = 10 AND "Year" = 2012) AS t2 WHERE Region <=5')
    data2 = cursor.fetchall()
    cursor.close()
    df2 = pd.DataFrame(data2, columns=['Region','Country','AvgTemperature'])
    print(df2)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit(1) 
print("Connection successful")