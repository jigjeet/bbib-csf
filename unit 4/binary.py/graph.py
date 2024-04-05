import matplotlib.pyplot as plt

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