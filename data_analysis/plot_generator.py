# This script takes a InfluNet files and print on screen
# the ILI curve during the seasonal influenza period.
#
# Written by Giovanni De Toni (2017)
# Email: giovanni.det at gmail.com

import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Set the font's size and weight.
font = {
        'weight' : 'normal',
        'size'   : 14
        }

matplotlib.rc('font', **font)

# All possible colors
colors = ["b", "g", "r", "c", "m", "y", "k", "#5900b3", "#004d00", "#ff6600"]
weeks = ["42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]

def plot_data(_range, data, color_gv, label_name):
    plt.plot(_range, data, color=color_gv, linestyle="-", marker='.',  label=label_name)

plt.title("Stagioni influenzali")
plt.ylabel("Incidenza su 100000 persone")
plt.xlabel("Settimana")
plt.grid()

_range = range(0, len(weeks));

# For each file provided as command line arguments
# print its content on a plot.
for f in range(0, len(sys.argv)-1):
    _file = sys.argv[f+1]
    document = pd.read_csv(_file)
    labels = document["week"][0:len(weeks)]
    data = document["incidence"][0:len(weeks)]

    year = int(labels[1][0:4])

    if len(weeks) > len(data):
        plot_data(range(0, len(data)), data, colors[f], str(year)+"-"+str(year+1))
    else:
        plot_data(_range, data, colors[f], str(year)+"-"+str(year+1))

plt.legend()
plt.xticks(_range, weeks, rotation="vertical")
plt.subplots_adjust(bottom=0.15)
plt.show()
