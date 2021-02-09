import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from methods.esprit import ESPRIT
from methods.minnorm import MinNorm
from methods.music import MUSIC
from signal import Signal
from utils import generate_signal, apply_method

sns.set_style("whitegrid")
sns.despine(left=True, bottom=True)
sns.set_context("poster", font_scale = .45, rc={"grid.linewidth": 0.8})

def get_real_test_signal(show=True):
    w = 2 * np.pi * np.array([-0.4, -0.2, -0.15, 0, 0.15, 0.2, 0.4])
    alpha = np.array([1, 0.7, 1.2, 0.5, 1.2, 0.7, 1])

    y = generate_signal(w=w, alpha=alpha, sigma_n=1)
    sig = Signal(y=y, n=len(w), w=w, alpha=alpha, sigma_n=1)
    sig.plot_spectar(plt) if show else None
    return sig

def get_imag_test_signal(show=True):
    w = 2 * np.pi * np.array([-0.4, -0.26, -0.18, -0.1, 0.15, 0.36])
    alpha = np.array([1.83, 1.87, 1.65, 1.55, 1.12, 1.1])

    y = generate_signal(w=w, sigma_n=0.5)
    sig = Signal(y=y, n=len(w), w=w, alpha=alpha, sigma_n=0.5)
    sig.plot_spectar(plt) if show else None
    return sig

def get_signal_with_large_n(show=True):
    n = 50
    w = 2 * np.pi * (np.arange(n) / n - 0.5)
    alpha = np.random.uniform(low=0.1, high=2, size=(n,))

    y = generate_signal(w=w, alpha=alpha, sigma_n=1, N=400)
    sig = Signal(y=y, n=n, w=w, alpha=alpha, sigma_n=1)
    sig.plot_spectar(plt) if show else None
    return sig
            
if __name__ == '__main__':
    test_signal_1 = get_real_test_signal(True)
    test_signal_2 = get_imag_test_signal(True)
    test_signal_large_n = get_signal_with_large_n(True)

    for method in [MUSIC(), MinNorm(), ESPRIT()]:
        apply_method(method, test_signal_1, True)
        apply_method(method, test_signal_2, True)
        apply_method(method, test_signal_large_n, True)