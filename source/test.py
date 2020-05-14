from signal import Signal

if __name__ == '__main__':
    s = Signal(w=[-1.5, 0, 1.5], alpha=[2, 1, 2], theta=[0, 0, 0], sigma_n=1)
    s.plot_real_signal_part()
    s.plot_spectar()