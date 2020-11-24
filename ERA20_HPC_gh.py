#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import timedelta
from datetime import datetime
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer(url="https://api.ecmwf.int/v1",key="your key here",email="your email here")

Events_List = pd.read_csv(r'Event_List.csv')

for x in range(len(Events_List)):
    ######################################################################################
    ###START TIME AND END TIME FOR OBSERVATION WEBSCRAPE
    ######################################################################################
    Initialization_Year      = int(Events_List['YYYY'][x])
    Initialization_Month     = int(Events_List['MM'][x])
    Initialization_Day       = int(Events_List['DD'][x])
    Initialization_Hour      = int(Events_List['simTime'][x])
    Spinup                   = 12
    margin_of_error          = 12 #hours
    Duration                 = 48
    Initialization_Durration = 48+Spinup+margin_of_error
    ### Obtain the Start and End Times of the Simulation
    Datetime_Initialization  = datetime(Initialization_Year, Initialization_Month, Initialization_Day,Initialization_Hour,0,0)
    Datetime_Termination     = Datetime_Initialization+timedelta(hours=int(Initialization_Durration))
    ### End times
    if Datetime_Termination.month>9:Month_str = str(Datetime_Termination.month)
    else:Month_str = "0"+str(Datetime_Termination.month)   
    if Datetime_Termination.day>9:Day_str = str(Datetime_Termination.day)
    else:Day_str = "0"+str(Datetime_Termination.day)
    str_end = str(Datetime_Termination.year)+Month_str+Day_str
    ### Start times
    if Datetime_Initialization.month>9:Month_str = str(Datetime_Initialization.month)
    else:Month_str = "0"+str(Datetime_Initialization.month)   
    if Datetime_Initialization.day>9:Day_str = str(Datetime_Initialization.day)
    else:Day_str = "0"+str(Datetime_Initialization.day)
    str_begin = str(Datetime_Initialization.year)+Month_str+Day_str

    print('-------------------------------------------------------------------------------------')
    print('Start of Data Download: ...')
    print(Datetime_Initialization)
    print('-------------------------------------------------------------------------------------')
    print('End of Data Download: ...')
    print(Datetime_Termination)
    print('-------------------------------------------------------------------------------------')
   
    DATE1 = str_begin
    DATE2 = str_end
    ############################################################################################################
    ###pl.py: Pressure level data (or model levels)
    ############################################################################################################
    server.retrieve({
          'class'   : "e2",
          'dataset' : "era20c",
          'expver'  : "1",
          'step'    : "0",
          'stream'  : "oper",
          'number'  : "all",
          'levtype' : "pl",
          'levelist': "10/20/30/50/70/100/125/150/200/250/300/350/400/450/500/550/600/650/700/750/800/850/900/925/950/975/1000",
          'date'    : DATE1+"/to/"+DATE2,
          'time'    : "00/06/12/18",
          'origin'  : "all",
          'type'    : "an",
          'param'   : "129.128/133.128/131.128/132.128/130.128/157.128",
          'grid'    : "160",
          'target'  : "ERA-Int_pl_"+DATE1+"_"+DATE2+".grib"})    
    ############################################################################################################
    ###sfc.py: Surface variable data
    ############################################################################################################
    server.retrieve({
          'class'   : "e2",
          'dataset' : "era20c",
          "expver"  : "1",
          'step'    : "0",
          'stream'  : "oper",
          'class'   : "ei",
          'number'  : "all",
          'levtype' : "sfc",
          'date'    : DATE1+"/to/"+DATE2,
          'time'    : "00/06/12/18",
          'type'    : "an",
          'param'   : "134.128/151.128/235.128/167.128/165.128/166.128/168.128/34.128/31.128/141.128/139.128/170.128/183.128/236.128/39.128/40.128/41.128/42.128/33.128",
          'grid'    : "160",
          'target'  : "ERA-Int_sfc_"+DATE1+"_"+DATE2+".grib"})
    ############################################################################################################
    ###fix.py: Fixed data.
    ############################################################################################################
    server.retrieve({
          "class": "e2",
          "dataset": "era20c",
          "date": "1989-01-01", #this stays constant... no changing
          "expver": "1",
          "grid": "160",
          "levtype": "sfc",
          "param": "129.128/172.128",
          "step": "0",
          "stream": "oper",
          "time": "12:00:00",
          "type": "an",
          "target": "ERA_inv.grib",})
  
















