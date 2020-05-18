import numpy as np

from .abstract import AbstractMethod
from math import sqrt
from scipy.signal import find_peaks

class MUSIC(AbstractMethod):

    def __init__(self):
        super(MUSIC, self).__init__()
        self.type = 'MUSIC'
        self.pseudo_spectrum = None

    def estimate(self, sig, m=5):
        self.sig = sig
        self.m = m
        self._estimate_cov_matrix()
        self._eig_decomp()
        self._estimate_pseudo_spectrum()
        self._remember_spectrum_peaks()

    def plot_pseudo_spectrum(self, plt):
        if self.pseudo_spectrum is None:
            return
        plt.plot(self.all_w, self.pseudo_spectrum.real)
        plt.xlabel('$\omega$')
        plt.title('MUSIC Pseudo Spectrum')
        plt.show()

    def _estimate_cov_matrix(self):
        N = len(self.sig.y)
        self.R = np.zeros((self.m, self.m), dtype='complex')

        for t in np.arange(self.m, N):
            y_tilde = np.matrix(self.sig.y[t-self.m : t]).T
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

    def _estimate_pseudo_spectrum(self):
        self.pseudo_spectrum = np.zeros(len(self.all_w))
        for i in range(len(self.all_w)):
            w = self.all_w[i]
            a = self._get_response_vector(w)

            self.pseudo_spectrum[i] = 1.0 / np.linalg.norm(self.G.H * a)

    def _remember_spectrum_peaks(self):
        w_peaks_idx,_ = find_peaks(self.pseudo_spectrum)
        w_max_idx = w_peaks_idx
        if len(w_peaks_idx) > self.sig.n:
            peaks = np.array([self.pseudo_spectrum[w_max_idx]][0])
            w_peaks = np.array([self.all_w[w_max_idx]][0])
            w_max_idx = np.array([
                w_max_idx[peaks.argsort()[-self.sig.n:][::-1]]
            ][0])
        self.w = np.array([self.all_w[w_max_idx]][0])
