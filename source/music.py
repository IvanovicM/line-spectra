import numpy as np

from numpy import linalg as la 

class MUSIC():

    def __init__(self):
        self.type = 'MUSIC'

        # --- For testing ---
        self.n = 3
        self.w = np.array([-1.4, 0, 1.6])

    def apply(self, sig):
        pass

    def show_w(self, plt):
        plt.plot(
            self.w, np.zeros(self.n), label='estimated $\omega$',
            marker='X', linewidth=0, color='maroon'
        )
        return plt