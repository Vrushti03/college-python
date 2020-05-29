import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from random import randint

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

points = []
last = 0
bound = 100
for i in range(0, 100):
  last += randint(-bound, bound)
  points.append(last)
  
ax.plot(points)
fig.savefig('graph.png')