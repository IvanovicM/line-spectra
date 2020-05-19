import numpy as np

class Signal():

    def __init__(self, w, sigma_n, alpha=None, theta=None, N=100, Ts=1):
        self.n = len(w)
        self.w = np.array(w)
        self.sigma_n = sigma_n
        self.Ts = Ts

        self.alpha = (
            np.array(alpha) if alpha is not None
            else np.random.uniform(1, 2, self.n)
        )
        self.theta = (
            np.array(theta) if theta is not None
            else np.pi * (2*np.random.rand(10) - 1)
        )

        self._generate_signal(N)

    def plot_real_signal_part(self, plt):
        plt.plot(self.t, self.y.real)
        plt.xlabel('$t$')
        plt.ylabel('$y(t)$')
        plt.title('Signal\'s real part')
        plt.show()

    def plot_spectar(self, plt, show=True):
        plt.plot(
            [-np.pi/2, np.pi/2], [self.sigma_n**2, self.sigma_n**2],
            color='#1f77b4', label='noise'
        )
        plt.stem(
            self.w, self.alpha**2 + self.sigma_n**2, label='signal',
            bottom=self.sigma_n**2, use_line_collection=True,
            basefmt='#1f77b4', markerfmt='^', linefmt='maroon'
        )
        plt.xlabel('$\omega$')
        plt.ylabel('$S(\omega)$')
        plt.title('Signal\'s real PSD')
        plt.legend()
        plt.show() if show else None
        return plt

    def _generate_signal(self, N):
        self.t = np.arange(0, N * self.Ts, self.Ts)
        self.y = np.zeros(N, dtype=complex)

        for i in range(N):
            for k in range(self.n):
                self.y[i] += self.alpha[k] * np.exp(
                    1j * (self.w[k] * self.t[i] + self.theta[k])
                )
            self.y[i] += self.sigma_n * np.random.randn()
