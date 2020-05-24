import numpy as np

from .abstract import AbstractMethod
from math import sqrt
from scipy.signal import find_peaks

class ESPRIT(AbstractMethod):

    def __init__(self):
        super(ESPRIT, self).__init__()
        self.type = 'ESPRIT'

    def estimate(self, sig, m=None, toeplitz_correct=False):
        self.sig = sig
        self.m = m if m is not None else len(self.sig.y) // 2

        self._estimate_cov_matrix()
        self._eig_decomp()
