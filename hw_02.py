import matplotlib.pyplot as plt

import csv
file = open('ELAtest.csv')
reader = csv.reader(file)
data = list(reader)

year = []
mean = []

# year
x1 = int(data[1][1])
year.append(x1)
x2 = int(data[2][1])
year.append(x2)
x3 = int(data[3][1])
year.append(x3)
x4 = int(data[4][1])
year.append(x4)
x5 = int(data[5][1])
year.append(x5)
x6 = int(data[6][1])
year.append(x6)

# mean score
y1 = int(data[1][4])
mean.append(y1)
y2 = int(data[2][4])
mean.append(y2)
y3 = int(data[3][4])
mean.append(y3)
y4 = int(data[4][4])
mean.append(y4)
y5 = int(data[5][4])
mean.append(y5)
y6 = int(data[6][4])
mean.append(y6)

#plotting graph 1
fig, ax = plt.subplots()
ax.plot(year, mean)
plt.xlabel('Year (2006-2011)', fontweight='bold')
plt.ylabel('Mean ELA test scores of Grade 3 students in NYC', fontweight='bold')
plt.legend()
plt.savefig('NYC grade 3 ELA test mean.jpg')
plt.show()


'''
Graph #2
'''

file = open('mathscore.csv')
reader = csv.reader(file)
data = list(reader)

ethn = []
means = []

#ethnicity
x1 = (data[41][2])
ethn.append(x1)
x2 = (data[83][2])
ethn.append(x2)
x3 = (data[125][2])
ethn.append(x3)
x4 = (data[167][2])
ethn.append(x4)

#mean score
y1 = int(data[41][4])
means.append(y1)
y2 = int(data[83][4])
means.append(y2)
y3 = int(data[125][4])
means.append(y3)
y4 = int(data[167][4])
means.append(y4)

#plotting graph 2
plt.bar(ethn, means, color = 'y', width = 0.6)
plt.xlabel('Ethnicity of Grade 8 students', fontweight='bold')
plt.ylabel('NYS math test mean scale scores', fontweight='bold')
plt.legend()
plt.savefig('NYC math scores by ethnicityjpg')
plt.show()