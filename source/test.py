import matplotlib.pyplot as plt
import seaborn as sns

from methods.music import MUSIC
from signal import Signal

sns.set()

if __name__ == '__main__':
    # Generate and show signal
    sig = Signal(w=[-2.5, -1, 0, 1, 2.5], sigma_n=1, Ts=1)
    # sig.plot_real_signal_part(plt)
    # sig.plot_spectar(plt)

    # Apply methods and plot results
    ms = MUSIC()
    ms.estimate(sig, m=10)
    ms.plot_pseudo_spectrum(plt)
    ms.plot_w(plt)