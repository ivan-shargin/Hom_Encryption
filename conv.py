import numpy as np

A1 = np.array() #3-dim arr
A2 = np.array() #4-dim arr

(A1 * A2).reshape(-1, A2.shape[-1]).sum(axis=0)