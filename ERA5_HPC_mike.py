#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import timedelta
from datetime import datetime
import cdsapi

North = 90
South = -90
East  = 180
West  = -180

Events_List = pd.read_csv(r'Event_List.csv')

for x in range(11,12):
    ######################################################################################
    ###START TIME AND END TIME FOR OBSERVATION WEBSCRAPE
    ######################################################################################
    Initialization_Year      = int(Events_List['YYYY'][x])
    Initialization_Month     = int(Events_List['MM'][x])
    Initialization_Day       = int(Events_List['DD'][x])
    Initialization_Hour      = int(Events_List['simTime'][x])
    Spinup                   = 12
    Initialization_Durration = 48+Spinup
    ### Obtain the Start and End Times of the Simulation
    Datetime_Initialization  = datetime(Initialization_Year, Initialization_Month, Initialization_Day,Initialization_Hour,0,0)-timedelta(hours=Spinup)
    Datetime_Termination     = Datetime_Initialization+timedelta(hours=int(Initialization_Durration))
    ### End times
    if Datetime_Termination.month>9:
         Month_str = str(Datetime_Termination.month)
    else:
        Month_str = "0"+str(Datetime_Termination.month)   
    if Datetime_Termination.day>9:
        Day_str = str(Datetime_Termination.day)
    else:
        Day_str = "0"+str(Datetime_Termination.day)
    str_end = str(Datetime_Termination.year)+Month_str+Day_str
    ### Start times
    if Datetime_Initialization.month>9:
        Month_str = str(Datetime_Initialization.month)
    else:
        Month_str = "0"+str(Datetime_Initialization.month)   
    if Datetime_Initialization.day>9:
        Day_str = str(Datetime_Initialization.day)
    else:
        Day_str = "0"+str(Datetime_Initialization.day)
    str_begin = str(Datetime_Initialization.year)+Month_str+Day_str
   
    DATE1 = str_begin
    DATE2 = str_end
    ############################################################################################################
    ###SURFACE DATA
    ############################################################################################################
    c = cdsapi.Client()
    c.retrieve('reanalysis-era5-single-levels',{'product_type':'reanalysis','format':'grib','variable':[
                '10m_u_component_of_wind','10m_v_component_of_wind','2m_dewpoint_temperature',
                '2m_temperature','land_sea_mask','mean_sea_level_pressure',
                'sea_ice_cover','sea_surface_temperature','skin_temperature',
                'snow_depth','soil_temperature_level_1','soil_temperature_level_2',
                'soil_temperature_level_3','soil_temperature_level_4','surface_pressure',
                'volumetric_soil_water_layer_1','volumetric_soil_water_layer_2','volumetric_soil_water_layer_3',
                'volumetric_soil_water_layer_4'],
        'date':DATE1+'/'+DATE2,
        'area':str(North)+'/'+str(West)+'/'+str(South)+'/'+str(East),
        'time':['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00',
                '12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00',
                '21:00','22:00','23:00'],
        'grid':"0.25/0.25",},
               'ERA5_'+DATE1+'_'+DATE2+'_sl.grib')
    ############################################################################################################
    ###ISOBARIC SURFACE DATA
    ############################################################################################################
    c = cdsapi.Client()
    c.retrieve('reanalysis-era5-pressure-levels',{'product_type':'reanalysis','format':'grib','pressure_level':[
                '1','2','3','5','7','10','20','30','50','70','100','125',
                '150','175','200','225','250','300','350','400','450',
                '500','550','600','650','700','750','775','800','825',
                '850','875','900','925','950','975','1000'],
            'date':DATE1+'/'+DATE2,
            'area':str(North)+'/'+str(West)+'/'+str(South)+'/'+str(East),
            'time':['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00',
                '12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00',
                '21:00','22:00','23:00'],
            'variable':['geopotential','relative_humidity','specific_humidity',
                'temperature','u_component_of_wind','v_component_of_wind'],
            'grid':"0.25/0.25",},'ERA5_'+DATE1+'_'+DATE2+'_pl.grib')


# In[ ]:




