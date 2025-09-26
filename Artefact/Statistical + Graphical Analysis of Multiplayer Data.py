import statistics
import csv
import matplotlib.pyplot as plt


multiplayer_file = open("game_results(MULTIPLAYER).csv", "r")
multi_list = list(csv.reader(multiplayer_file))
multiplayer_file.close()


multi_list_float = []
for i in multi_list:
    for x in i:
        multi_list_float.append(float(x))
multi_list_float = sorted(multi_list_float)

print("The 'mean' average of the time taken for multiplayer games to finish is:", round(statistics.mean(multi_list_float), 2),"seconds")
print("The 'mode' average of the time taken for multiplayer games to finish is:", statistics.mode(multi_list_float),"seconds")
print("The 'median' average of the time taken for multiplayer games to finish is:", statistics.median(multi_list_float),"seconds")

nums = [round(statistics.mean(multi_list_float), 2), statistics.mode(multi_list_float), statistics.median(multi_list_float)]
averages = ["Mean", "Mode", "Median"]
plt.bar(averages, nums)
plt.title("Averages of Multiplayer Data (Time Taken)")
plt.xlabel("Names of Averages")
plt.ylabel("Time Taken")
plt.show()