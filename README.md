# `eeg-binary-mindstates`
- neural decoding
# File Structure
- The *data* folder stores raw data recieved from the device, as well as processed training data
- The *models* folder stores all models ready to use
- The *src* folder contains all the project's scripts for:
  - recording, preprocessing, and cleaning EEG.
  - Training and (live) inference
- The *docs* folder contains:
  - Guides on major scripts in `src`
  - Essential theory on Brainwaves
- The *examples* folder holds scripts that are ready to run with no device using existing data in the `data` folder.
# Getting Started
## Environment
1. Create a `.env` file with the variables required to connect your neurosity device. If you simply want to run example, skip this step as well as the Data Collection/Pre-processing sections.
```
NEUROSITY_EMAIL=your email here
NEUROSITY_PASSWORD=your password here
NEUROSITY_DEVICE_ID=your device id here
```
2. Setup a virtual enviroment (*Using Python 3.12*) and IDE
  - note: there are Jupyter Notebooks provided for data analysis and examples
3. Source the virtual environment and install the libraries in `/requirements.txt`
4. Go to [SDK Testing Notebook](src/python/notebooks/SDKtest.ipynb) to test SDK/API device connection, and analyze incoming data in the form of epochs and simple graphs. This is unnecessary if you just want to run the examples
## Data Collection
5. run the [data collection](src/python/scripts/data_collection.py) script to connect and start recieving live data streams from your device, make sure to change the config variables to choose how many epochs should be gathered and buffer size (how much data to recieve before autosaving):
## Data Cleaning & Pre-processing (in progress)
- run the [processing](src/python/scripts/pre-processing.py) to clean the file with raw data, add all mathematical summary & relative columns/selected features, and more
### What the final table should look like: (need to add the kinesis / accelo (motion artifact) columns, PSD columns for comparing left and right parts of brain)
- Timestamp
- alpha
- beta
- delta
- gamma
- theta
- mean_alpha
- mean_beta
- mean_delta
- mean_gamma
- mean_theta
- alpha_cp6
- beta_cp6
- gamma_cp6
- delta_cp6
- theta_cp6
- alpha_f6
- beta_f6
- gamma_f6
- delta_f6
- theta_f6
- alpha_c4
- beta_c4
- gamma_c4
- delta_c4
- theta_c4
- alpha_cp4
- beta_cp4
- gamma_cp4
- delta_cp4
- theta_cp4
- alpha_cp3
- beta_cp3
- gamma_cp3
- delta_cp3
- theta_cp3
- alpha_f5
- beta_f5
- gamma_f5
- delta_f5
- theta_f5
- alpha_c3
- beta_c3
- gamma_c3
- delta_c3
- theta_c3
- alpha_cp5
- beta_cp5
- gamma_cp5
- delta_cp5
- theta_cp5
- alpha_varience
- alpha_max
- alpha_min
- beta_varience
- beta_max
- beta_min
- gamma_varience
- gamma_max
- gamma_min
- delta_varience
- delta_max
- delta_min
- theta_varience
- theta_max
- theta_min
- raw_cp6
- raw_f6
- raw_c4
- raw_cp4
- raw_cp3
- raw_f5
- raw_c3
- raw_cp5
- relative_alpha
- relative_beta
- relative_delta
- relative_gamma
- relative_theta
- p_focus
- p_calm
- label
## Training The Model
(soon)
## Inference
(soon)
## Examples
(soon)