#!/usr/bin/env python3

import psycopg2

DBNAME = "news"   # database name variable

# First question

articlesQuestion = "1. What are the most popular three articles of all time?"

# First question query

articlesQuery = """SELECT a.title, count(*) as view
                FROM log as l, articles as a
                WHERE a.slug = substr(l.path, 10)
                GROUP BY a.title ORDER BY view DESC LIMIT 3;"""
# Second question

authorsQuestion = "2. Who are the most popular article authors of all time?"

# Second question query

authorsQuery = """SELECT au.name, count(*) as num
                FROM articles  as ar
                INNER JOIN authors as au
                ON ar.author = au.id
                INNER JOIN log as l
                ON ar.slug = substring(l.path, 10)
                WHERE l.status LIKE '%200%'
                GROUP BY au.name ORDER BY num DESC"""

# Third question

errorQuestion = "3. On which days did more than 1% of requests lead to errors?"

# Exceute the view query before select the errorsdetails
# CREATE VIEW errorsdetails AS
# SELECT TO_CHAR(time ::date, 'Mon dd, yyyy') AS date,
# COUNT(*) AS tot,
# COUNT( CASE WHEN (status != '200 OK') THEN 1 END) AS fail,
# ROUND((COUNT( CASE WHEN (status != '200 OK')
# THEN 1 END)::decimal / COUNT(*)::decimal) * 100::numeric, 2) AS per
# FROM log GROUP BY time ::date
# HAVING ((COUNT( CASE WHEN (status != '200 OK') THEN 1 END)::decimal
# / COUNT(*)::decimal) * 100) > 1
# ORDER BY date;

errorQuery = """SELECT date, per FROM errorsdetails"""   # Third question query


def executeQuery(sql_query):   # Connect database and execute the query
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

# Call the exceute function with query


articlesResult = executeQuery(articlesQuery)
authorsResult = executeQuery(authorsQuery)
errorResult = executeQuery(errorQuery)


def generatReports():   # Generat the reports
    print("\n")
    print(articlesQuestion)
    for title, views in articlesResult:
        print("   {} -- {} views".format(title, views))
    print("\n")
    print(authorsQuestion)
    for author, views in authorsResult:
        print("   {} -- {} views".format(author, views))
    print("\n")
    print(errorQuestion)
    for date, per in errorResult:
        print("   {} -- {}% errors".format(date, per))
    print("\n")


generatReports()    # Call the generatReports function
