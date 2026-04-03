use ride_demand;
create table ride(
	id int auto_increment primary key,
	tpep_pickup_date date,
    tpep_pickup_time time,
    tpep_dropoff_time time,
    passenger_count int,
    trip_distance float,
    pickup_longitude float,
    pickup_latitude float,	
    payment_type int,	
    fare_amount float,	
    total_amount float
);
select * from ride;
select * from ride limit 10;

select hour(tpep_pickup_time) AS hour , count(*) AS ride_count from ride
group by hour
order by ride_count ASc;

select day(tpep_pickup_date) as day, count(*) as ride_count from ride
group by day
order by day desc;



SELECT 
    MONTH(tpep_pickup_date) AS month,
    COUNT(*) AS ride_count
FROM ride
GROUP BY month
ORDER BY month;

select 
round(pickup_latitude,2) as  latzone,
round(pickup_longitude,2) as lonzone,
count(*) demand
from ride
group by latzone,lonzone
order by demand desc
limit 1;

CREATE TABLE rides_backup AS SELECT * FROM ride;

SET SQL_SAFE_UPDATES = 0;

UPDATE ride
SET tpep_pickup_date = 
    CONCAT(
        IF(RAND() < 0.5, '2015', '2016'), '-',
        LPAD(FLOOR(1 + RAND() * 3), 2, '0'), '-',
        LPAD(FLOOR(1 + RAND() * 28), 2, '0')
    )
WHERE id > 0;