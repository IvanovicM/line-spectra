import matplotlib.pyplot as plt
import seaborn as sns

from music import MUSIC
from signal import Signal

sns.set()

if __name__ == '__main__':
    # Generate and show signal
    sig = Signal(w=[-1.5, 0, 1.5], alpha=[2, 1, 2], theta=[0, 0, 0], sigma_n=1)
    # sig.plot_real_signal_part(plt)
    # sig.plot_spectar(plt)

    # Apply methods and plot results
    ms = MUSIC()
    ms.estimate(sig)
    ms.plot_pseudo_spectrum(plt)
    ms.plot_w(plt)