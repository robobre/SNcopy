#!/usr/bin/python
import re
#from __future__ import print_function
class metadata_parser:
    def __init__(self,debug=0):
        self.data={}
        self.DEBUG=debug
    def parse_file(self,filename):
 #       print("Hello World") 
        if self.DEBUG>0 :
            print (conf_path,filename)
#       conf_path="../simdata/"
#        filename="config.d/conf.d/launch_file_0.conf"
#       filename="output_files.d/file_0.meta"
#        filename="config.d/variant.d/variant.profile"
        cf=open(filename)
        line=cf.readline()
        while line:
           # print (line)
           m= re.match("(\S+)\=(\S+)",line)
           if m:
                self.data [m.group(1)]= m.group(2) 
           line=cf.readline()
        cf.close()
#a=metadata_parser(0)
#a.parse_file("/work/breier/praca/SUPERNEMO/data_trans/run_419/snemo_crate-1_run-419.log")
#print a.data
