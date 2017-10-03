#!usr/bin/python
""" read push.txt and push all the files to destination """

import os
import csv
import time

SRC_PATH = os.getcwd()
os.chdir(r'/home/jicheng/MY20')
print(os.getcwd())
time.sleep(1)
PUSH_CMD = []

FILEPATH = SRC_PATH + r'/push.txt'
with open(FILEPATH,'r') as data_file:
   CSV_DATA = csv.reader(data_file)
   for line in CSV_DATA:
      if(line[0] != "#"):
         PUSH_CMD.append('adb push {} {}'.format(line[0].strip(), line[1].strip()))

for cmd in PUSH_CMDS:
   print(cmd)
   os.system(cmd)
   time.sleep(2)

os.chdir(SRC_PATH)

