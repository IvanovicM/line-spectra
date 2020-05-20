import numpy as np

from .music import MUSIC

class MinNorm(MUSIC):

    def __init__(self):
        super(MinNorm, self).__init__()
        self.type = 'Min-Norm'

    def _estimate_pseudo_spectrum(self):
        self._calculate_g()
        self.pseudo_spectrum = np.zeros(len(self.all_w))
        for i in range(len(self.all_w)):
            w = self.all_w[i]
            a = self._get_response_vector(w)

            self.pseudo_spectrum[i] = 1.0 / np.linalg.norm(a.H * self.g)

    def _calculate_g(self):
        if self.m > 2 * self.sig.n:
            alpha = self.S[0, :].H
            S_part = self.S[1:, :]
            g_hat = -S_part @ alpha / (1 - np.linalg.norm(alpha))
        else:
            beta = self.G[0, :].H
            G_part = self.G[1:, :]
            g_hat = G_part @ beta / np.linalg.norm(beta)

        self.g = np.zeros((self.m, 1), dtype=complex)
        self.g[0] = 1
        self.g[1:] = g_hat