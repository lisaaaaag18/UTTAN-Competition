import math
import csv
import pandas as pd

# The following codes are for the bikeshare data for the summer months of 2021

norm_list = []
total_summer_trips = 0


def Bikeshares_2021_05(file1):    
    '''
    file --> dict

    This function calculates the total number of bikeshare trips each day for the month of May in 2021, not including holidays.
    '''
    Date = []
    Trip_ID = []
    trip_dict = {}
    all_dates = []

    with open(file1, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:   
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1 
                Date.append(row[4])
                all_dates.append(row[4])
                Trip_ID.append(row[0])
        Date_set = set(Date)
        Date_tuple = tuple(Date_set)
        all_date_set = set(all_dates)
        all_dates = list(all_date_set)

    for i in range (0, len(Date_tuple),1):
        trip_count = 0
        for j in range (i, len(Date),1):
            if Date[j] == Date_tuple[i]:
                trip_count += 1
        trip_dict[Date_tuple[i]] = trip_count

    return trip_dict, all_dates

May = Bikeshares_2021_05("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-05.csv")[0]
May_dates = Bikeshares_2021_05("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-05.csv")[1]
#print(len(May_dates))

def Bikeshares_2021_06(file1): 
    '''
    file --> dict

    This function calculates the total number of bikeshare trips each day for the month of June in 2021, not including holidays.
    '''   

    Date = []
    Trip_ID = []
    trip_dict = {}
    all_dates = []

    with open(file1, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:   
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1 
                Date.append(row[4])
                all_dates.append(row[4])
                Trip_ID.append(row[0])
        Date_set = set(Date)
        Date_tuple = tuple(Date_set)
        all_date_set = set(all_dates)
        all_dates = list(all_date_set)
    
    for i in range (0, len(Date_tuple),1):
        trip_count = 0
        for j in range (i, len(Date),1):
            if Date[j] == Date_tuple[i]:
                trip_count += 1
        trip_dict[Date_tuple[i]] = trip_count

    return trip_dict, all_dates

June = Bikeshares_2021_06("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-06.csv")[0]
June_dates = Bikeshares_2021_06("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-06.csv")[1]
#print(len(June_dates))

def Bikeshares_2021_07(file1):    
    '''
    file --> dict

    This function calculates the total number of bikeshare trips each day for the month of July in 2021, not including holidays and free-ride Wednesdays.
    '''
    Date = []
    Trip_ID = []
    trip_dict = {}
    all_dates = []

    with open(file1, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:   
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1 
                Date.append(row[4])
                all_dates.append(row[4])
                Trip_ID.append(row[0])
        Date_set = set(Date)
        Date_tuple = tuple(Date_set)
        all_date_set = set(all_dates)
        all_dates = list(all_date_set)
    
    for i in range (0, len(Date_tuple),1):
        trip_count = 0
        for j in range (i, len(Date),1):
            if Date[j] == Date_tuple[i]:
                trip_count += 1
        trip_dict[Date_tuple[i]] = trip_count

    return trip_dict, all_dates

July = Bikeshares_2021_07("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-07.csv")[0]
July_dates = Bikeshares_2021_07("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-07.csv")[1]
#print(len(July_dates))

def Bikeshares_2021_08(file1):    
    '''
    file --> dict

    This function calculates the total number of bikeshare trips each day for the month of August in 2021, not including holidays.
    '''

    Date = []
    Trip_ID = []
    trip_dict = {}
    all_dates = []

    with open(file1, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:   
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1 
                Date.append(row[4])
                all_dates.append(row[4])
                Trip_ID.append(row[0])
        Date_set = set(Date)
        Date_tuple = tuple(Date_set)
        all_date_set = set(all_dates)
        all_dates = list(all_date_set)
    
    for i in range (0, len(Date_tuple),1):
        trip_count = 0
        for j in range (i, len(Date),1):
            if Date[j] == Date_tuple[i]:
                trip_count += 1
        trip_dict[Date_tuple[i]] = trip_count

    return trip_dict, all_dates

August = Bikeshares_2021_08("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-08.csv")[0]
August_dates = Bikeshares_2021_08("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\Bike share ridership 2021-08.csv")[1]
#print(len(August_dates))

total_dates = May_dates+June_dates+July_dates+August_dates
#print(len(total_dates))

summer_dict = May | June | July | August # Combining all the months into one dictionary
#print(summer_dict)

for i in summer_dict: # Counting total number of bikeshares in the summer
    total_summer_trips += summer_dict[i]

for j in summer_dict: # Normalizing values
    norm_value = summer_dict[j]/total_summer_trips
    norm_list.append(norm_value)
#print(norm_list)

def Temperatures(file1, total_dates):    

    max_temp_list = []
    min_temp_list = []
    avg_temp_list = []

    with open(file1, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:   
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1 
                if row[8] in total_dates:
                    max_temp_list.append(row[10])
                    min_temp_list.append(row[12])

    index1 = min_temp_list.index('')
    min_temp_list[index1] = min_temp_list[index1-1]

    index2 = max_temp_list.index('')
    max_temp_list[index2] = max_temp_list[index2-1]
    
    for i in range (0, len(max_temp_list), 1):
        avg_temp = (float(max_temp_list[i]) + float(min_temp_list[i]))/2
        avg_temp_list.append(avg_temp)

    return max_temp_list, min_temp_list, avg_temp_list

Temps = Temperatures("C:\\Users\\lisaa\\Downloads\\UTTAN Competition\\Datasets\\2021 Daily temperatures.csv", total_dates)
#print(Temps)

df = pd.DataFrame.from_dict(summer_dict, orient = 'index')
df['Normalized Volume'] = norm_list
df['Daily Average Temperature'] = Temps[2]
df['Daily High Temperature'] = Temps[0]
df.to_csv('Data Table.csv',sep=',')
#print(df)