### Nuerology summary (Read `docs/theory/brainwaves.md`)
- The **PSD** shows how much of the signal’s energy sits at each frequency. **Band power** is the energy in a range (e.g., alpha 8–12 Hz).
- General note:
    - If there is more synchrony : there is higher power at that frequency
    - If there is more **desynchrony**: then there is lower power at that frequency.

# Power Spectral Density (PSD)
- represents how the power of a signal is distributed across different frequency components.
- Used as a frequency domain analysis tool.
- PSD indicates which frequencies carry more energy.
- PSD is used to analyze signals contaminated by noise or containing multiple oscillatory components.
- General note:
    - If there is more synchrony : there is higher power at that frequency
    - If there is more **desynchrony**: then there is lower power at that frequency.
## Using Matplotlib
- [source](https://matplotlib.org/stable/gallery/lines_bars_and_markers/psd_demo.html#sphx-glr-gallery-lines-bars-and-markers-psd-demo-py)
- Matplotlib allows you to compute and compare power spectral density estimates using two methods:
    1. **Periodogram**
    2. **Welch’s method**
### Welch's method
There are two main interfaces:
1. **`matplotlib.pyplot.psd()`** :
    - A direct plotting function that computes and displays the PSD of an input signal.
    Arguments:
        - `x`: Array or sequence containing the data.
        - `NFFT`: No. of data points used for each block in the FFT.
        - `Fs`: Sampling frequency of the signal.
        - `detrend`, `window`, `noverlap`: Options for preprocessing.
    - [source](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html#)
2. **`Axes.psd()`**
    - An object-oriented variant, called on an `Axes` object.
    - Provides the same functionality, but integrates into subplot management more flexibly.
    - [source](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.psd.html)
## How PSD can help in EEG and Brainwave Data Analysis:
- PSD can decompose eeg signals into their frequency components (delta, theta, alpha, beta, gamma). This allows you to see which brainwave band carries the most power at a given time.
- For example, if alpha is high, this can indicate a calm state.
