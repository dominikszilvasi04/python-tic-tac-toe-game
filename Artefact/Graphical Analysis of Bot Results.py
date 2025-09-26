import matplotlib.pyplot as plt
import csv

botfile = open("Bot_Results.csv", "r")
data_bot = list(csv.reader(botfile))
botfile.close()

datalistbot = []

for i in data_bot:
    for x in i:
        datalistbot.append(int(x))

bot1 = datalistbot.count(1)
bot2 = datalistbot.count(2)
totalbot = []
totalbot.append(bot1)
totalbot.append(bot2)

Pie = ["Bot 1 Wins","Bot 2 Wins"]
plt.pie(totalbot, labels=Pie)
plt.title("Bot 1 vs Bot 2")
plt.show()
