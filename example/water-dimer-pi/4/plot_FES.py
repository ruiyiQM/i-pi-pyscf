import matplotlib.pyplot as plt
import numpy as np


s1 = np.genfromtxt("fes.dat")

# Remove horizontal space between axes
#annotate("Outside %s,\nInside %s" % (wise(outside), wise(inside)),
               
# Plot each graph, and manually set the y tick values
plt.plot(s1[:,0]/3.14*180, s1[:,1],'g',linewidth=1)

plt.xlabel("Torsion angle (degree)",fontsize=12)
plt.ylabel("Free energy (kJ/mol)",fontsize=12)
plt.show()
