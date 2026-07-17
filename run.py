import pandas as pd
import numpy as numpy
import yaml
import argparse
import json
import logging
import time 
import os

start_time = time.time()

try: 
    # object to understand command line arguments
    parser = argparse.ArgumentParser(
        description = "ML OPS Assesment"
    )


    # add arguments

    parser.add_argument(
        "--input",
        required = True,
        help = "Path to input CSV"
        )

    parser.add_argument(
        "--config",
        required = True,
        help = "Path to YAML --config file"

    )

    parser.add_argument(
        "--output",
        required = True,
        help = "Path to the output"
    )

    parser.add_argument(
        "--log-file",
        required = True,
        help = "path to log file"
    )

    args = parser.parse_args()
    logging.basicConfig(
        filename = args.log_file,
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s"
    )


    logging.info("Job Started !!")

    # opeing the config file and storing the data of config file in dictionary using safe_load
    with open(args.config , 'r') as file:
        config = yaml.safe_load(file)
    #print(config)

    required_keys = ['seed' , 'window' , 'version']

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config field : {key}")
        
    logging.info("Config Loaded")
    numpy.random.seed(config['seed'])

    # taking dataset as an input

    df = pd.read_csv(args.input)
    # Validating dataset
    if df.empty:
        raise ValueError("Dataset is empty!!")

    if "close" not in df.columns:
        raise ValueError("Missing a column : close")

    logging.info("Dataset Loaded")

    # Rolling Mean Logic

    window = config['window']
    df["rolling_mean"] = df['close'].rolling(window=window).mean()

    logging.info("Rolling Mean Calculated")
    # Signal Logic
    df["signal"] = (df["close"] > df["rolling_mean"]).astype(int)

    # print(df[['close' , 'rolling_mean' , 'signal']].head())
    end_time = time.time()

    # row processed
    rows_processed = df.shape[0]
    print(f"Row Processed = {rows_processed}")

    # signal_rate

    signal_rate = df['signal'].mean()
    print(f"Signal Rate: {signal_rate}")


    # latency_ms

    latency_ms = (end_time - start_time) * 1000
    print(f"Latency: {latency_ms} ms")

    # metrics.json

    metrics = {
        "version" : config["version"],
        "rows_processed" : rows_processed,
        "metric" : "signal_rate",
        "value" : round(signal_rate , 4),
        "latency_ms" : round(latency_ms),
        "seed" :  config["seed"],
        "status" : "success"
    }

    with open(args.output , 'w') as file:
        json.dump(metrics,file , indent = 4)


    logging.info("Job Completed Successfully")

except Exception as e:
    logging.error(str(e))

    error_metrics = {
        "version" : config["version"] if "config" in locals() else "unknown",
        "status" : "error",
        "error_message" : str(e)
    }

    with open(args.output , 'w') as f:
        json.dump(error_metrics , f , indent = 4)

    raise


