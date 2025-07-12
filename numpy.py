import numpy as np

import matplotlib.pyplot as plt
samples = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(samples,bins=30, density=True, alpha=0.5, color='g')
plt.savefig('normal_distribution.png')