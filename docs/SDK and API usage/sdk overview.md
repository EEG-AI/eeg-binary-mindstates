## Purpose of the SDK:
- The SDK connects your Python code to a Neurosity headset.
- Handles:
    - **Authentication**
    - **Device selection**
    - **Live Data Streaming**:
- The SDK gives you access to live data streaming for:
    1. Raw EEG signals - filtered or unfiltered
    2. Frequency features - brainwaves like **delta**, **theta**, **alpha**, **beta**, **gamma**
    3. Built-in mental states:
        - **Calm**: how relaxed you are. It’s high when you’re peaceful, quiet, or meditating.
        - **Focus**: how concentrated you are. It’s high when you are paying attention, solving problems, or working hard.
        - note: Calm and Focus are different: you can be calm but not focused (daydreaming), or focused but not calm (stressed).
    - **Motion** - data from the accelerometer (detects when your head moves).
    - **Device information** - battery, charging, online status.
### Authentication and Device Setup:
- `device_id` and login information can be found through neurosity's official app and console
- Required before subscribing to any data streams.
-----
## Data Streams:
### Sampling Rate:
Every device has a specific sampling rate:
- Crown :256Hz
- Notion 2 -> 250Hz
- Notion 1 -> 250Hz
**Note**: A sampling rate of 250Hz means the data contains 250 samples per second.
### Metrics:
- rawFiltered - raw EEG data (time-domain) with neurosity's build in noise filtering
- rawUnfiltered: **time-domain** EEG before device filters, used for complete control of filtering.
- psd (Power Spectral Density): **frequency** distribution of power (μV²/Hz).
    - Use for frequency features, entropy, ratios.
- powerByBand: absolute band powers for **delta, theta, alpha, beta, gamma.**
    - Use for quick features without FFT.
### Other Streams
- **quality**: signal quality per electrode.
    - Use to reject noisy windows.
- **accelerometer**: head motion (X, Y, Z).
    - Use to detect movement artifacts.
- **calm**: built-in relaxation probability.
- **focus**: built-in attention probability.
- **kinesis**: trained commands for thought-based control.
- **status / device_info**: battery, charging, online state, firmware.
------
# Key Terms
- Oscillation: repeating up-down electrical pattern.
- Synchrony: many neurons oscillate together; increases band power.
- Desynchrony (ERD): neurons work independently during active processing; this usually lowers alpha.
- PSD: power at each frequency.
- Absolute/Relative band power: energy in a band before/after normalization.
- Artifact: non-brain signal (eyes, muscles, motion, mains noise).
# References
https://docs.neurosity.co/docs/overview/
https://github.com/neurosity/neurosity-sdk-python
https://www.geeksforgeeks.org/electronics-engineering/power-spectral-density/

