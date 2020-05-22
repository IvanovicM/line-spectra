import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from methods.minnorm import MinNorm
from methods.music import MUSIC
from signal import Signal

sns.set_style("whitegrid")
sns.despine(left=True, bottom=True)
sns.set_context("poster", font_scale = .45, rc={"grid.linewidth": 0.8})

def get_real_test_signal(show=True):
    w = 2 * np.pi * np.array([-0.4, -0.2, -0.15, 0, 0.15, 0.2, 0.4])
    alpha = np.array([1, 0.7, 1.2, 0.5, 1.2, 0.7, 1])
    sig = Signal(w=w, alpha=alpha, sigma_n=1)
    sig.plot_spectar(plt) if show else None
    return sig

def get_imag_test_signal(show=True):
    w = 2 * np.pi * np.array([-0.4, -0.26, -0.18, -0.1, 0.15, 0.36])
    sig = Signal(w=w, sigma_n=0.5)
    sig.plot_spectar(plt) if show else None
    return sig

def method_results(method, signals, show=True):
    results = []
    for sig in signals:
        method.estimate(sig)
        results.append(method.w)
        if show:
            method.plot_pseudo_spectrum(plt)
            method.plot_w(plt)
            print('Noise std estimation: {:.2f}'.format(method.sigma_n))
            
    return np.array(results)

if __name__ == '__main__':
    real_sig = get_real_test_signal(False)
    imag_sig = get_imag_test_signal(False)

    for method in [MUSIC(), MinNorm()]:
        method_results(method, [real_sig, imag_sig], True)