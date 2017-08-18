import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import os.path
import sys
import json

config = None

if not os.path.isfile(os.path.expanduser('~/.config/battd/config.json')):
    print("Configuration file does not exist. Have you run battd?")
    sys.exit(1)
else:
    with open(os.path.expanduser('~/.config/battd/config.json'), 'r') as f:
        config = json.loads(f.read())

with open(os.path.expanduser(config["log_path"])) as f:
    batt_lines = [x.strip().split(' ') for x in f]

if len(batt_lines) == 0:
    print("No entries in battery log, exiting.")
    sys.exit(1)

times_origin = int(batt_lines[0][0])

sampling_rate = 60
time_scale = 1 / 3600

times = [(int(x[0]) - times_origin) * time_scale for x in batt_lines]
charge_nows = [int(x[1]) for x in batt_lines]
charge_fulls = [int(x[2]) for x in batt_lines]
statuses = [x[3] for x in batt_lines]
percentages = [(int(x[1]) / int(x[2]) * 100) for x in batt_lines]
deltaqs = [0 if i == 0 else percentages[i] - percentages[i - 1] for i in range(0, len(percentages))]
if len(batt_lines) > 1:
    deltaq_last = (percentages[-1] - percentages[-2])
else:
    deltaq_last = 0

percentages_predict = []
times_predict = []
t = times[-1]
q = percentages[-1]
for x in range(10):
    percentages_predict.append(q)
    q += deltaq_last
    times_predict.append(t)
    t +=  sampling_rate * time_scale

fig, (ax, ay) = plt.subplots(2, sharex=True)

ax.plot(times + times_predict, percentages + percentages_predict)
ax.fill_between(times, percentages, facecolor = 'g')
ax.fill_between(times_predict, percentages_predict, facecolor = 'c')
ax.set_yticks([x * 5 for x in range(1, 20)])
ax.set_ylabel("Charge (%)")
ax.axis([0, t - sampling_rate * time_scale, 0, 100])

ay.plot(times, deltaqs)
ay.set_ylabel("Change in charge per unit of time (%/t)")

plt.xlabel("Time (h)")

plt.show()