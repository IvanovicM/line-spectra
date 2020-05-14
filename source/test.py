import matplotlib.pyplot as plt
import seaborn as sns

from music import MUSIC
from signal import Signal

sns.set()

def plot_real_and_estimated_w(sig, method):
    sig_plt = sig.show_w(plt)
    method_plt = method.show_w(plt)

    method_plt.xlabel('$\omega$')
    method_plt.legend()
    method_plt.title('Real and estimated $\omega$ with {}'.format(method.type))
    method_plt.show()

if __name__ == '__main__':
    # Generate and show signal
    sig = Signal(w=[-1.5, 0, 1.5], alpha=[2, 1, 2], theta=[0, 0, 0], sigma_n=1)
    # sig.plot_real_signal_part(plt)
    # sig.plot_spectar(plt)

    # Apply methods and plot results
    ms = MUSIC()
    ms.apply(sig)
    plot_real_and_estimated_w(sig, ms)