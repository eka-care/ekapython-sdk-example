# Eka Python SDK Example

This project provides a simple example demonstrating how to use the Eka Python SDK which simulating a flow similar to that used by the Ekascribe Chrome extension.

## Description

The `Eka Python SDK Example` showcases the integration of the EkaCare API for handling audio file uploads and fetching transcription results. It includes a test script that initializes the client, authenticates, uploads audio files, and retrieves results based on a session ID.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/eka-care/ekapython-sdk-example

    cd ekapython-sdk-example
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    This will install the `ekacare` (specify the version you need) SDK and other necessary libraries.
    ```text
    # requirements.txt

    ekacare==X.Y.Z # Replace X.Y.Z with version of ekacare

    ```
## Configuration

Before running the script, you need to set up your client credentials. Open the `src/sample_usage.py` file and replace the placeholders with your actual credentials:
### Must Do Configuration
```python
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
AUDIO_FILE_LIST =  [ "/path/to/your/audio1.m4a" ] # Multiple audio absolute file path
TRANSACTION_ID = "your_unique_transaction_id" 
```
### Optional Configuration for File Upload
```python
# filepath: src/sample_usage.py

ACTION_TYPE = "ekascribe" # "ekascribe" is typically used for transcription services.
EXTRA_PARAMS = {"mode": "dictation"} 
```

## Running the Example

To run the example:

1. Make sure you are in the `ekapython-sdk-example` directory
2. Execute the sample script:
    ```bash
    python src/sample_usage.py
    ```

The script will authenticate, upload your audio files, and retrieve transcription results based on your configuration.

## Usage

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Open the `src/sample_usage.py` file and ensure the configuration are set correctly.
5. Run the script using the following command:

```
python src/sample_usage.py
```

## Flow of Script

When you execute the script, it will perform the following actions:

- Initialize the `EkaCareClient` with the provided credentials.
- Authenticate the client and retrieve access tokens.
- Upload the specified audio file and handle the response.
- Fetch and print the transcription results based on the session ID.
