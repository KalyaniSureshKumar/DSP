import numpy as np
import matplotlib.pyplot as plt
n=np.arange (0,10)
x=np.zeros_like(n)
x[n]=n
plt.stem(n,x)
plt.xticks(n)

