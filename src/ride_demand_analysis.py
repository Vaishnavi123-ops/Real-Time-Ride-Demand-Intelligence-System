import pandas as pd
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LOTUS",
    database="ride_demand"
)


query = "SELECT * FROM ride"
df = pd.read_sql(query, conn)

df['tpep_pickup_time'] = df['tpep_pickup_time'].astype(str).str.replace('0 days ', '')

df['tpep_dropoff_time'] = df['tpep_dropoff_time'].astype(str).str.replace('0 days ', '')

print(df.head())

df = df[
    (df['pickup_latitude'].between(40.5, 41)) &
    (df['pickup_longitude'].between(-74.5, -73))
]

df['lat_zone'] = df['pickup_latitude'].round(2)
df['lon_zone'] = df['pickup_longitude'].round(2)

zone_demand=df.groupby(["lat_zone","lon_zone"]).size().reset_index(name="demand")


zone_demand['demand_level'] = zone_demand['demand'].apply(
    lambda x: "HIGH" if x > 100 else "LOW" if x < 20 else "MEDIUM"
)

zone_demand['alert'] = zone_demand['demand_level'].apply(
    lambda x: "⚠️ SURGE" if x == "HIGH" else "NORMAL"
)


zone_demand['decision'] = zone_demand['demand_level'].apply(
    lambda x: "Increase Drivers" if x == "HIGH"
    else "Reduce Drivers" if x == "LOW"
    else "Maintain"
)


print(zone_demand.sort_values(by='demand', ascending=False))
zone_demand.to_csv("zone_demand_output.csv", index=False)
