from pathlib import Path

import matplotlib.pyplot as plt

import csv

from datetime import datetime

path = Path('data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(reader)
#Extract Dates, High and low Temperatures.
dates,highs,lows = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[2],"%Y-%m-%d")
    high = int(row[4])
    low=int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

#plot high and low temperatures
plt.style.use('seaborn-v0_8')
fix,ax = plt.subplots()
ax.plot(dates,highs,color='red',linewidth=1,alpha=0.5)
ax.plot(dates,lows,color='green',linewidth=1,alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#Format Plot
ax.set_title("Daily High and Low Temperatures, 2021",fontsize=24)
ax.set_xlabel('',fontsize=16)
fix.autofmt_xdate()
ax.set_ylabel("Teperature (F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.show()