# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
	for filename in filenames:
    	 print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mlb
sns.set(color_codes = True)
df = pd.read_csv ('/kaggle/input/csvfile/CSV-bhu-key-indicators-2023.csv')
df.head
df.tail()
df.info()
ind = df.iloc[[2,3,4]]
ind
p = ind.transpose()
ind_converted = p.rename(columns = {2:"population density", 3:"population (%annual change)", 4:'urban population' })
ind_converted
ind_converted1= ind_converted.drop(ind_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,13]])
ind_converted1
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
population_density = [19, 19, 20, 20, 19, 19, 19, 20, 20, 20]
population_growth_rate = [1.7, 1.7, 1.6, 1.5, 1.3, 1, 1, 0.9, 1, 0.9]
urban_population = [37.2, 38.1, 38.9, 39.4, 37.8, 40.9, 40.9, 42.3, 43, 40.9]

# Plotting
plt.figure(figsize=(10, 6))

# Plot population density
plt.plot(years, population_density, label='Population Density', marker='o')

# Plot population growth rate
plt.plot(years, population_growth_rate, label='Population Growth Rate (%)', marker='o')

# Plot urban population
plt.plot(years, urban_population, label='Urban Population', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Population Metrics Over Time')

# Change the legend location
plt.legend(loc='upper right')

# Increase the scale of the graph
plt.xlim(2013, 2022)  # Set the x-axis limits
plt.ylim(0, 100)  # Set the y-axis limits

# Display the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Bhutan has progressed in terms of key development indicators over the past decade based on the analysis from the population data.
#from population trends from 2013 to 2022 , the data shows that the population density remained relatively stable around 19-20 over the years. This could indicate that there hasn't been a significant increase in population concentration within the area under consideration.
 
#In terms of population growth rate (%annual change) has generally decreased over time 1.7% to 0.9%. This decline in population may reflect factors such as decrease in birth rate, aging population.

#However, in the case of urban population growth , it has shown a steady increase , reaching 40.9% to 43% of the total population by the end of the data period. A rising urban population suggests ongoing urbanization and migration trends toward urban centers, which could be driven by economic opportunities, better infrastructure , and services available in urban areas.

#higher urban population percentage can be associated with increased economic activities, services, and market opportunities. it also indicates that the most of of the people are educated and are hoping for better living standard which leads tio increase in urban population.

indicator = df.iloc[[165,166]]
indicator.head(3)

p = indicator.transpose()
indicator_converted = p.rename(columns = {165:"GDP per capita", 166:"GNI per capita"})
indicator_converted1= indicator_converted.drop(indicator_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
indicator_converted1
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
gdp_per_capita = [137583.60, 146935.80, 164157.00, 179080.50, 199661.00, 216941.10, 227867.50, 240755.70, 230054.90, 248334.30]
gni_per_capita = [126606.70, 136608.50, 152537.40, 166319.30, 182507.30, 198099.00, 207362.20, 218960.50, 215920.80, 233114.90]

# Set the width of each bar
bar_width = 0.35

# Set the position of each bar on the x-axis
r1 = range(len(years))
r2 = [x + bar_width for x in r1]

# Plotting
plt.figure(figsize=(10, 6))

plt.bar(r1, gdp_per_capita, color='blue', width=bar_width, edgecolor='grey', label='GDP per Capita')
plt.bar(r2, gni_per_capita, color='orange', width=bar_width, edgecolor='grey', label='GNI per Capita')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('GDP and GNI per Capita Over Time')
plt.xticks([r + bar_width/2 for r in range(len(years))], years)
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()

#Bhutan's  GDP per capita and GNI per capita show a consistent upward trend from 2012 to 2021, as seen in the increasing height of the bars.this steady growth suggest overall economic progress and an increase in the average income of individual within the country over the years.additionally to the rate of growth in both GDP per capita and GNI per capita appears to be moderate but steady, indicating a gradual improvement in the average income of bhutaneses individuals.
#yearly growth
# Create the DataFrame
data = {
	'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
	'Per capita GDP': [32044.90, 36111.50, 41448.00, 45469.80, 49346.70, 55348.20, 61286.50, 73316.90, 79596.80, 87404.50, 104848.10, 121357.50, 137583.60, 146935.80, 164157.00, 179080.50, 199661.00, 216941.10, 227867.50, 240755.70, 230054.90, 248334.30],
	'Per capita GNI': [32007.50, 36092.90, 40808.00, 44432.00, 48192.20, 54544.80, 61037.20, 72243.70, 77391.60, 83822.40, 98889.40, 113578.90, 126606.70, 136608.50, 152537.40, 166319.30, 182507.30, 198099.00, 207362.20, 218960.50, 215920.80, 233114.90]
}

df = pd.DataFrame(data)

# Calculate yearly growth rates
df['GDP Growth Rate (%)'] = df['Per capita GDP'].pct_change() * 100
df['GNI Growth Rate (%)'] = df['Per capita GNI'].pct_change() * 100

# Plotting
plt.figure(figsize=(10, 6))

# Plot GDP growth rate
plt.plot(df['Year'][1:], df['GDP Growth Rate (%)'][1:], label='GDP Growth Rate (%)', marker='o')

# Plot GNI growth rate
plt.plot(df['Year'][1:], df['GNI Growth Rate (%)'][1:], label='GNI Growth Rate (%)', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.title('Yearly Growth Rate of Per Capita GDP and GNI')
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#The trend of growth rate in both GDP and GNI growth rates show fluctuation over the years, with varying levels of increase or decrease. The growth rates can be positive or negative, indicating a period of economic expansion or contraction.
#period of economic expansion, years with high positive growth rate represent periods of economic expansion and increasing prosperity, suggesting strong economic performance. for example, the peak growth rate in the mid-2000s and around 2010 indicate significant economic growth during those periods.
#impact in economic events , negative growth rates or lower growth rates in certain years may be influenced by external economic events such as global recessions, economic policy change,or fluctuations in key economic sectors.

electricity = df.iloc[[181,182,180]]
electricity

elec = electricity.transpose()
elec
elec_converted = elec.rename(columns = {181:'imports',182:'consumption',180:'Export'})
elec_converted1= elec_converted.drop(elec_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
elec_converted1


# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
imports = [59.4, 112.3, 159.2, 124.5, 86.5, 91.9, 134, 96.4, 81.8, 98]
consumption = [1739.00, 2061.40, 2004.80, 2057.10, 2008.90, 2185.80, 2328.40, 2280.60, 1960.50, 2717.80]
exports = [4895.70, 5557.60, 5301.30, 5503.10, 5763.10, 5701.00, 4558.10, 6146.60, 9175.90, 8075.50]

# Plotting
plt.figure(figsize=(10, 6))

# Plot Imports
plt.plot(years, imports, label='Imports', marker='o')

# Plot Consumption
plt.plot(years, consumption, label='Consumption', marker='o')

# Plot Exports
plt.plot(years, exports, label='Exports', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Imports, Consumption, and Exports Over Time')

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(years)  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

#As the most important key for economic development, electricity has been playing the most significant role in economic growth.
#where  exporting electricity is being exported for country revenue compared to other key driving forces.
exte = df.iloc[[285,286]]
exte = exte.transpose()
exte_converted = exte.rename(columns = {285:'Export',286:'Import'})
df.index.name = 'external trade'
exte_converted
exte_converted1= exte_converted.drop(exte_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
exte_converted1



# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
exports = [2.8, -3.4, 9.8, 9.4, -9.1, 12.7, 6.4, 9.5, 9.1, 13.3]
imports = [-0.2, -0.5, 12.7, 9.8, 9.4, -0.7, -2.3, 7.3, -2.4, -5.8]

# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size

# Plot Exports
plt.plot(years, exports, label='Exports', marker='o')

# Plot Imports
plt.plot(years, imports, label='Imports', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Percentage Growth (%)')
plt.title('External Trade: Exports and Imports Over Time')

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(years)  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

#there is notable variability in the growth rates of export tares over the years , in 2021 there was a positive growth rate of 2.8%, indicating an increase in export compared to the previous year. however ,in 2013, there  was negative growth rate of -3.4%, representing a decline in export. therefore importing from the external trade has been playing negative role in the economic growth.
inds = df.iloc[[169,59,60]]
inds
inds = inds.transpose()
inds_converted = inds.rename(columns = {169:'agri',59:'indusrty',60:"services"})
df.index.name = 'industry contribution'
inds_converted
inds_converted1= inds_converted.drop(inds_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
inds_converted1

import matplotlib.pyplot as plt

# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
agriculture = [91.9, 89.3, 93.4, 96.2, 110.5, 109.8, 95.2, 102.2, 111, 99.4]
industry = [42.6, 43.4, 41.7, 42.5, 42.6, 41.8, 38.2, 36.1, 34.7, 34.2]
services = [43.4, 42.5, 43.8, 43.1, 43.1, 43.1, 45.8, 48.2, 46.1, 46.6]

# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size

# Plot Agriculture
plt.plot(years, agriculture, label='Agriculture', marker='o')


# Plot Industry
plt.plot(years, industry, label='Industry', marker='o')

# Plot Services
plt.plot(years, services, label='Services', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Contribution (%)')
plt.title('Industry Contribution Over Time')

# Add legend
plt.legend()

# Set x-axis and y-axis scales
plt.xlim(2011, 2022)  # Set the lower and upper bounds for the x-axis
plt.ylim(0, 120)  # Set the lower and upper bounds for the y-axis

# Display the plot with smaller grid
plt.grid(True, linewidth=0.5, alpha=0.5)  # Set smaller grid lines
plt.xticks(range(2012, 2022))  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
#Agriculture's contribution shows fluctuation over the years, with a peak in 2016 followed by a decline , overall, it maintains a significant share but exhibits variability.it started at a high level around 90% in 2012,drops slightly in the following years, experiences a significant increase in 2016.It indicates that agriculture has been a consistent major contributor to the economy.
#Industry contribution shows a decreasing trend over the years, starting around 42% in 2012 and gradually declines to around  34% by 2021.. this trend suggests the growing importance of the services sector in the economy , which could be due to factors.
#services contribution shows a mixed pattern, with some fluctuations but generally increasing over time , it started around 43% in 2012, experiences fluctuation in the middle years, and then rises to around 46% by 2021. this trend suggest the growing importance of the services in the economy .
expen = df.iloc[[234, 241,360,281]]
expen
expen = expen.transpose()
expen_converted = expen.rename(columns = {234:'total revenue', 241:'total expenditure',360:'total debt',281:'trade balance'})
df.index.name = 'Fisical sustanibality'
expen_converted
expen_converted1= expen_converted.drop(expen_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
expen_converted1

 

# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
total_revenue = [20144.80, 21093.50, 23582.80, 26276.00, 27149.70, 29686.40, 37266.00, 31516.80, 38178.10, 44813.80]
total_expenditure = [34843.10, 36527.80, 34609.90, 36475.80, 44688.40, 49966.60, 56331.40, 44053.70, 57572.30, 71091.80]
total_debt = [1449.60, 1528.20, 1841.20, 2011.10, 2289.70, 2608.00, 2552.00, 2703.80, 3036.80, 3069.40]
trade_balance = [50878.10, 50640.00, 57047.10, 62645.00, 68533.20, 68021.20, 66432.40, 71290.20, 69589.20, 65529.40]

# Plotting
plt.figure(figsize=(12, 8))  # Set the figure size

# Plot Total Revenue
plt.plot(years, total_revenue, label='Total Revenue', marker='o')

# Plot Total Expenditure
plt.plot(years, total_expenditure, label='Total Expenditure', marker='o')

# Plot Total Debt
plt.plot(years, total_debt, label='Total Debt', marker='o')

# Plot Trade Balance
plt.plot(years, trade_balance, label='Trade Balance', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Fiscal Sustainability Analysis (2012-2021)')
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(years)  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
	for filename in filenames:
    	 print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mlb
sns.set(color_codes = True)
df = pd.read_csv ('/kaggle/input/csvfile/CSV-bhu-key-indicators-2023.csv')
df.head
df.tail()
df.info()
ind = df.iloc[[2,3,4]]
ind
p = ind.transpose()
ind_converted = p.rename(columns = {2:"population density", 3:"population (%annual change)", 4:'urban population' })
ind_converted
ind_converted1= ind_converted.drop(ind_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,13]])
ind_converted1
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
population_density = [19, 19, 20, 20, 19, 19, 19, 20, 20, 20]
population_growth_rate = [1.7, 1.7, 1.6, 1.5, 1.3, 1, 1, 0.9, 1, 0.9]
urban_population = [37.2, 38.1, 38.9, 39.4, 37.8, 40.9, 40.9, 42.3, 43, 40.9]

# Plotting
plt.figure(figsize=(10, 6))

# Plot population density
plt.plot(years, population_density, label='Population Density', marker='o')

# Plot population growth rate
plt.plot(years, population_growth_rate, label='Population Growth Rate (%)', marker='o')

# Plot urban population
plt.plot(years, urban_population, label='Urban Population', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Population Metrics Over Time')

# Change the legend location
plt.legend(loc='upper right')

# Increase the scale of the graph
plt.xlim(2013, 2022)  # Set the x-axis limits
plt.ylim(0, 100)  # Set the y-axis limits

# Display the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Bhutan has progressed in terms of key development indicators over the past decade based on the analysis from the population data.
#from population trends from 2013 to 2022 , the data shows that the population density remained relatively stable around 19-20 over the years. This could indicate that there hasn't been a significant increase in population concentration within the area under consideration.
 
#In terms of population growth rate (%annual change) has generally decreased over time 1.7% to 0.9%. This decline in population may reflect factors such as decrease in birth rate, aging population.

#However, in case of urban population growth , it has shown a steady increase , reaching 40.9% to 43% of the total population by the end of the data period. A rising urban population suggests ongoing urbanization and migration trends toward urban centers, which could be driven by economic opportunities, better infrastructure , and services available in urban areas.

#higher urban population percentage can be associated with increased economic activities, services, and market opportunities. It also indicates that most of the people are educated and are hoping for a better living standard which leads to an increase in urban population.

indicator = df.iloc[[165,166]]
indicator.head(3)

p = indicator.transpose()
indicator_converted = p.rename(columns = {165:"GDP per capita", 166:"GNI per capita"})
indicator_converted1= indicator_converted.drop(indicator_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
indicator_converted1
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
gdp_per_capita = [137583.60, 146935.80, 164157.00, 179080.50, 199661.00, 216941.10, 227867.50, 240755.70, 230054.90, 248334.30]
gni_per_capita = [126606.70, 136608.50, 152537.40, 166319.30, 182507.30, 198099.00, 207362.20, 218960.50, 215920.80, 233114.90]

# Set the width of each bar
bar_width = 0.35

# Set the position of each bar on the x-axis
r1 = range(len(years))
r2 = [x + bar_width for x in r1]

# Plotting
plt.figure(figsize=(10, 6))

plt.bar(r1, gdp_per_capita, color='blue', width=bar_width, edgecolor='grey', label='GDP per Capita')
plt.bar(r2, gni_per_capita, color='orange', width=bar_width, edgecolor='grey', label='GNI per Capita')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('GDP and GNI per Capita Over Time')
plt.xticks([r + bar_width/2 for r in range(len(years))], years)
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()

#Bhutan's  GDP per capita and GNI per capita show a consistent upward trend from 2012 to 2021, as seen in the increasing hight of the bars.this steady growth suggest overall economic progress and an increase in the average income of individual within the country over the years.addationaly to the rate of growth in both GDP per capita and GNI per capita apperas to be modreate but steady, indicating a gradual improvement in the average income of bhutaneses indivbiduals.
#yearly growth
# Create the DataFrame
data = {
	'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
	'Per capita GDP': [32044.90, 36111.50, 41448.00, 45469.80, 49346.70, 55348.20, 61286.50, 73316.90, 79596.80, 87404.50, 104848.10, 121357.50, 137583.60, 146935.80, 164157.00, 179080.50, 199661.00, 216941.10, 227867.50, 240755.70, 230054.90, 248334.30],
	'Per capita GNI': [32007.50, 36092.90, 40808.00, 44432.00, 48192.20, 54544.80, 61037.20, 72243.70, 77391.60, 83822.40, 98889.40, 113578.90, 126606.70, 136608.50, 152537.40, 166319.30, 182507.30, 198099.00, 207362.20, 218960.50, 215920.80, 233114.90]
}

df = pd.DataFrame(data)

# Calculate yearly growth rates
df['GDP Growth Rate (%)'] = df['Per capita GDP'].pct_change() * 100
df['GNI Growth Rate (%)'] = df['Per capita GNI'].pct_change() * 100

# Plotting
plt.figure(figsize=(10, 6))

# Plot GDP growth rate
plt.plot(df['Year'][1:], df['GDP Growth Rate (%)'][1:], label='GDP Growth Rate (%)', marker='o')

# Plot GNI growth rate
plt.plot(df['Year'][1:], df['GNI Growth Rate (%)'][1:], label='GNI Growth Rate (%)', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.title('Yearly Growth Rate of Per Capita GDP and GNI')
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#The trend of growth rate in both GDP and GNI growth rates show fluctuation over the years, with varying levels of increase or decrease. The growth rates can be positive or negative, indicating a period of economic expansion or contraction.
#period of economic expansion, years with high positive growth rate represent [period of economic expansion and increasing prosperity, suggesting strong economic performance. for example, the peak growth rate in the mid-2000s and around 2010 indicate significant economic growth during those periods.
#impact in economic events , negative growth rates or lower growth rates in certain years may be influenced by external economic events such as global recessions, economic policy change,or fluctuations in key economic sectors.

electricity = df.iloc[[181,182,180]]
electricity

elec = electricity.transpose()
elec
elec_converted = elec.rename(columns = {181:'imports',182:'consumption',180:'Export'})
elec_converted1= elec_converted.drop(elec_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
elec_converted1


# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
imports = [59.4, 112.3, 159.2, 124.5, 86.5, 91.9, 134, 96.4, 81.8, 98]
consumption = [1739.00, 2061.40, 2004.80, 2057.10, 2008.90, 2185.80, 2328.40, 2280.60, 1960.50, 2717.80]
exports = [4895.70, 5557.60, 5301.30, 5503.10, 5763.10, 5701.00, 4558.10, 6146.60, 9175.90, 8075.50]

# Plotting
plt.figure(figsize=(10, 6))

# Plot Imports
plt.plot(years, imports, label='Imports', marker='o')

# Plot Consumption
plt.plot(years, consumption, label='Consumption', marker='o')

# Plot Exports
plt.plot(years, exports, label='Exports', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Imports, Consumption, and Exports Over Time')

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(years)  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

#As the most important key for economic development, electricity has been playing the most significant role in economic growth.
#where  exporting electricity is being exporting for country revenue compared to other key driving force.
exte = df.iloc[[285,286]]
exte = exte.transpose()
exte_converted = exte.rename(columns = {285:'Export',286:'Import'})
df.index.name = 'external trade'
exte_converted
exte_converted1= exte_converted.drop(exte_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
exte_converted1



# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
exports = [2.8, -3.4, 9.8, 9.4, -9.1, 12.7, 6.4, 9.5, 9.1, 13.3]
imports = [-0.2, -0.5, 12.7, 9.8, 9.4, -0.7, -2.3, 7.3, -2.4, -5.8]

# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size

# Plot Exports
plt.plot(years, exports, label='Exports', marker='o')

# Plot Imports
plt.plot(years, imports, label='Imports', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Percentage Growth (%)')
plt.title('External Trade: Exports and Imports Over Time')

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(years)  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

#There is notable variability in the growth rates of export tares over the years , in 2021 there was a positive growth rate of 2.8%, indicating an increase in export compared to the previous year. However ,in 2013, there  was a negative growth rate of -3.4%, representing a decline in exports. Therefore importing from external trade has been playing a negative role in the economic growth.
inds = df.iloc[[169,59,60]]
inds
inds = inds.transpose()
inds_converted = inds.rename(columns = {169:'agri',59:'industry',60:"services"})
df.index.name = 'industry contribution'
inds_converted
inds_converted1= inds_converted.drop(inds_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
inds_converted1

import matplotlib.pyplot as plt

# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
agriculture = [91.9, 89.3, 93.4, 96.2, 110.5, 109.8, 95.2, 102.2, 111, 99.4]
industry = [42.6, 43.4, 41.7, 42.5, 42.6, 41.8, 38.2, 36.1, 34.7, 34.2]
services = [43.4, 42.5, 43.8, 43.1, 43.1, 43.1, 45.8, 48.2, 46.1, 46.6]

# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size

# Plot Agriculture
plt.plot(years, agriculture, label='Agriculture', marker='o')


# Plot Industry
plt.plot(years, industry, label='Industry', marker='o')

# Plot Services
plt.plot(years, services, label='Services', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Contribution (%)')
plt.title('Industry Contribution Over Time')

# Add legend
plt.legend()

# Set x-axis and y-axis scales
plt.xlim(2011, 2022)  # Set the lower and upper bounds for the x-axis
plt.ylim(0, 120)  # Set the lower and upper bounds for the y-axis

# Display the plot with smaller grid
plt.grid(True, linewidth=0.5, alpha=0.5)  # Set smaller grid lines
plt.xticks(range(2012, 2022))  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
#Agriculture's contribution shows fluctuation over the years, with a peak 2016 followed by a decline , overall, it maintains a significant share but exhibits variability.it started at a high level around 90% in 2012,drops slightly in the following years, experiences a significant increase in 2016.It indicates that agriculture has been a consistent major contributor to the economy.
#Industry contribution shows a decreasing trend over the years, starting around 42% in 2012 and gradually declines to around  34% by 2021.. this trend suggests the growing importance of the services sector in the economy , which could be due to factors.
#services contribution shows a mixed pattern, with some fluctuations but generally increasing over time , it started around 43% in 2012, experienced fluctuation in the middle years, and then rose to around 46% by 2021. This trend suggests the growing importance of the services in the economy .
expen = df.iloc[[234, 241,360,281]]
expen
expen = expen.transpose()
expen_converted = expen.rename(columns = {234:'total revenue', 241:'total expenditure',360:'total debt',281:'trade balance'})
df.index.name = 'Fiscal sustainability'
expen_converted
expen_converted1= expen_converted.drop(expen_converted.index[[0,1,2,3,4,5,6,7,8,9,10,11,12,23]])
expen_converted1

 

# Given data
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
total_revenue = [20144.80, 21093.50, 23582.80, 26276.00, 27149.70, 29686.40, 37266.00, 31516.80, 38178.10, 44813.80]
total_expenditure = [34843.10, 36527.80, 34609.90, 36475.80, 44688.40, 49966.60, 56331.40, 44053.70, 57572.30, 71091.80]
total_debt = [1449.60, 1528.20, 1841.20, 2011.10, 2289.70, 2608.00, 2552.00, 2703.80, 3036.80, 3069.40]
trade_balance = [50878.10, 50640.00, 57047.10, 62645.00, 68533.20, 68021.20, 66432.40, 71290.20, 69589.20, 65529.40]

# Plotting
plt.figure(figsize=(12, 8))  # Set the figure size

# Plot Total Revenue
plt.plot(years, total_revenue, label='Total Revenue', marker='o')

# Plot Total Expenditure
plt.plot(years, total_expenditure, label='Total Expenditure', marker='o')

# Plot Total Debt
plt.plot(years, total_debt, label='Total Debt', marker='o')

# Plot Trade Balance
plt.plot(years, trade_balance, label='Trade Balance', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Fiscal Sustainability Analysis (2012-2021)')
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(years)  # Set x-axis ticks to be the years
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


