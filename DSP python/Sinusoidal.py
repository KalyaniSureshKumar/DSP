import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,1,.02)
x=np.sin(2*np.pi*1*t)
y=np.sin(2*np.pi*2*t)
plt.plot(t,x,label='1 hz')
plt.plot(t,y,label='2 hz')
plt.legend();