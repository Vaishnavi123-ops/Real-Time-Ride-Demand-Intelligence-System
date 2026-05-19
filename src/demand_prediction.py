import mysql.connector
import pandas as pd
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LOTUS",
    database="ride_demand"
)

query="""
select
    hour(tpep_pickup_time) AS hour ,
    count(*) AS demand 
from ride
group by hour
order by hour
"""
hourly_demand = pd.read_sql(query,conn)

x=hourly_demand[['hour']]
y=hourly_demand['demand']

poly = PF(degree=3)
X_poly = poly.fit_transform(hourly_demand[['hour']])

model = LR()
model.fit(X_poly, hourly_demand['demand'])

hourly_demand['predicted_demand'] = model.predict(X_poly)
hourly_demand['predicted_demand'] = hourly_demand['predicted_demand'].astype(int)

hourly_demand['alert']=hourly_demand['predicted_demand'].apply(
    lambda x: "⚠️  HIGH DEMAND" if x> 350 else "Medium"
)

hourly_demand["decision"] = hourly_demand['predicted_demand'].apply(
    lambda x: "Increase Drivers" if x> 350
    else "Reduce Drivers" if x<50
    else "maintain"
)

print(hourly_demand)
hourly_demand.to_csv("hourly_demand_output.csv", index=False)