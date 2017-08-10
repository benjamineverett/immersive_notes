import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname='socialmedia')
c = conn.cursor()

c.execute(
'''CREATE TEMPORARY TABLE last_login_table AS
SELECT userid, MAX(DATE(tmstmp)) AS last_login
FROM logins
GROUP BY userid;''';
)

c.execute(
'''
CREATE TABLE table_one AS
SELECT r.userid,
    DATE(r.tmstmp) AS reg_date,
    l_l_t.last_login AS last_login
FROM registrations as r
JOIN last_login_table AS l_l_t
ON r.userid = l_l_t.userid;'''
)

c.execute(
'''CREATE TEMPORARY TABLE logins_last_2014_08_14 AS
SELECT userid, COUNT(*) AS cnt
FROM logins
WHERE logins.tmstmp > timestamp '2014-08-14' - interval '7 days'
GROUP BY userid;'''
)

c.execute(
'''CREATE TEMPORARY TABLE web_mobile_tb AS
SELECT userid, type, COUNT(type) AS cnt
FROM logins
WHERE DATE(tmstmp) > timestamp '2014-08-07'
GROUP BY userid, type
ORDER BY userid
LIMIT 10;'''
)

c.execute()
