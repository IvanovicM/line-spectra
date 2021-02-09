# Signal analysis for line spectra signals

Various algorithms for the line spectra estimation, such as
* MUltiple SIgnal Classification (**MUSIC**) method 
* **Min Norm** method
* Estimation of Signal Parameters via Rational Invariance Techniques (**ESPRIT**) method

Based on the book "Spectral Analysis of Signals", P. Stoica &amp; R. Moses

## Methods results

To illustrate the results, let's look at the real spectrum of a testing sinal, and its pseudo spectrum generated by MUSIC method.

| <img src="images/real_spectum.png"> | <img src="images/music_pseudo_spectrum.png">|
|:---:|:---:|
| Real spectrum | Pseudo spectrum (MUSIC) |

Below you can see the real and the estimated sinusoidal components of the testing signal. Note that the results of the Min Norm method is very similar.

| <img src="images/music.png"> | <img src="images/esprit.png">|
|:---:|:---:|
| MUSIC estimation | ESPRIT estimation |

## Creating and running tests

To create your custom test, you can ```generate_signal``` and then ```apply_method``` from ```utils.py```.

To run any test, simply go to the directory 'source' and type in the following command in your terminal.

```
  python test.py
```
