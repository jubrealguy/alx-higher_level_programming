-- import in hbtn_0c and display temp by city and ordered by temp
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC
