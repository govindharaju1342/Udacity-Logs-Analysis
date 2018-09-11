# Logs Analysis Project

Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

### Technologies

**1. PSQL** <br />
**2. Python3** <br />
**3. Virtual Machine** <br />
**4. DB-API** <br />

### How to Install?

  * Install [Python3](https://www.python.org/)
  * Install [Vagrant](https://www.vagrantup.com/)
  * Install [VirtualBox](https://www.virtualbox.org/)
  * Download the [vagrant](https://s3.amazonaws.com/video.udacity-data.com/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip) folder
  * Download the sql data [data](https://github.com/govindharaju1342/Udacity-Logs-Analysis/blob/master/newsdata.zip).


### How to RUN
  1. Go to vagrant directory
  2. Run $ <b>vagrant up</b> to start the VM
  3. Run $ <b>vagrant ssh</b> to login into VM
  4. Run $ <b>psql -d news -f newsdata.sql</b> to start database
  5. Run $ python reports.py

### PSQL VIEW Query for Get the Error Percentage

<b>CREATE VIEW errorsdetails AS SELECT TO_CHAR(time ::date, 'Mon dd, yyyy') AS date, COUNT(*) AS tot, COUNT( CASE WHEN (status != '200 OK') THEN 1 END) AS fail, ROUND((COUNT( CASE WHEN (status != '200 OK') THEN 1 END)::decimal / COUNT(*)::decimal) * 100::numeric, 2) AS per FROM log GROUP BY time ::date HAVING ((COUNT( CASE WHEN (status != '200 OK') THEN 1 END)::decimal / COUNT(*)::decimal) * 100) > 1  ORDER BY date;</b>

### Reports Format -- Output

**1. What are the most popular three articles of all time?** <br />
	   Candidate is jerk, alleges rival -- 338647 views <br />
	   Bears love berries, alleges bear -- 253801 views <br />
	   Bad things gone, say good people -- 170098 views <br />
**2. Who are the most popular article authors of all time?** <br />
	   Ursula La Multa -- 507594 views <br />
	   Rudolf von Treppenwitz -- 423457 views <br />
	   Anonymous Contributor -- 170098 views <br />
	   Markoff Chaney -- 84557 views <br />
**3. On which days did more than 1% of requests lead to errors?** <br />
	  Jul 17, 2016 -- 2.26% errors <br />






