#!usr/bin/python
""" read push.txt and push all the files to destination """

import os
import csv
import time
import logging

#logging config
logging.basicConfig(filename='test.log', level=logging.DEBUG,
   format='%(asctime)s:%(levename)s:%(message)s')

SRC_PATH = os.getcwd()
os.chdir(r'/home/jicheng/MY20')
logging.debug(os.getcwd())
time.sleep(1)
PUSH_CMD = []

FILEPATH = SRC_PATH + r'/push.txt'
with open(FILEPATH,'r') as data_file:
   CSV_DATA = csv.reader(data_file)
   for line in CSV_DATA:
      if(line[0] != "#"):
         PUSH_CMD.append('adb push {} {}'.format(line[0].strip(), line[1].strip()))
         logging.debug('adb push {} {}'.format(line[0].strip(),line[1].strip()))

for cmd in PUSH_CMDS:
   logging.debug(cmd)
   os.system(cmd)
   time.sleep(2)

os.chdir(SRC_PATH)

