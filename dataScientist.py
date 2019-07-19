import injuries
import matplotlib.pyplot as plt

list_of_report = injuries.get_reports()

#total number of injuries by business or industry
homeDepot = 0
lowes = 0
fedex = 0
ups = 0
target = 0
walmart = 0
pepsi = 0
coca=0
kmart=0

for item in list_of_report:
    #get business and industry name
    businessName = item['business']['name']
    industry = item['industry']['major_group']
    #if business or industry name is found, add to total
    if("home depot" in businessName.lower()):
        homeDepot+=1
    if("lowe" in businessName.lower()):
        lowes+=1
    if("fedex" in businessName.lower()):
        fedex+=1
    if("united parcel" in businessName.lower()):
        ups+=1
    if("wal-mart" in businessName.lower()):
        walmart+=1
    if("target" in businessName.lower()):
        target+=1
    if("kmart" in businessName.lower()):
        kmart+=1
    if("target" in businessName.lower()):
        target+=1
    if("pepsi" in businessName.lower()):
        pepsi+=1
    if("coca" in businessName.lower()):
        coca+=1

#bar graph
plt.style.use('ggplot')

labels = ['Home Depot', 'Lowes', 'Pepsi', 'Coca-Cola', 'Fedex', 'UPS', 'Target', 'Kmart', 'Wal-Mart']
businesses = [homeDepot, lowes, pepsi, coca, fedex, ups, target, kmart, walmart]

x_pos = [i for i, _ in enumerate(labels)]

plt.bar(x_pos, businesses, color='blue')
plt.xlabel("Business")
plt.ylabel("Injuries")
plt.title("Injuries by Business")

plt.xticks(x_pos, labels)

plt.show()

#horizontal bar graph
x_pos = [i for i, _ in enumerate(labels)]

plt.barh(x_pos, businesses, color='green')
plt.ylabel("Businesses")
plt.xlabel("Injuries")
plt.title("Injuries by Business")

plt.yticks(x_pos, labels)

plt.show()

#pie chart
sizes = [homeDepot, lowes, pepsi, coca, fedex, ups, target, kmart, walmart]
colors = ['yellow', 'green', 'black', 'blue', 'gray', 'pink', 'red', 'purple', 'darkblue']
plt.pie(sizes, l abels=labels, colors=colors, shadow=True, startangle=140)
plt.axis('equal')
plt.tight_layout()
plt.show()

#3D bar graph
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

xpos = [1,2,3,4,5,6,7,8,9]
ypos = [1,2,3,4,5,6,7,8,9]
num_elements = len(xpos)
zpos = np.zeros(9)
dx = np.ones(9)
dy = np.ones(9)
dz = businesses

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
ax1.set_zlabel('Injuries')
ax1.set_xlabel('Businesses')
ax1.set_ylabel('Businesses')

plt.show()
