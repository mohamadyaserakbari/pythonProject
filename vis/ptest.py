import pandas as pd
import numpy
import cv2
import geopy
from geopy.geocoders import Nominatim

# df = pd.read_excel("supermarkets.xlsx",sheet_name=0)
# df = pd.read_csv("supermarkets-commas.txt")
# df.columns = ["ID", "Address", "City", "ZIP", "Country", "Name", "Employees"]
# df2 = df.set_index("ID")
# df3 = pd.read_json("supermarkets.json")
# df3 = df3.set_index("Address")
# df5 = df3.iloc[1:3, 1:4]
# df4 = list(df3.loc[:, "Country"])
# df3 = df3.loc["735 Dolores St":"332 Hill St", "ID":"Country"]
# print(df)
# print("\n")
# print(df2)
# print("\n")
# print(df3)
# print("\n")
# print(df4)
# print("\n", "DF5 is :")
# print(df5)
# dm = pd.merge(left=df2, right=df3, on="ID")
# print(dm)
# nom = Nominatim(user_agent="http")
# location = nom.geocode("Iran,Tehran,Azadi Tower")
# df_new = pd.read_csv("supermarkets.csv")
# df_new["Address"] = df_new["Address"] + ", " + df["City"] + ", " + df_new["State"] + " , " + df_new["Country"]
# df_new["Coordinates"] = df_new["Address"].apply(nom.geocode)
# df_new["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
# df_new["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
# print(df_new)


# a = [[123, 12, 123, 12, 33], [], []]
# aa = numpy.arange(27)
# aa = aa.reshape(3, 3, 3)
# print(aa)

img = cv2.imread("1.png", 1)
img_new = cv2.imwrite("new.png", img)

# for i in img:
#     print(i)

imgs = numpy.hstack((img, img))
print(imgs)