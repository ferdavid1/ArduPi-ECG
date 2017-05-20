import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

val = pd.read_table('PredValues.txt')
test = pd.read_table('MIT_1.txt')
plt.figure()
plt.plot(test)
plt.plot(np.arange(len(test), len(test) + len(val)), val)
plt.show()