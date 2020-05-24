import numpy as np

from .abstract import AbstractMethod
from math import sqrt
from scipy.signal import find_peaks

class ESPRIT(AbstractMethod):

    def __init__(self):
        super(ESPRIT, self).__init__()
        self.type = 'ESPRIT'

    def estimate(self, sig, m=None):
        self.sig = sig
        self.m = m if m is not None else len(self.sig.y) // 2

        self._estimate_cov_matrix()
        self._eig_decomp()
        self._compute_phi()
        self._estimate_w_from_phi()

    def _compute_phi(self):
        S1 = self.S[:-1, :]
        S2 = self.S[1:, :]
        self.phi = (S1.H * S1).I * S1.H * S2

    def _estimate_w_from_phi(self):
        eig_values, _ = np.linalg.eig(self.phi)
        self.w = -np.angle(eig_values) / self.sig.Ts
