import csv
from datetime import datetime
from matplotlib import pyplot as plt
file_name='death_valley_2014.csv'
with open(file_name) as f :
    redear=csv.reader(f)
    header_row=next(redear)
    highs,lows,dates=[],[],[]
    for row in redear:
      try:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        high=int(row[1])
        low=int(row[3])
      except ValueError :
        print(current_date,'missing data')
      else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

fig=plt.figure(dpi=124,figsize=(10,5))
plt.plot(dates,highs,c='green',alpha=0.6)
plt.plot(dates,lows,c='blue',alpha=0.6)
plt.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.1)
fig.autofmt_xdate()
title="Daily high and low temperatures-2014\nDeath valley"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()