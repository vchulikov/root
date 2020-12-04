import numpy as np
import matplotlib.pyplot as plt

npzfile = np.load("learning_info.npz")
train_arr = npzfile['tr']
accur_arr = npzfile['ac']

#PLOT_MATPLOTLIB
fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
fig.suptitle('Training Metrics')

axes[0].set_ylabel("Loss", fontsize=14)
axes[0].plot(train_arr)

axes[1].set_ylabel("Accuracy", fontsize=14)
axes[1].set_xlabel("Epoch", fontsize=14)
axes[1].plot(accur_arr)
plt.show()

