# Logs Analysis Project

Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

# Solution for Generate the Reports with Below Requirements

**1. What are the most popular three articles of all time?** <br />
**2. Who are the most popular article authors of all time?** <br />
**3. On which days did more than 1% of requests lead to errors?** <br />

# Technologies

**1. PSQL** <br />
**2. Python3** <br />
**3. Virtual Machine** <br />
**4. DB-API** <br />

# SETUP

1. Install **vagrant** <br />
2. Install **Virtual Box** <br />
2. Download **newsdata.sql**  <br />

# PSQL VIEW Query for Get the Error Percentage

CREATE VIEW errorsdetails AS SELECT TO_CHAR(time ::date, 'Mon dd, yyyy') AS date, COUNT(*) AS tot, COUNT( CASE WHEN (status != '200 OK') THEN 1 END) AS fail, ROUND((COUNT( CASE WHEN (status != '200 OK') THEN 1 END)::decimal / COUNT(*)::decimal) * 100::numeric, 2) AS per FROM log GROUP BY time ::date HAVING ((COUNT( CASE WHEN (status != '200 OK') THEN 1 END)::decimal / COUNT(*)::decimal) * 100) > 1  ORDER BY date;


# RUN

python reports.py

