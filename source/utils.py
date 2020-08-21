import numpy as np

def generate_signal(w, sigma_n, alpha=None, theta=None, Ts=1, N=100):
    '''
        Generates signal, based on:
            w: frequencies
            sigma_n: white noise std
            (optional) alpha: amplitudes
            (optional) theta: phases
            (optional) Ts: sample period
            (optional) N: number of samples

        Returns:
            y: generated signal
    '''
    # Check params
    n = w.size
    alpha = (
        np.array(alpha) if alpha is not None
        else np.random.uniform(1, 2, n)
    )
    theta = (
        np.array(theta) if theta is not None
        else np.pi * (2*np.random.rand(n) - 1)
    )
    if alpha.size != n or theta.size != n:
        print(w.size, alpha.size, theta.size)
        return None, None

    # Generate the signal
    t = np.arange(0, N * Ts, Ts)
    y = np.zeros(N, dtype=complex)
    for i in range(N):
        for k in range(n):
            y[i] += alpha[k] * np.exp(1j * (w[k] * t[i] + theta[k]))
        y[i] += sigma_n * np.random.randn()
    return y
