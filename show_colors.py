import matplotlib.pyplot as plt
from myterial.lookup import colors


f, axarr = plt.subplots(ncols=5, nrows=10, figsize=(10, 10))
axarr = axarr.flatten()

for ax, (name, hex) in zip(axarr, colors.items()):
    ax.scatter(0, 0, color=hex, lw=1, edgecolors='k', s=2000)
    ax.axis('off')
    ax.set(title=name)

f.tight_layout()
plt.show()
