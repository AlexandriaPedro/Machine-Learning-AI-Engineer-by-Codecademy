import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()

print(digits)
print(digits.DESCR)
print(digits.data)
print(digits.target)

plt.gray()
plt.matshow(digits.images[100])
plt.show()

print(digits.target[100])

model = KMeans(n_clusters = 10)
model.fit(digits.data)

fig = plt.figure(figsize = (8, 3))
fig.suptitle('Cluster Center Images', fontsize = 14, fontweight = 'bold')

print(digits.data)

for i in range(10):
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

new_samples = np.array(
[
[0.00,0.00,0.00,0.00,1.99,0.69,0.00,0.00,0.00,0.00,0.23,4.51,7.62,4.50,0.00,0.00,0.00,0.76,6.26,7.63,7.55,4.57,0.00,0.00,0.00,2.97,7.32,2.29,6.86,4.57,0.00,0.00,0.00,0.00,0.00,0.00,7.09,4.57,0.00,0.00,0.00,0.00,0.00,0.68,7.63,3.36,0.00,0.00,0.00,0.00,0.00,0.76,7.63,3.05,0.00,0.00,0.00,0.00,0.00,0.07,3.36,0.76,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.76,5.65,6.03,3.43,0.46,0.00,0.00,1.53,7.40,6.71,6.18,7.63,4.89,0.00,0.00,5.35,7.24,0.61,0.00,4.73,7.40,0.00,0.00,6.86,4.65,0.00,0.00,3.96,7.62,0.00,0.00,6.86,5.11,0.00,0.15,6.10,6.40,0.00,0.00,4.57,7.62,7.01,7.09,7.62,3.20,0.00,0.00,0.23,2.98,3.81,3.81,2.82,0.08,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.37,5.04,5.34,3.90,0.92,0.00,0.00,0.69,7.10,6.94,6.71,7.63,7.18,0.69,0.00,3.51,7.63,1.45,0.00,1.90,7.63,2.90,0.00,3.81,7.63,0.23,0.00,0.76,7.62,3.05,0.00,2.13,7.62,5.95,3.81,5.11,7.62,2.66,0.00,0.00,2.98,6.41,6.86,6.71,4.50,0.31,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.76,1.53,1.53,0.61,0.00,0.00,0.69,5.11,7.48,7.63,7.63,7.64,2.75,0.23,6.72,7.40,4.35,3.28,2.29,7.09,4.58,0.76,7.63,3.28,0.00,0.00,0.00,6.86,4.57,0.38,7.32,6.10,2.06,0.23,1.30,7.32,4.50,0.00,2.44,7.17,7.62,7.62,7.62,7.17,1.22,0.00,0.00,0.15,2.36,3.05,2.90,0.92,0.00]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')