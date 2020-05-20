import numpy as np

from .music import MUSIC

class MinNorm(MUSIC):

    def __init__(self):
        super(MinNorm, self).__init__()
        self.type = 'Min Norm'

    def _estimate_pseudo_spectrum(self):
        super(MinNorm, self)._estimate_pseudo_spectrum()
        # TODO
