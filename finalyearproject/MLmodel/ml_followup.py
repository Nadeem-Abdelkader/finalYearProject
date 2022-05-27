# -*- coding: utf-8 -*-

# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour

# Upload image
image = open(filename, 'r')
read = plt.imread('brain2.jpg')
show = plt.imshow(read)

gray_brain = rgb2gray(read)
plt.imshow(gray_brain, cmap = plt.cm.gray)

# Applying Gaussian Filter to remove noise
gray_brain_noiseless = gaussian(gray_brain, 1)
 
# Localising the circle's center at 220, 110
x1 = 225 + 100*np.cos(np.linspace(0, 2*np.pi, 200))
x2 = 200 + 100*np.sin(np.linspace(0, 2*np.pi, 200))
 
# Generating a circle based on x1, x2
snake = np.array([x1, x2]).T
 
# Computing the Active Contour for the given image
brain_snake = active_contour(gray_brain_noiseless,
                                 snake)
 
fig = plt.figure(figsize=(10, 10))
 
# Adding subplots to display the markers
ax = fig.add_subplot(111)
 
# Plotting sample image
ax.imshow(gray_brain_noiseless, cmap = plt.cm.gray)
 
# Plotting the lesion boundary marker
ax.plot(brain_snake[:, 0],
        brain_snake[:, 1],
        '-b', lw=5)
 
# Plotting the circle around lesion feature
# ax.plot(snake[:, 0], snake[:, 1], '--r', lw=5)