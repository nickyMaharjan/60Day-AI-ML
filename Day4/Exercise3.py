from scipy.datasets import face, ascent

import scipy
import matplotlib.pyplot as plt
from numpy import linalg

img = ascent()

print(scipy.__version__)

print(dir(scipy.datasets))

print(type(img))

plt.imshow(img)
plt.show()

# print(img[:,:,0])
#
# img_array = img / 255
# red_array = img_array[:, :, 0]
# green_array = img_array[:, :, 1]
# blue_array = img_array[:, :, 2]
#
# img_gray = img_array @ [0.2126, 0.7152, 0.0722]

# print(img_gray.shape)
#
# plt.imshow(img_gray, cmap="gray")
# plt.show()

print(dir(scipy))