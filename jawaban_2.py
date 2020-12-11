import pandas as pd
import pyodbc


data = pd.read_csv (r'city_temperature.csv', sep=',')   
df = pd.DataFrame(data, columns= ['Region', 'Country', 'State', 'City', 'Month', 'Day', 'Year', 'AvgTemperature'])

conn = pyodbc.connect("DRIVER={PostgreSQL Unicode};DATABASE=bootcamp;UID=bootcamp;PWD=Bootcamp*123;SERVER=206.189.80.195;PORT=5432;")

cursor = conn.cursor()

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO bootcamp_test_mita ("Region", "Country", "State", "City", "Month", "Day", "Year", "AvgTemperature")
                VALUES (?,?,?,?,?,?,?,?)'''
                ,
                row.Region, 
                row.Country,
                row.State,
                row.City,
                row.Month,
                row.Day,
                row.Year,
                row.AvgTemperature
                )
conn.commit()