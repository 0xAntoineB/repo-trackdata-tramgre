import requests
import csv
import json

def get_pattern_id(datajson:dict) -> all:
    """"""

    data = [] 

    for element in datajson:

        key = element["pattern"]["id"]
        data.append(key)

    return data

def get_pattern_desc(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:

       key = element["pattern"]["desc"]
       data.append(key)

    return data

def get_pattern_dir(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:

       key = element["pattern"]["dir"]
       data.append(key)

    return data

def get_pattern_shortDesc(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:

       key = element["pattern"]["shortDesc"]
       data.append(key)

    return data

def get_pattern_lastStop(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:

       key = element["pattern"]["lastStop"]
       data.append(key)

    return data

def get_pattern_lastStopName(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:

       key = element["pattern"]["lastStopName"]
       data.append(key)

    return data

def get_time_stopid(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:

            key = elements["stopId"]
            data.append(key)

    return data

def get_time_stopname(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:

            try:
                key = elements["stopName"]
                data.append(key)
            except:

                data.append(None)

    return data

def get_time_scheduledarrival(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            
            try:
                key = elements["scheduledArrival"]
                data.append(key)
            except:

                data.append(None)

    return data

def get_time_scheduleddeparture(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            try:
                key = elements["scheduledDeparture"]
                data.append(key)
            except:

                data.append(None)
    return data

def get_time_realtimearrival(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            try:
                key = elements["realtimeArrival"]
                data.append(key)
            except:

                data.append(None)
    return data

def get_time_realtimedeparture(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            try:
                key = elements["realtimeDeparture"]
                data.append(key)
            except:

                data.append(None)
    return data

def get_time_arrivaldelay(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            try:
                key = elements["arrivalDelay"]
                data.append(key)
            except:

                data.append(None)
    return data

def get_time_departuredelay(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            try:
                key = elements["departureDelay"]
                data.append(key)
            except:

                data.append(None)
    return data

def get_time_timepoint(datajson:dict) -> bool:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            
            try:

                key = elements["timepoint"]
                data.append(key)

            except:

                data.append(None)

    return data

def get_time_realtime(datajson:dict) -> bool:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:

            try:

                key = elements["realtime"]
                data.append(key)

            except:

                data.append(None)

    return data

def get_time_realtimestate(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:

            try:

                key = elements["realtimeState"]
                data.append(key)

            except:

                data.append(None)

    return data

def get_time_serviceday(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:

            try:

                key = elements["serviceDay"]
                data.append(key)

            except:

                data.append(None)

    return data

def get_time_tripid(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            
            try:

                key = elements["tripId"]
                data.append(key)

            except:

                data.append(None)

    return data

def get_time_pickupyype(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:

            try:
                key = elements["pickupType"]
                data.append(key)

            except:

                data.append(None)
    return data

def get_time_occupancy(datajson:dict) -> str:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:
            
            try:
            
                key = elements["occupancy"]
                data.append(key)

            except:

                data.append(None)
    return data

def get_time_occupancyid(datajson:dict) -> int:
    """"""

    data = [] 

    for element in datajson:
        for elements in element["times"]:

            key = elements["occupancyId"]
            data.append(key)

    return data

def get_data_response() -> list:
    """"""

    try:
        
        data = []
        url = "https://data.mobilites-m.fr/api/routers/default/index/clusters/SEM:GENMAICULTU/stoptimes"

        headers = {
 
                'origin': 'mon_appli'

            }
 
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
                
            datajson = response.json()

            time_stopid = get_time_stopid(datajson)
            time_stopname = get_time_stopname(datajson)
            time_scheduledarrival = get_time_scheduledarrival(datajson)
            time_scheduleddeparture = get_time_scheduleddeparture(datajson)
            time_realtimearrival = get_time_realtimearrival(datajson)
            time_realtimedeparture = get_time_realtimedeparture(datajson)
            time_arrivaldelay = get_time_arrivaldelay(datajson)
            time_departuredelay = get_time_departuredelay(datajson)
            time_timepoint = get_time_timepoint(datajson)
            time_realtime = get_time_realtime(datajson)
            time_realtimestate = get_time_realtimestate(datajson)
            time_serviceday = get_time_serviceday(datajson)
            time_tripid = get_time_tripid(datajson)
            time_pickupyype = get_time_pickupyype(datajson)
            time_occupancy = get_time_occupancy(datajson)
            time_occupancyid = get_time_occupancyid(datajson)



            for tuple in zip(time_stopid,
                             time_stopname,
                             time_scheduledarrival,
                             time_scheduleddeparture,
                             time_realtimearrival,
                             time_realtimedeparture,
                             time_realtimearrival,
                             time_arrivaldelay,
                             time_departuredelay,
                             time_timepoint,
                             time_realtime,
                             time_realtimestate,
                             time_serviceday,
                             time_tripid,
                             time_pickupyype,
                             time_occupancy,
                             time_occupancyid):
                                

                data.append(list(tuple))
                print(data)

    except Exception as error:

        print(error)

    return data 

def write_tram_data() -> None:
    """"""

    try:

        data = get_data_response()

        with open('/scripts/serpistollillustre/serpistollillustre.csv', 'w', encoding='utf-8', newline='') as file_:

            writer = csv.writer(file_)
            writer.writerows(data)

        print("Ecriture des membres dans le fichier csv")

    except Exception as error:

        print(error)

def filter_csv_data(value) -> None:
    """"""

    filtered_data = []

    try:

        with open('/scripts/serpistollillustre/serpistollillustre.csv', 'r') as file_:
            reader = csv.reader(file_)

            for row in reader:

                if len(row) >= 14 and row[13] == value:
                    filtered_data.append(row)

    except Exception as error:

        print(error)

    return filtered_data

def append_new_data() -> None:
    """"""

    try:

        data = get_data_response()

        with open('/scripts/serpistollillustre/serpistollillustre.csv', 'a', encoding='utf-8', newline='') as file_:
            writer = csv.writer(file_)

            for line in data:

                tripid = line[13]
                if not filter_csv_data(tripid):

                    writer.writerow(line)

                    print("Nouvelles données ajoutées")

                else:

                    print("sa existe :", line[13])

    except Exception as error:

        print(error)

#write_tram_data()
#append_new_data()
