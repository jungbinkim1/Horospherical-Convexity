import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import math

def B1(x,y):
    try: return -2*math.log((1-x**2-y**2)/((x-1)**2+y**2))
    except: return 99
def B2(x,y):
    try: return -4*math.log((1-x**2-y**2)/((y-1)**2+x**2)) 
    except: return 99
def B3(x,y):
    try: return -math.sqrt(5)*math.log((1-x**2-y**2)/((x-1/math.sqrt(5))**2+(y-2/math.sqrt(5))**2))
    except: return 99
def maxB(x,y):
    return max(B1(x,y),B2(x,y))
def dif(x,y):
    return 0.1+B3(x,y)-maxB(x,y)


v_dif = np.vectorize(dif)

plt.rcParams['text.usetex'] = True
plt.rcParams["font.family"] = "serif"
mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-0.3, 0.3, 1000)
y = np.linspace(-0.3, 0.3, 1000)
x, y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(5,5))

plt.xlabel(r'$\mathrm{Re}[z]$',size=15)
plt.ylabel(r'$\mathrm{Im}[z]$',size=15)
ax.contour(x, y, v_dif(x,y), [0], colors='k')
ax.contourf(x, y, v_dif(x,y), [0,1], colors='gray')

legend_elements = [mpl.patches.Rectangle((0, 0), 1, 1, fc='gray',label=r'$B_3(z)+0.1\geq B_1(z)+B_2(z)$')]
ax.legend(handles=legend_elements)
filename = 'results/buse_plot'+'.pdf'
# plt.savefig(filename, format='pdf',  bbox_inches='tight')
plt.show()