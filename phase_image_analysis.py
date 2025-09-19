import cv2
from matplotlib import pyplot as plt

phase_image = cv2.imread('PHA Versuch6_375nm_35mW_15s 17_09_25 15h31m42s879ms.tif', -1)

fig, ax = plt.subplots()
plt.imshow(phase_image, cmap='hot_r', interpolation='nearest')
plt.colorbar(label='Phase (nm)')
plt.xlabel('image width in px')
plt.ylabel('image height in px')
plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.xaxis.set_label_position('top')
plt.show()
