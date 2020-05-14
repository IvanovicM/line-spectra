import matplotlib.pyplot as plt
import seaborn as sns

from signal import Signal

sns.set()

def plot_real_and_estimated_w(sig):
    sig_plt = sig.show_w(plt)

    sig_plt.xlabel('$\omega$')
    sig_plt.legend()
    sig_plt.title('Real and estimated $\omega$ values')
    sig_plt.show()

if __name__ == '__main__':
    # Generate and swho signal
    sig = Signal(w=[-1.5, 0, 1.5], alpha=[2, 1, 2], theta=[0, 0, 0], sigma_n=1)
    sig.plot_real_signal_part(plt)
    sig.plot_spectar(plt)

    # Apply methods and plot results
    plot_real_and_estimated_w(sig)