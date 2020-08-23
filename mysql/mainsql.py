import mysql.connector
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# import xlrd
#
# user = xlrd.open_workbook("1.xls")
# sheet = user.sheet_by_name("user_test")
# mydb = mysql.connector.connect(
#     user="root",
#     password="",
#     database="learn"
# )
# cursor = mydb.cursor()
# query = """INSERT INTO user(fname, lname, sex, age, email) VALUES("%s", "%s", "%s", "%s", "%s") """
# for r in range(1, sheet.nrows):
#     fname = sheet.cell(r, 0).value
#     lname = sheet.cell(r, 1).value
#     sex = sheet.cell(r, 2).value
#     age = sheet.cell(r, 3).value
#     email = sheet.cell(r, 4).value
#     values = (fname, lname, sex, age, email)
#     cursor.execute(query, values)
# cursor.close()
# mydb.commit()
# mydb.close()--
# print("")
# print("All done!")
# print("")
# columns = str(sheet.ncols)
# rows = str(sheet.nrows)
# print("I import " + columns + " col and " + rows + " rows to mysql!")
# con = mysql.connector.connect(
#     user="root",
#     password="",
#     database="learn"
# )
#
# cursor = con.cursor()
# agee = input("Enter the upper age:")
# query = cursor.execute("select * from user where age > '%s'" %agee)
# res = cursor.fetchall()
# n = 0
# if res:
#     for i in res:
#         print(i)
#         n = n + 1
#     print(n)
# else:
#     print("No result!")


# from bs4 import BeautifulSoup as bs
# import requests
#
# r = requests.get("https://robord.ir")
# soup = bs(r.content)
# print(soup.prett)


mydb = mysql.connector.connect(
    user="root",
    password="",
    database="learn"
)
query = """select cast(user_registered as date) as start_day , count(display_name) from myli_users group by date(start_day)"""
try:
    cursor = mydb.cursor()
    cursor.execute(query)
    a = np.array(list(cursor))
    b = 0
    a21 = []
    a22 = []
    while b < len(a):
        a21.append(a[b][0])
        a22.append(a[b][1])
        b = b + 1
        #print(a21, a22)
    plt.plot(a21, a22)
    plt.show()
    plt.savefig('figure.jpg',)
finally:
    cursor.close()
    mydb.commit()
    mydb.close()
print("")
print("All done!")
print("")
