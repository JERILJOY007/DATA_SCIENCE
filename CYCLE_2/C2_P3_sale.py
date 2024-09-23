import matplotlib.pyplot as plt
import numpy as np
mon = np.array(['jan','feb','mar','Apr','may','Jun','jul','Aug','Sep','oct','nov''Dec'])
As = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
LS = np.array([189,189,105,112,173,109,151,197,174,145,174,145])
SLS = np.array([185,185,126,134,196,153,112,133,200,145,167,])
plt.xlabel("Month of Year" , fontsize=18)
plt.ylabel('Sales of segments')
plt.title('Sales Data')
plt.title('JERIL JOY\n23mca034\ncycle3_pgm3',loc='right')
plt.scatter(mon, As, label='Affordable segment',color='pink')
plt.scatter(mon, LS, label='Luxury Segment',color='yellow')
plt.scatter(mon, SLS, label='Super luxury segment',color='blue')
plt.show()