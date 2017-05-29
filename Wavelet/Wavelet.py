import numpy as np
import pywt # pywavelet
import matplotlib.pyplot as plt
import pandas as pd
    
data = pd.read_table('../Real_Values.txt').get_values()
values = [float(d) for d in data]

def blocks(x):
    """
    Piecewise constant function with jumps at t.
 
    Constant scaler is not present in Donoho and Johnstone.
    """
    K = lambda x : (1 + np.sign(x))/2.
    t = np.array([[.1, .13, .15, .23, .25, .4, .44, .65, .76, .78, .81]]).T
    h = np.array([[4, -5, 3, -4, 5, -4.2, 2.1, 4.3, -3.1, 2.1, -4.2]]).T
    return 3.655606 * np.sum(h*K(x-t), axis=0)
 
x = np.linspace(0,1,2**11)
blk = blocks(x)

from scipy import stats
import numpy as np

np.random.seed(12345)
blck = blocks(np.linspace(0,1,2**11))
nblck = blck + stats.norm().rvs(2**11)
# true_coefs = pywt.wavedec(blck, 'db8', level=7, mode='per')
noisy_coefs = pywt.wavedec(values, 'db8', level=2, mode='per')

from statsmodels.robust import stand_mad

sigma = stand_mad(noisy_coefs[-1])
uthresh = sigma*np.sqrt(2*np.log(len(nblck)))
denoised = noisy_coefs[:]

denoised[1:] = (pywt.threshold(i, value=uthresh, mode='soft') for i in denoised[1:])

plt.figure()
signal = pywt.waverec(denoised, 'db8', mode='per')

plt.plot(values)
plt.plot(np.arange(len(values), len(values) + len(signal)), signal)
plt.title("Recovered Signal")
    
plt.tight_layout()
plt.show()
with open('Wavelet_PredValues.txt', 'w') as out:
    out.write(str([s for s in signal]).strip('[]'))
