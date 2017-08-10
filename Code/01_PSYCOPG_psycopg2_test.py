import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname='socialmedia')
c = conn.cursor()

today = '2014-08-14'

ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")


userid, registration date and the last login date.
'''join on userid from logins and registrations'''
'''get date from registartion table'''
'''get date for last login from logins table'''

c.execute(
    '''CREATE TABLE assignment_table AS
    SELECT l.userid, DATE(r.tmstmp) AS reg_date, DATE(l.tmstmp) AS last_login
    FROM logins AS l
    JOIN registrations AS r
    ON l.userid = r.userid;'''
    )
conn.commit()









# conn.commit()
# conn.close()
#
# conn = psycopg2.connect(dbname='socialmedia')
# c = conn.cursor()
#
# go_on = input('Look at next line?: ')
# while go_on == 'y':
#     c.execute('''SELECT userid1 FROM friends LIMIT 10;''')
#     print(c.fetchone())
#     go_on = input('look at next one?: ')
#
# conn.close()
