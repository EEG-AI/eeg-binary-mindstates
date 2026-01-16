# all necessary imports for data retrieval and storage
import time
import argparse
import pandas as pd
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os

# Function saving stored rows to a csv
def save_checkpoint():
    print("Saving Current Rows & Clearing Buffer...")
    global apList, calmList, focusList, rawList
    if not (apList or calmList or focusList or rawList):
        return # If it is none of the states, nothing to save

    # Convert lists to DataFrames
    ap_df = pd.DataFrame(
        apList,
        columns=["timestamp", "alpha", "beta", "delta", "gamma", "theta"]
    )
    calm_df = pd.DataFrame(
        calmList,
        columns=["timestamp", "p_calm"]
    )
    focus_df = pd.DataFrame(
        focusList,
        columns=["timestamp", "p_focus"]
    )
    raw_df = pd.DataFrame(
        rawList,
        columns=['timestamp', 'CP6', 'F6', 'C4', 'CP4', 'CP3', 'F5', 'C3', 'CP5']
    )
       # Merge all three DataFrames
    merged = pd.merge(ap_df, calm_df, on="timestamp", how="outer")
    merged = pd.merge(merged, focus_df, on="timestamp", how="outer")

    # Format timestamp into datetime index
    merged.index = pd.to_datetime(
        merged["timestamp"], unit="ms", utc=True
    ).dt.strftime("%m/%d/%Y, %H:%M:%S")
    merged = merged.drop(columns=["timestamp"])
    # Define paths
    FEATURE_CSV_FILE = 'data/collected/ap_probability.csv'
    RAW_CSV_FILE = 'data/collected/raw_eeg.csv'
    # Append feature list to CSV (write header only if file doesn't exist)
    file_exists = os.path.isfile(FEATURE_CSV_FILE)
    merged.to_csv(FEATURE_CSV_FILE, mode="a", header=not file_exists)

    # Append eeg data to csv
    file_exists = os.path.isfile(RAW_CSV_FILE)
    raw_df.to_csv(RAW_CSV_FILE, mode="a", header=not file_exists)

    print(f"Appended {len(merged)} Rows To ap_probability.csv")
    print(f'Appended {len(raw_df)} Rows To raw_eeg.csv')
    # Clear buffers
    apList, calmList, focusList, rawList = [], [], [], []

# Callbacks for the SDK
def callback_focus(data):
    global focusList
    row = [data['timestamp'],data['probability']]
    focusList.append(row) # adds samples as rows with the structure of [ts, p_f]
    print(row)
    if len(focusList) >= BUFFER_LIMIT:
        save_checkpoint()

def callback_calm(data):
    global calmList
    row = [data['timestamp'], data['probability']]
    calmList.append(row) # adds samples as rows with the structure of [ts, p_c]
    print(row)
    if len(calmList) >= BUFFER_LIMIT:
        save_checkpoint()

def callback_ap(data):
    global apList
    ts = int(time.time() * 1000) # since the API doesn't send the ap's timestamp i use the system clock for it
    # adds samples as rows of [ts, alpha, beta, delta, gamma, theta]
    row = [ts, data['data']['alpha'], data['data']['beta'], data['data']['delta'], data['data']['gamma'], data['data']['theta']]
    apList.append(row)
    print(row)
    if len(apList) >= BUFFER_LIMIT:
        save_checkpoint()

def callback_raw(data):
    global rawList

    ts = data['info']['startTime']
    data = data['data']
    rawList.append([ts] + data)
    print([ts] + data)

# function initializing data subscribtions, parsing arguments, and handling exit
def main():
    # parse CL arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=60, help="Recording Duration")
    parser.add_argument("--buffer_limit", type=int, default=100, help="number or rows to cache before saving to csv")
    args = parser.parse_args()

    # All config variables
    global focusList
    global calmList
    global apList
    global rawList
    global BUFFER_LIMIT
    seconds = args.seconds
    focusList = []
    calmList = []
    apList = []
    rawList = []
    BUFFER_LIMIT = args.buffer_limit

    # Authenticating & Connecting To Neurosity
    load_dotenv()
    neurosity = NeurositySDK({
        "device_id": os.getenv("NEUROSITY_DEVICE_ID")
    })
    neurosity.login({
        "email": os.getenv("NEUROSITY_EMAIL"),
        "password": os.getenv("NEUROSITY_PASSWORD")
    })

    # Subscriptions to the Neurosity's live stream for focus, calm, and absolute power by band
    print(f"collecting data for the ap_probability table for {seconds} seconds")
    focus_unsubscribe = neurosity.focus(callback_focus)
    calm_unsubscribe = neurosity.calm(callback_calm)
    ap_unsubscribe = neurosity.brainwaves_power_by_band(callback_ap)
    raw_unsubscribe = neurosity.brainwaves_raw(callback_raw)

    # Try block to save even if Ctrl+C is pressed
    try:
        # Duration of stream
        time.sleep(seconds)
    finally:
        print("Termination Initialized \n Unsubscribing & Saving...")
        # Stop Subscription
        focus_unsubscribe()
        calm_unsubscribe()
        ap_unsubscribe()
        raw_unsubscribe()
        save_checkpoint()

if __name__ == "__main__":
    main()