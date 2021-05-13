#!/usr/bin/python3
# encoding: utf-8
import re
import os
import database_connector
import getopt,sys
import csv
def publish_data(filename):
    myDB=database_connector.MYSQL_SIM_DATA()
    with open(filename,'r',encoding='utf-8') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=';')
      line_count = 0
      for row in csv_reader:
         if line_count == 0:
           print(f'Column names are {", ".join(row)}')
           line_count += 1
         else:
           myDB.det_data_comitioning(row[3].strip(),row[2],row[0],row[4],row[5],row[6],row[7],row[1])
           print(row[3],row[2],row[0],row[4],row[5],row[6],row[7],row[1])
           line_count += 1
           print(f'Processed {line_count} lines.')

#    my.det_data_comitioning(row[4],row[3],row[1],row[5],row[6],row[7],row[8],row[2])

try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:v", ["help", "input="])
except getopt.GetoptError as err:
        print(err) 
        print("run ./publish_csv_comitioning_data.sh --input<name of input csv file")
        sys.exit(2)
input='none'
for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            print("run ./publish_csv_comitioning_data.sh --input<name of input csv file")
            sys.exit()
        elif o in ("-i", "--input"):
            filename = a
        else:
            assert False, "unhandled option"
        print(filename)
publish_data(filename)
     
