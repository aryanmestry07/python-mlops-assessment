# MLOps Batch Processing Pipeline

## Project Overview

This project is a simple MLOps-style batch processing pipeline built using Python. The main objective was to understand how a production-style data processing job works by reading configuration files, processing a dataset, generating execution metrics, logging important events, and running the entire application inside a Docker container.

The application reads stock market data from a CSV file, calculates a rolling mean on the closing prices, generates a simple binary signal based on the rolling average, and stores execution metrics in a JSON file.

---

## Features

- Reads configuration from a YAML file
- Processes stock market CSV data
- Calculates rolling mean using Pandas
- Generates binary trading signals
- Creates execution metrics in JSON format
- Logs every important step of execution
- Handles errors using exception handling
- Runs inside a Docker container
- Supports command-line arguments using argparse

---

## Project Structure

```
mlops-batch-processing-pipeline/
│
├── data.csv
├── config.yaml
├── Dockerfile
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3.12
- Pandas
- NumPy
- PyYAML
- JSON
- Logging
- Argparse
- Docker

---

## How It Works

The application performs the following steps:

1. Reads configuration values from `config.yaml`
2. Loads the CSV dataset
3. Validates the required columns
4. Calculates the rolling mean of the `close` column
5. Generates a binary signal
6. Calculates execution metrics
7. Saves metrics into a JSON file
8. Logs the execution process
9. Handles any runtime errors gracefully

---

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/aryanmestry07/python-mlops-assessment.git
cd mlops-batch-processing-pipeline
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

## Running with Docker

Build the Docker image:

```bash
docker build -t mlops-assessment .
```

Run the container:

```bash
docker run --rm -v "${PWD}:/app" mlops-assessment --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

## Sample Output

Console Output

```
Rows Processed = 10000
Signal Rate = 0.4989
Latency = 41.19 ms
```

Example `metrics.json`

```json
{
    "version": "v1",
    "rows_processed": 10000,
    "metric": "signal_rate",
    "value": 0.4989,
    "latency_ms": 41.19,
    "seed": 42,
    "status": "success"
}
```

---

## Error Handling

The application validates the input dataset before processing.

If any required file or column is missing, it:

- Logs the error
- Creates an error metrics file
- Stops execution gracefully

---

## What I Learned

Through this project, I gained hands-on experience with:

- Building a Python batch processing application
- Working with YAML configuration files
- Using argparse for command-line applications
- Logging and exception handling
- Generating execution metrics
- Docker containerization
- Writing cleaner and more maintainable Python code

---

## Future Improvements

Some improvements I would like to add in the future are:

- Unit testing using pytest
- Better logging with log rotation
- Additional data validation
- Configuration through environment variables
- CI/CD pipeline using GitHub Actions

---

## Author

**Aryan Mestry**

GitHub: https://github.com/aryanmestry07
