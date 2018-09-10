# Logs Analysis Project

Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

# Solution for Generate the Reports with Below Requirements

**1. What are the most popular three articles of all time?**
**2. Who are the most popular article authors of all time?**
**3. On which days did more than 1% of requests lead to errors?**

# Technologies

**1. PSQL**
**2. Python3**
**3. Virtual Machine**
**4. DB-API**

# SETUP

1. Install **vagrant**
2. Install **Virtual Box**
2. Download **newsdata.sql** 

#PSQL VIEW Query for Get the Error Percentage

**CREATE VIEW errorsdetails AS SELECT TO_CHAR(time ::date, 'Mon dd, yyyy') AS date, COUNT(*) AS tot, COUNT( CASE WHEN (status != '200 OK') THEN 1 END) AS fail, ROUND((COUNT( CASE WHEN (status != '200 OK') THEN 1 END)::decimal / COUNT(*)::decimal) * 100::numeric, 2) AS per FROM log GROUP BY time ::date HAVING ((COUNT( CASE WHEN (status != '200 OK') THEN 1 END)::decimal / COUNT(*)::decimal) * 100) > 1  ORDER BY date; **