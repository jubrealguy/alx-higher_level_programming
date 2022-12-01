-- import hbtn_0c_0 and display the max temperature of each state
SELECT state, MAX(value) as max_temp from temperature group by state order by state ASC LIMIT 3
