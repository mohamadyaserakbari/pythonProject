from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='learn')
cursor = cnx.cursor()
cursor.execute('insert into people values (\'far\',\'f\',38)')
cnx.close()