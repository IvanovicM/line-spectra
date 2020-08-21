import numpy as np

class Signal():

    def __init__(self, y, n, w=None, sigma_n=None, alpha=None, theta=None, Ts=1):
        '''
            Constructor for wrapper class around signal.
                y: signal itself
                n: number of sinusoidal components
                (optional) w: frequencies, if known
                (optional) sigma_n: white noise std, if known
                (optional) alpha: amplitudes, if known
                (optional) theta: phases, if known
                (optional) Ts: sample perio
        '''
        self.y = y
        self.n = n

        # Optional params, usually not known
        self.w = np.array(w) if w is not None else None
        self.sigma_n = sigma_n
        self.alpha = np.array(alpha) if alpha is not None else None
        self.theta = np.array(theta) if theta is not None else None
        self.Ts = Ts

    def plot_real_signal_part(self, plt):
        t = np.arange(0, self.y.size * self.Ts, self.Ts)
        plt.plot(t, self.y.real)
        plt.xlabel('$t$')
        plt.ylabel('$y(t)$')
        plt.title('Signal\'s real part')
        plt.show()

    def plot_spectar(self, plt, show=True):
        if self.w is None or self.alpha is None or self.sigma_n is None:
            print('Real signal spectar is not known.')
            return plt

        plt.plot(
            [-np.pi, np.pi], [self.sigma_n**2, self.sigma_n**2],
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
