-- a script that displays the top 3 cities temperature
SELECT city, AVG(value) AS avg_temp FROM hbtn_0c_0.temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
