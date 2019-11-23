import numpy as np
from os import path
import sys
import os
import re
import matplotlib.pyplot as plt

"""
This script is used to plot the time and win for each iteration.
Need an input file to analyze.
"""
FILE="./20_6Othello"
assert(os.path.isdir(FILE))
AVERAGETIME = FILE + "/20_6Average_time.png"
FRACTIONWIN = FILE + "/20_6Fraction_win.png"
TRAINTIME = FILE + "/20_6Train_time.png"

# File names
if len(sys.argv) < 2:
    print("Need input a file")
    sys.exit()
filename = sys.argv[1]
assert(os.path.isfile(filename))

# Plot for average time and win for each nn vs players
f = open(filename, 'r')
data = {}
iteration = ""
player = ""
for line in f.readlines():
    # read the lines
    if "Iteration" in line:
        iteration = line[:-1]
        data[iteration] = {}
    elif "Random" in line:
        player = 'random'
        data[iteration][player] = {}
        data[iteration][player]['time'] = []
    elif "Greedy" in line:
        player = 'greedy'
        data[iteration][player] = {}
        data[iteration][player]['time'] = []
    elif "time" in line:
        time_used = float(re.findall(r"[-+]?\d*\.\d+|\d+", line)[0])
        data[iteration][player]['time'].append(time_used)
    elif "(" in line:
        data[iteration][player]['win'] = int(re.findall(r"[-+]?\d*\.\d+|\d+", line)[0])/100
        data[iteration][player]['lose'] = int(re.findall(r"[-+]?\d*\.\d+|\d+", line)[1])/100
        data[iteration][player]['draw'] = int(re.findall(r"[-+]?\d*\.\d+|\d+", line)[2])/100
total_game = data[iteration][player]['win'] + data[iteration][player]['lose'] + data[iteration][player]['draw']


# Deal with data
random_t = []
random_w = []
greedy_t = []
greedy_w = []
for it, v in data.items():
    # Random player
    times = v['random']['time']
    random_t.append(sum(times)/len(times))
    random_w.append(v['random']['win'])
    
    # Greedy player
    times = v['greedy']['time']
    greedy_t.append(sum(times)/len(times))
    greedy_w.append(v['greedy']['win'])

# plot
plt.plot(random_t, "g", greedy_t, "r")
plt.xticks(np.arange(0,len(data)+1,5))
plt.legend(labels = ['random', 'greedy'])
plt.xlabel('Iteration')
plt.ylabel('Average time')
plt.title('Average time used for each iteration\nMCTS vs. random/greedy player')

plt.savefig(AVERAGETIME, dpi=300)

plt.show()

plt.plot(random_w, "g", greedy_w, "r")
plt.xticks(np.arange(0,len(data)+1,5))
plt.yticks(np.arange(0.4, 1.01, 0.1))
plt.legend(labels = ['random', 'greedy'])
plt.xlabel('Iteration')
plt.ylabel('Fraction of win')
plt.title('Fraction of win for each iteration\nMCTS vs. random/greedy player')

plt.savefig(FRACTIONWIN, dpi=300)

plt.show()

# plot time used for train
if len(sys.argv) < 3:
    sys.exit()
filename = sys.argv[2]
assert(os.path.isfile(filename))

f = open(filename, 'r')
train_time = []
for line in f.readlines():
    if "Total:" in line:
        time = float(re.findall(r"[-+]?\d*\.\d+|\d+", line)[0])/60
        train_time.append(time)

plt.plot(train_time, "g")
plt.xticks(np.arange(0, len(train_time),5),np.arange(1, len(train_time)+1,5))
plt.xlabel('Iteration')
plt.ylabel('Time(min)')
plt.title('Train time for each iteration')

plt.savefig(TRAINTIME, dpi=300)

plt.show()