## OPEN MYSQL + PYTHON LAB 

import mysql.connector

try:
    DB = mysql.connector.connect(host="localhost",
                                user="abc",
                                password="password")
except:
    print('Unable to connect to DB, Pls verify credentials')
    
print('DB Connected - {}'.format(DB.is_connected()))


create_query = '''CREATE DATABASE IF NOT EXISTS FSDS_DB'''
select_db    = '''USE FSDS_DB'''
create_table = '''CREATE TABLE IF NOT EXISTS FSDS1(
                    name VARCHAR(40), 
                    roll_no INT, 
                    mail_id VARCHAR(50))
               '''
insert_query = '''INSERT INTO FSDS1 values('JOHN', 21, 'JOHN.DOE@gmail.com') '''
display_all_table = '''SELECT * FROM FSDS_DB.FSDS1'''


## CURSOR TO EXECUTE COMMANDS 
cur = DB.cursor()
cur.execute(create_query)
cur.execute(select_db)
cur.execute(create_table)
cur.execute(insert_query)
DB.commit()


## DISPLAY records in DB
cur.execute(display_all_table)
for i in cur:
    print(i)