import pandas as pd
from datetime import datetime

ahs_energy = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\2016-2019 - AHS Daily (2300-0400)-Sample1.csv", skiprows=4, usecols=range(8), header=None, names=['Date','HSKE','HSDG','LVPL','HSDL','HSM','HSCC','HSMC'])
#uploads the data, and skips the 2015 values and renames each column

ahs_energy["Date"]= pd.to_datetime(ahs_energy["Date"], errors ='coerce')
#make the date column in to a datetime data type inorder to find day of week and year

ahs_energy["HSKE"] = pd.to_numeric(ahs_energy.HSKE, errors='coerce')
ahs_energy["HSDG"] = pd.to_numeric(ahs_energy.HSDG, errors='coerce')
ahs_energy["LVPL"] = pd.to_numeric(ahs_energy.LVPL, errors='coerce')
ahs_energy["HSDL"] = pd.to_numeric(ahs_energy.HSDL, errors='coerce')
ahs_energy["HSM"] = pd.to_numeric(ahs_energy.HSM, errors='coerce')
ahs_energy["HSCC"] = pd.to_numeric(ahs_energy.HSCC, errors='coerce')
ahs_energy["HSMC"] = pd.to_numeric(ahs_energy.HSMC, errors='coerce')
#makes the data a float instead of object to find the total energy for each day


ahs_energy['Total Energy'] = ahs_energy.sum(axis=1) # finds total energy for each day


ahs_energy['Weekday'] = ahs_energy['Date'].apply(lambda x: x.weekday()) # make a week day column and assign number 0-6 based on day of the week

ahs_energy['Year'] = ahs_energy['Date'].dt.year # makes a year column to seperate the data into seperate years


def average_energy(day_of_week,year,ahs_energy): # function to calculate the average energy by filtering through the data using the day of the week and year
    ahs_energy_day = ahs_energy[ahs_energy['Weekday'] == day_of_week]
    ahs_energy_day_year = ahs_energy_day[ahs_energy_day['Year'] == year]
    return ahs_energy_day_year['Total Energy'].mean()

print()
print("Average electricity used in AHS between 11 PM and 4 AM per day")
print()
print()

# calls the function and input the day and year wanted and prits the result

#2016 Averages

print("Averages for the year 2016:")
print()

print("Monday: "+str(average_energy(0,2016,ahs_energy))+" kWh")
print("Tuesday: "+str(average_energy(1,2016,ahs_energy))+" kWh")
print("Wednesday: "+str(average_energy(2,2016,ahs_energy))+" kWh")
print("Thursday: "+str(average_energy(3,2016,ahs_energy))+" kWh")
print("Friday: "+str(average_energy(4,2016,ahs_energy))+" kWh")
print("Saturday: "+str(average_energy(5,2016,ahs_energy))+" kWh")
print("Sunday: "+str(average_energy(6,2016,ahs_energy))+" kWh")
print()

#2017 Averages

print("Averages for the year 2017:")
print()

print("Monday: "+str(average_energy(0,2017,ahs_energy))+" kWh")
print("Tuesday: "+str(average_energy(1,2017,ahs_energy))+" kWh")
print("Wednesday: "+str(average_energy(2,2017,ahs_energy))+" kWh")
print("Thursday: "+str(average_energy(3,2017,ahs_energy))+" kWh")
print("Friday: "+str(average_energy(4,2017,ahs_energy))+" kWh")
print("Saturday: "+str(average_energy(5,2017,ahs_energy))+" kWh")
print("Sunday: "+str(average_energy(6,2017,ahs_energy))+" kWh")
print()

#2018 Averages

print("Averages for the year 2018:")
print()

print("Monday: "+str(average_energy(0,2018,ahs_energy))+" kWh")
print("Tuesday: "+str(average_energy(1,2018,ahs_energy))+" kWh")
print("Wednesday: "+str(average_energy(2,2018,ahs_energy))+" kWh")
print("Thursday: "+str(average_energy(3,2018,ahs_energy))+" kWh")
print("Friday: "+str(average_energy(4,2018,ahs_energy))+" kWh")
print("Saturday: "+str(average_energy(5,2018,ahs_energy))+" kWh")
print("Sunday: "+str(average_energy(6,2018,ahs_energy))+" kWh")
print()







