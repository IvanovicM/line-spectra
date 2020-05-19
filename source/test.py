import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from methods.music import MUSIC
from signal import Signal

sns.set_style("whitegrid")
sns.despine(left=True, bottom=True)
sns.set_context("poster", font_scale = .45, rc={"grid.linewidth": 0.8})

def get_real_test_signal():
    w = np.pi * np.array([-0.4, -0.2, -0.15, 0, 0.15, 0.2, 0.4])
    alpha = np.array([1, 0.7, 1.2, 0.5, 1.2, 0.7, 1])
    sig = Signal(w=w, alpha=alpha, sigma_n=1)
    sig.plot_spectar(plt)

    return sig

def get_imag_test_signal():
    w = np.pi * np.array([-0.4, -0.26, -0.18, -0.1, 0.15, 0.36])
    sig = Signal(w=w, sigma_n=0.5)
    sig.plot_spectar(plt)
    
    return sig

def method_results(method):
    # Real signal
    sig = get_real_test_signal()
    method.estimate(sig)
    method.plot_pseudo_spectrum(plt)
    method.plot_w(plt)
    s_real = method.sigma_n

    # Imag signal
    sig = get_imag_test_signal()
    method.estimate(sig)
    method.plot_pseudo_spectrum(plt)
    method.plot_w(plt)
    s_imag = method.sigma_n

    # sigma_n estimations
    print('Estimation for noise std in:\n'
          '(1) real signal: {}\n'
          '(2) imag signal: {}'.format(s_real, s_imag)
    )

if __name__ == '__main__':
    ms = MUSIC()
    method_results(ms)