import numpy as np

from numpy import linalg as la 

class MUSIC():

    def __init__(self):
        self.type = 'MUSIC'

        # --- For testing ---
        self.w = np.array([-1.4, 0, 1.6])

    def estimate(self, sig, m=10):
        self.sig = sig

    def plot_w(self, plt):
        plt.plot(
            self.sig.w, np.zeros(self.sig.n), label='real $\omega$',
            marker='D', markersize=9, linewidth=0, color='goldenrod'
        )
        plt.plot(
            self.w, np.zeros(self.sig.n), label='estimated $\omega$',
            marker='X', linewidth=0, color='maroon'
        )

        plt.xlabel('$\omega$')
        plt.legend()
        plt.title('Real and estimated $\omega$ with {}'.format(self.type))
        plt.show()