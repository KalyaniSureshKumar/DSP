import numpy as np
import matplotlib.pyplot as plt
n=np.arange(41)
x=np.exp((-1/12)+(1j*np.pi*n)/6)
plt.subplot(1,2,1)
plt.stem(n,np.real(x))
plt.subplot(1,2,2)
plt.stem(n,np.imag(x))
#plt.stem(x)