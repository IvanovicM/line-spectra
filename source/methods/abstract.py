import numpy as np

from math import sqrt

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
            marker='X', markersize=6, linewidth=0, color='maroon'
        )

        plt.xlabel('$\omega$')
        plt.legend()
        plt.title('Real and estimated $\omega$ with {}'.format(self.type))
        plt.show()

    def _estimate_cov_matrix(self):
        N = len(self.sig.y)
        self.R = np.zeros((self.m, self.m), dtype='complex')

        for t in np.arange(self.m, N):
            y_tilde = np.matrix(self.sig.y[t-self.m : t][::-1]).T
            self.R += y_tilde * y_tilde.H
        self.R /= N

    def _eig_decomp(self):
        eig_values, eig_vectors = np.linalg.eig(self.R)

        # Estimate noise std
        lambda_sigma_n = eig_values[self.sig.n :]
        self.sigma_n = (
            sqrt(np.mean(lambda_sigma_n.real)) if len(lambda_sigma_n) > 1
            else lambda_sigma_n.real
        )
        
        # Form S and G
        self.S = np.matrix(eig_vectors[:, : self.sig.n])
        self.G = np.matrix(eig_vectors[:, self.sig.n :])

    def _get_response_vector(self, w):
        a = np.exp(-1j * w * np.arange(0, self.m) * self.sig.Ts)
        return np.matrix(a).T
