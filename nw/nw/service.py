import requests

import json


from math import*

pi = 3.14159265359

data = json.loads(requests.get("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events").text)
 


def dist(x1, y1, geom):
    x2 = float (geom [0])
    y2 = float (geom [1])
    xx1 = (pi * x1) / 180
    xx2 = (pi * x2) / 180
    yy2 = (pi * y2) / 180
    yy1 = (pi * y1) / 180
    d = sin(xx1)*sin(xx2) + cos(xx1)*cos(xx2)*cos(yy1 - yy2)
    return acos(d) * 6371.830



def lesstime(start,end,dateofEvent):
    date = int(dateofEvent[0:4])
    return(start <= date <= end) 


def func(lat, lon, eventId, rad, start, end):
    ans = []
    for event in data ['events']:
        for category in event ['categories']:
            if category ['id'] == int (eventId):
                for geometry in event ['geometries']:
                    if lesstime (int (start), int (end), geometry ['date']) == True:
                        if dist (float (lat), float (lon), geometry ['coordinates']) <= int (rad):
                            ans.append (event ['title'])
                        else:
                            pass
                    else:
                        pass
            else:
                pass 

            
    return ans  






    

    












    









        
        





    
       
