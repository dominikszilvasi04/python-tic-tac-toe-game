#Exam number: 111123
import statistics
import csv
import matplotlib.pyplot as plt

singleplayer_file = open("game_results(SINGLEPLAYER).csv", "r")
single_list = list(csv.reader(singleplayer_file))
singleplayer_file.close()


single_list_float = []
for i in single_list:
    for x in i:
        single_list_float.append(float(x))
single_list_float = sorted(single_list_float)

print("The 'mean' average of the time taken for single player games to finish is:", round(statistics.mean(single_list_float), 2),"seconds")
print("The 'mode' average of the time taken for single player games to finish is:", statistics.mode(single_list_float),"seconds")
print("The 'median' average of the time taken for single player games to finish is:", statistics.median(single_list_float),"seconds")


nums = [round(statistics.mean(single_list_float), 2), statistics.mode(single_list_float), statistics.median(single_list_float)]
averages = ["Mean", "Mode", "Median"]
plt.bar(averages, nums)
plt.title("Averages of Singleplayer Data (Time Taken)")
plt.xlabel("Names of Averages")
plt.ylabel("Time Taken")
plt.show()
