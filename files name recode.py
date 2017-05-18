#This code takes files in one folder which have , and - in the name 
#replaces these with m and c, and copies them to another folder

path2 = "filepath1"
import os
path="filepath2"
for filename in os.listdir(path):
     if filename.endswith(".jpg"):
      os.rename(os.path.join(path, filename), os.path.join(path2, filename.replace('-','m').replace(',','c')))
