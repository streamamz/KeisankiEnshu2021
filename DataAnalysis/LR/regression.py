#Sample code
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

#Number of years
nyear = 38

#Reading data
year,month,day,area = np.loadtxt("/Users/tozuka/ENSHU/REGRESSION/arctic_alldata.dat", comments='Y', unpack=True)
area2=area.reshape(nyear,72)
year2=year.reshape(nyear,72)
area2[area2 < 0.0] = None

#Annual mean
area2_yave = ma.empty(nyear)
year3 = ma.empty(nyear)
for k in range(nyear):
    area2_yave[k] = np.nanmean(area2[k,:],axis=0)
    year3[k]=year2[k,0]

#Regression analysis
a, b = np.polyfit(year3, area2_yave, 1)
print(a,b)
y = a * year3 + b

#Figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(year3, area2_yave, "o-", color='blue', label="Annual mean")
ax.plot(year3, y,color='black')
ax.text(2005,1240, 'y='+ str(round(a,2)) +'x+'+str(round(b,2)),fontsize=16)
ax.tick_params(axis='both', labelsize=16)
ax.set_xlabel("Year", fontsize=16)
ax.set_ylabel("Sea Ice Area (10$^4$ km$^2$)", fontsize=16)
ax.legend(loc="upper right")
plt.savefig("/Users/tozuka/Desktop/ts_area_arctic.png", dpi=150, bbox_inches='tight', pad_inches=0)
plt.show()

