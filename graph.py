import matplotlib.pyplot as plt
import numpy as np
import parse

vals = parse.getTotals()

# Data for the bar chart
entities = []
wins = []
losses = []

for val in vals.values():
    entities.append(parse.namingDictionary[val[3]])
    wins.append(val[0])
    losses.append(val[1])
    print(f"{parse.namingDictionary[val[3]]}: {val}\n")

# X-axis positions for each group
x = np.arange(len(entities))

# Width of the bars
bar_width = 0.35

# Create the bar plots
plt.bar(x - bar_width/2, wins, width=bar_width, label='Wins', color='green')
plt.bar(x + bar_width/2, losses, width=bar_width, label='Losses', color='red')

# Add labels and title
plt.xlabel('Teams')
plt.ylabel('Count')
plt.title('W/L Ratio for NMU Sports 2002-2024')
plt.xticks(x, entities)  # Labeling the x-axis with team names
plt.xticks(rotation=30)  # Rotates labels to 45 degrees


# Add a legend
plt.legend()

# Display the plot
plt.show()
