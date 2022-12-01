-- import hbtn_0c_0 and display top 3 city temp between July and August
SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE month = 7 OR month = 8
group by city order by avg_temp DESC
LIMIT 3
