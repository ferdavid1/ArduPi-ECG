import numpy as np
import pywt # pywavelet
import matplotlib.pyplot as plt
import pandas as pd
    
data = pd.read_table('../Real_Values.txt').get_values()
values = [float(d) for d in data]

w = pywt.Wavelet('Haar') # use the Haar wavelet model to extrapolate the data
db8 = pywt.Wavelet('db8')
scaling, wavelet, x = db8.wavefun()

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(8,6))
ax1, ax2 = axes

ax1.plot(x, scaling);
ax1.set_title('Scaling function, N=8');
ax1.set_ylim(-1.2, 1.2);

ax2.set_title('Wavelet, N=8');
ax2.tick_params(labelleft=False);
ax2.plot(x-x.mean(), wavelet);

fig.tight_layout()
# plt.show()

from statsmodels.robust import stand_mad

sigma = stand_mad(noisy_coefs[-1])
uthresh = sigma*np.sqrt(2*np.log(len(nblck)))

denoised = noisy_coefs[:]

denoised[1:] = (pywt.thresholding.soft(i, value=uthresh) for i in denoised[1:])

signal = pywt.waverec(denoised, 'db8', mode='per')

fig, axes = plt.subplots(1, 2, sharey=True, sharex=True,
                         figsize=(10,8))
ax1, ax2 = axes

ax1.plot(signal)
ax1.set_xlim(0,2**10)
ax1.set_title("Recovered Signal")
ax1.margins(.1)

ax2.plot(nblck)
ax2.set_title("Noisy Signal")

for ax in fig.axes:
    ax.tick_params(labelbottom=False, top=False, bottom=False, left=False, 
                 right=False)
    
fig.tight_layout()
plt.show()
# with open('Wavelet_PredValues.txt', 'w') as out:
#     out.write(str([e for e in extrapolation]).strip('[]'))
