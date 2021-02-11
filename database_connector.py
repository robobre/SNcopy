#!/usr/bin/python2.7
import mysql.connector
from mysql.connector import Error
#from metadata_parser import metadata_parser
import datetime
import os

class MYSQL_SIM_DATA:
    def __init__(self,debug=0):
        print ("Constructing....")
        self.connection=None
        self.DEBUG=debug
        self.ConnectDatabase(os.environ['MYSQL_HOST'],os.environ['DB_NAME'],os.environ['DB_USERNAME'],os.environ['DB_PW'])
    def __del__(self):
        if self.connection is not None:
            self.connection.close()
        print ("destructing.....")
    def is_connected(self):
        return self.connection.is_connected()
    def ConnectDatabase(self,h, db, u ,pww):
        #type: (MYSQL_SIM_DATA,str,str,str,str)
        try:
            self.connection = mysql.connector.connect(host=h, database=db,user=u,password=pww)
            if self.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                if self.DEBUG>0:
                    cursor = self.connection.cursor()
                    cursor.execute("select database();")
#        cursor.execute("show tables;")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)
                    cursor.execute("show tables;")
                    record=cursor.fetchall()
                    for i in range(len(record)):
                        print("In database are these tables: ", record[i])
                        print("show columns from "+''.join(record[i]))
                        cursor.execute("show columns from "+''.join(record[i]))
                        record2=cursor.fetchall()
                        for j in range(len(record2)):
                            print(record2[j])
                    cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
            sys.exit(1)
#        finally:
#            if (self.connection.is_connected()):
#                cursor.close()
#                self.connection.close()
#                print("MySQL connection is closed")
    def det_data(self,run_file_ID,Run_date,run_number,type_Profile,Run_Start,Run_End,Shifter_ID,Detector_configuuration,Comment):
         #type: (MYSQL_SIM_DATA,str,str,str,str,str,str)
         #print username
         cursor=self.connection.cursor()
#         cursor.execute("select database()")
         now=datetime.datetime.utcnow()
         cursor.execute("INSERT INTO det_detdata (run_file_ID,Run_date,run_number,type_Profile,Run_Start,Run_End,Detector_configuration,Comment) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(run_file_ID,Run_date,run_number,type_Profile,Run_Start,Run_End,Detector_configuuration,Comment) )
         
         cursor.execute('SELECT last_insert_id()')
         record = cursor.fetchone()
#         print("You're connected to database: ", record)
         self.connection.commit()
         cursor.close()
         return record[0]
     
    def det_runefiles (self,FileID,split_index,filename,Md5sum,filesize,filesid):
         #type: (MYSQL_SIM_DATA,str,str,int,int,str,str,str)
         cursor=self.connection.cursor()
         cursor.execute("INSERT INTO det_runfiles ( split_index,filename,Md5sum,filesize,filesID) VALUES(%s,%s,%s,%s,%s)",( split_index,filename,Md5sum,filesize,filesid))
         cursor.execute('SELECT last_insert_id()')
         record = cursor.fetchone()
       #  cursor.execute("UPDATE det_data SET run_file_ID=%s where ID=%s"%(record[0],det_dataID))
#         cursor.execute
         self.connection.commit()
         cursor.close()
         return record[0]
    def det_ccfile  (self, run_number,det_detdataID, split_index,Filepath,Filename,Filesize,Md5sum,reco_level,status,creation_data):
         #type:(MYSQL_SIM_DATA,int,int,str,int,int,str,str,str,str)
         cursor=self.connection.cursor()
         cursor.execute("INSERT INTO det_ccfile (run_number,det_detdataID, split_index,Filepath,Filename,Filesize,Md5sum,reco_level,status,creation_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s, %s,%s) ",(run_number,det_detdataID, split_index,Filepath,Filename,Filesize,Md5sum,reco_level,status,creation_data))
         cursor.execute('SELECT last_insert_id()')
         record = cursor.fetchone()
#         cursor.execute("UPDATE det_data SET run_file_ID=%s where run_number=%s"%(record[0],det_dataID))
 #         cursor.execute
         self.connection.commit()
         cursor.close()
         return record[0]


    def det_datatrans  (self,trans_time,status ):
       #type:(MYSQL_SIM_DATA,int,int,str,int,int,str,str,str,str)
         cursor=self.connection.cursor()
         cursor.execute("INSERT INTO det_filetransfer ( transfer_time, status) VALUES(%s,%s) ",(trans_time,status))
         cursor.execute('SELECT last_insert_id()')
         record = cursor.fetchone()
#         cursor.execute("UPDATE det_data SET run_file_ID=%s where run_number=%s"%(record[0],det_dataID))
 #         cursor.execute
         self.connection.commit()
         cursor.close()
         return record[0]

#myconnect=MYSQL_SIM_DATA(0)
#rec=myconnect.init_prod("breier","nieco","nieco","nieco2","nieco3","nieco4")
#rec1=myconnect.store_simu(rec,"cc","/adresa/suboru/",10000,10,"hash","5.6.7","comentujem si")
#myconnect.store_reco(rec, rec1 ,"/adresa/recosuboru/",10000,10,10.6.1,1,,hash,comentujem )
#:print("You're connected to database: ", rec)
#conf_path="../simdata/"
#filename="output_files.d/file_0.meta"
#mp=metadata_parser(0)
#mp.parse_file(conf_path,filename)
#print mp.data
