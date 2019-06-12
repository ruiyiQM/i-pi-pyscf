import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot(i):  
  A = np.genfromtxt("TEST"+str(i))[:,2:]
  hist, bin_edges = np.histogram(A.flatten(), bins = np.arange(0.5,2.5,0.01),normed=True,density=True)
# seaborn histogram
#sns.distplot(A[:,1:].flatten(), hist=, kde=True, 
#             bins=60, color = 'blue',
#             hist_kws={'edgecolor':'black'})
# Add labels
  return hist
fig, ax = plt.subplots()
plt.plot(np.arange(0.5,2.5,0.01)[1:],plot(1),label='nbead=1')
plt.plot(np.arange(0.5,2.5,0.01)[1:],plot(4),label='nbead=4')
plt.plot(np.arange(0.5,2.5,0.01)[1:],plot(8),label='nbead=8')
plt.plot(np.arange(0.5,2.5,0.01)[1:],plot(16),label='nbead=16')
ax.get_yaxis().set_visible(False)
plt.legend()
plt.xlabel("OH distance(angstrom)")
plt.show()
