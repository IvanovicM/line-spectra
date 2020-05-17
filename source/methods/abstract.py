import numpy as np

class AbstractMethod():

    def __init__(self):
        self.all_w = np.linspace(-np.pi, np.pi, 100)

    def estimate(self, sig):
        pass

    def plot_w(self, plt):
        plt.plot(
            self.sig.w, np.zeros(self.sig.n), label='real $\omega$',
            marker='D', markersize=9, linewidth=0, color='goldenrod'
        )
        plt.plot(
            self.w, np.zeros(len(self.w)), label='estimated $\omega$',
            marker='X', linewidth=0, color='maroon'
        )

        plt.xlabel('$\omega$')
        plt.legend()
        plt.title('Real and estimated $\omega$ with {}'.format(self.type))
        plt.show()

    def _get_response_vector(self, w):
        a = np.zeros(self.m, dtype=complex)
        for i in range(self.m):
            a[i] = np.exp(-1j * i * w)
        return np.matrix(a).T
