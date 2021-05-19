#!/usr/bin/python3

import PySimpleGUI as sg
import database_connector

try:
  my=database_connector.MYSQL_SIM_DATA(0)
except:
  print ("I can not connect to MYSQL db")
  exit(1)
layout = [[sg.Text("Insert entry")],
[sg.Text("Year"),sg.Input(key='Year',size=(4,1)),sg.Text("Month"),sg.Input(key='Month',size=(2,1)),sg.Text("Day"),sg.Input(key='Day',size=(2,1))],
[sg.Text("Detector system"),sg.Input(key='det_sys')], 
[sg.Text("Operators"),sg.Input(key='operat')],
[sg.Text("Run number"),sg.Input(key='r_nb')],
[sg.Text("Duration"),sg.Input(key='dur')],
[sg.Text("Triger"),sg.Input(key='trg')],
[sg.Text("Description"),sg.Input(key='des')],
[sg.Text("Comment"),sg.Input(key='com')],
[sg.Button("QUIT"),sg.Button("Send"),sg.Button("Print")],
[sg.Text(key="OUTPUT1",size=(30,1))]]

# Create the window
window = sg.Window("Run file database UI", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "QUIT" or event == sg.WIN_CLOSED:
        del my
        break
    if event == "Send":
       try:
          my.det_data_comitioning(values['Year']+'/'+values['Month']+'/'+values['Day'],values['operat'],values['r_nb'],values['dur'],values['trg'],values['des'],values['com'],values['det_sys'])
       except:
          window['OUTPUT1'].update("Database insert was failed",text_color='red')
       else:
          window['OUTPUT1'].update("Database insert was succesfull",text_color='blue')
       
    if event == "Print":
       print (values)
       print (values['Year']+'/'+values['Month']+'/'+values['Day'])

window.close()

