import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)), viewers, color='blue')
plt.title('Featured Games Viewers')
plt.xlabel('Games')
plt.ylabel('Viewers')
ax1 = plt.subplot()
ax1.set_xticks(range(len(games)))
ax1.set_xticklabels(games, rotation = 45)
plt.legend(['Twitch'])
plt.show()
plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, colors=colors, explode=explode,  shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
#plt.axis('equal')
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc='right')
plt.show()
plt.clf()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

y_upper = [1.15*x for x in viewers_hour]
y_lower = [0.85*x for x in viewers_hour]

plt.plot(hour, viewers_hour)
plt.title('Time Series')
plt.xlabel('Hour')
plt.ylabel('Viewers')
ax2 = plt.subplot()
ax2.set_xticks(range(len(hour)))
ax2.set_xticklabels(hour)
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)
plt.legend(['2015-01-01'])
plt.show()
