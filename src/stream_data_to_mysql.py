import mysql.connector
import pandas as pd
import time


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LOTUS",
    database="ride_demand"
)

cursor = conn.cursor()

print("Connected successfully!")

df = pd.read_csv("cleaned_Mergeddata_csv.csv")  


print("Starting streaming...\n")

try:
    for index, row in df.iterrows():
        # Convert date format from MM/DD/YYYY to YYYY-MM-DD
        tp_pickup_date = pd.to_datetime(row['tpep_pickup_date']).strftime('%Y-%m-%d')
        
        query = """
        INSERT INTO ride (tpep_pickup_date, tpep_pickup_time, tpep_dropoff_time, passenger_count, trip_distance, pickup_longitude, pickup_latitude, payment_type, fare_amount, total_amount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            tp_pickup_date,
            str(row['tpep_pickup_time']),
            str(row['tpep_dropoff_time']),
            int(row['passenger_count']),
            float(row['trip_distance']),
            float(row['pickup_longitude']),
            float(row['pickup_latitude']),
            int(row['payment_type']),   
            float(row['fare_amount']),
            float(row['total_amount'])
        )

        cursor.execute(query, values)
        conn.commit()

        print(f"Inserted row {index}")
        time.sleep(1)
except Exception as e:
    print("Error during insert:", e)
finally:
    cursor.close()
    conn.close()
    print("Connection closed")