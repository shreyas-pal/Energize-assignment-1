import pandas as pd
from datetime import datetime
from functools import reduce


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
    return (ahs_energy_day_year['HSKE'].mean(),ahs_energy_day_year['HSDG'].mean(),ahs_energy_day_year['LVPL'].mean(),ahs_energy_day_year['HSDL'].mean(),ahs_energy_day_year['HSM'].mean(),ahs_energy_day_year['HSCC'].mean(),ahs_energy_day_year['HSMC'].mean())

mA16, mB16, mC16, mD16, mE16, mF16, mG16 = average_energy(0,2016,ahs_energy) # calls the function for each day and store the averaged to data frame
tA16, tB16, tC16, tD16, tE16, tF16, tG16 = average_energy(1,2016,ahs_energy)
wA16, wB16, wC16, wD16, wE16, wF16, wG16 = average_energy(2,2016,ahs_energy)
thA16, thB16, thC16, thD16, thE16, thF16, thG16 = average_energy(3,2016,ahs_energy)
fA16, fB16, fC16, fD16, fE16, fF16, fG16 = average_energy(4,2016,ahs_energy)
saA16, saB16, saC16, saD16, saE16, saF16, saG16 = average_energy(5,2016,ahs_energy)
sA16, sB16, sC16, sD16, sE16, sF16, sG16 = average_energy(6,2016,ahs_energy)


mA17, mB17, mC17, mD17, mE17, mF17, mG17 = average_energy(0,2017,ahs_energy)
tA17, tB17, tC17, tD17, tE17, tF17, tG17 = average_energy(1,2017,ahs_energy)
wA17, wB17, wC17, wD17, wE17, wF17, wG17 = average_energy(2,2017,ahs_energy)
thA17, thB17, thC17, thD17, thE17, thF17, thG17 = average_energy(3,2017,ahs_energy)
fA17, fB17, fC17, fD17, fE17, fF17, fG17 = average_energy(4,2017,ahs_energy)
saA17, saB17, saC17, saD17, saE17, saF17, saG17 = average_energy(5,2017,ahs_energy)
sA17, sB17, sC17, sD17, sE17, sF17, sG17 = average_energy(6,2017,ahs_energy)


mA18, mB18, mC18, mD18, mE18, mF18, mG18 = average_energy(0,2018,ahs_energy)
tA18, tB18, tC18, tD18, tE18, tF18, tG18 = average_energy(1,2018,ahs_energy)
wA18, wB18, wC18, wD18, wE18, wF18, wG18 = average_energy(2,2018,ahs_energy)
thA18, thB18, thC18, thD18, thE18, thF18, thG18 = average_energy(3,2018,ahs_energy)
fA18, fB18, fC18, fD18, fE18, fF18, fG18 = average_energy(4,2018,ahs_energy)
saA18, saB18, saC18, saD18, saE18, saF18, saG18 = average_energy(5,2018,ahs_energy)
sA18, sB18, sC18, sD18, sE18, sF18, sG18 = average_energy(6,2018,ahs_energy)




ahs_average_energy2016 = pd.DataFrame({'Days': ['Monday 2016','Tuesday 2016','Wednesday 2016','Thursday 2016','Friday 2016','Saturday 2016','Sunday 2016'],'HS Main (kWh)': [mA16, tA16, wA16, thA16, fA16, saA16, sA16],'LV Plug Loads (DHB)':  [mB16, tB16, wB16, thB16, fB16, saB16, sB16],
                                   'HS DL Lighting (kWh)':  [mC16, tC16, wC16, thC16, fC16, saC16, sC16],
                                   'HS DG Gym (kWh)':  [mD16, tD16, wD16, thD16, fD16, saD16, sD16],
                                   'HS Kitchen Emergency (kWh)':  [mE16, tE16, wE16, thE16, fE16, saE16, sE16],
                                   'HS M1 Chillers (kWh)':  [mF16, tF16, wF16, thF16, fF16, saF16, sF16],
                                   'HS CC Collins Center (kWh)':  [mG16, tG16, wG16, thG16, fG16, saG16, sG16]
                                   })

ahs_average_energy2017 = pd.DataFrame({'Days': ['Monday 2017','Tuesday 2017','Wednesday 2017','Thursday 2017','Friday 2017','Saturday 2017','Sunday 2017'],
                                   'HS Main (kWh)': [mA17, tA17, wA17, thA17, fA17, saA17, sA17],
                                   'LV Plug Loads (DHB)':  [mB17, tB17, wB17, thB17, fB17, saB17, sB17],
                                   'HS DL Lighting (kWh)':  [mC17, tC17, wC17,thC17, fC17, saC17, sC17],
                                   'HS DG Gym (kWh)':  [mD17, tD17, wD17, thD17, fD17, saD17, sD17],
                                   'HS Kitchen Emergency (kWh)':  [mE17, tE17, wE17, thE17, fE17, saE17, sE17],
                                   'HS M1 Chillers (kWh)':  [mF17, tF17, wF17, thF17, fF17, saF17, sF17],
                                   'HS CC Collins Center (kWh)':  [mG17, tG17, wG17, thG17, fG17, saG17, sG17]
                                   })

ahs_average_energy2018 = pd.DataFrame({'Days': ['Monday 2018','Tuesday 2018','Wednesday 2018','Thursday 2018','Friday 2018','Saturday 2018','Sunday 2018'],
                                       'HS Main (kWh)': [mA18, tA18, wA18, thA18, fA18, saA18, sA18],
                                   'LV Plug Loads (DHB)':  [mB18, tB18, wB18, thB18, fB18, saB18, sB18],
                                   'HS DL Lighting (kWh)':  [mC18, tC18, wC18,thC18, fC18, saC18, sC18],
                                   'HS DG Gym (kWh)':  [mD18, tD18, wD18, thD18, fD18, saD18, sD18],
                                   'HS Kitchen Emergency (kWh)':  [mE18, tE18, wE18, thE18, fE18, saE18, sE18],
                                   'HS M1 Chillers (kWh)':  [mF18, tF18, wF18, thF18, fF18, saF18, sF18],
                                   'HS CC Collins Center (kWh)':  [mG18, tG18, wG18, thG18, fG18, saG18, sG18]
                                   })

data = [ahs_average_energy2016, ahs_average_energy2017, ahs_average_energy2018]
ahs_energy_data= pd.concat(data)


#ahs_energy_csv.write("Electricity used by AHS between 23:00 hrs and 4:00 hrs\n\n")
ahs_energy_data.to_csv("averageEnergy.csv", sep=',', index_label="Electricity used by AHS between 23:00 hrs and 4:00 hrs")
#ahs_energy_csv.close()




