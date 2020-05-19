import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from methods.music import MUSIC
from signal import Signal

sns.set()

if __name__ == '__main__':
    # Generate and show signal
    w = np.pi * np.array([-0.4, -0.1, 0.15, -0.8, -0.6, 0.6])
    sig = Signal(w=w, sigma_n=1)
    # sig.plot_real_signal_part(plt)
    #sig.plot_spectar(plt)

    # Apply methods and plot results
    ms = MUSIC()
    ms.estimate(sig)
    sig.plot_spectar(plt, False)
    ms.plot_pseudo_spectrum(plt)
    ms.plot_w(plt)