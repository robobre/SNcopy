## DB log in information db_login_info.sh or DB_commissionig_GUI.bat

   Before it is using all tools set up login information in following files.

## SNcopy.py

copy production files to cc storage and parse information from log files and publish it in to db

### requirement:

* python3
* install  mysql.connector, re python module - on cc user space it is posible to install by pip3 --user <package name>

### Run
  
>sncopy.py [option]
  
> -h print this help
  
> -t Tarball file [path/file name]
  
> -l Log file [path/file name]
  
> -h hostname of destination
  
> -u username of remote server
  
> -p password
  
> -d destination  path on remote server
  

## publish_csv_comitioning_data.sh

This tool publish data to commissioning db. Commissioning db will be migrating to stable db after commissionig of SuperNEMO

>### requirement:
  
* python3
* install  mysql.connector, re, csv python module - on cc user space it is posible to install by pip3 --user <package name>
### Run
  
>publish_csv_comitioning_data.sh [name of csv file]

## DB_comissioning_GUI.py 

Gui for publish commissioning run information

### requirement:
  
* python3
* install  mysql.connector, re, PySimpleGUI python module - on cc user space it is posible to install by pip3 --user <package name>
  
### Run:
 > windows DB_commissionig_GUI.bat
 > Linux DB_comissioning_GUI.py
  


