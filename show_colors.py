import matplotlib.pyplot as plt
from myterials.lookup import colors


f, axarr = plt.subplots(ncols=5, nrows=20, figsize=(10, 20))
axarr = axarr.flatten()

for ax, (name, hex) in zip(axarr, colors.items()):
    ax.scatter(0, 0, color=hex, lw=1, edgecolors='k', s=2000)
    ax.set(title=name)

for ax in axarr:
    ax.axis('off')

f.tight_layout()
plt.show()
