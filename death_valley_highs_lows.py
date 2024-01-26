from pathlib import Path

import matplotlib.pyplot as plt

from datetime import datetime

import csv

path=Path('data/death_valley_2021_simple.csv')
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)
    
dates , highs , lows=[],[],[]
for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high=int(row[3])
        low=int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
        
#plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fix,ax=plt.subplots()
ax.plot(dates,highs,color='red',linewidth=1,alpha=0.5)
ax.plot(dates,lows,color='green',linewidth=1,alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#styling plot
ax.set_title('Daily High and Low Temperatures, 2021\nDeath Valley, CA',fontsize=20)
ax.set_xlabel("",fontsize=10)
ax.set_ylabel("Temperature (F)",fontsize=10)
fix.autofmt_xdate()
ax.tick_params(labelsize=10)

plt.show()