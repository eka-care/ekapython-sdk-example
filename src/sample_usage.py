from ekacare import EkaCareClient

# --- Configuration Needed MUST ---
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
AUDIO_FILE_LIST = [ "audio_file_1_path", "audio_file_2_path" ] # List of audio files to upload
TRANSACTION_ID = "unique_transaction_id"

# --- Configuration Not Medentory ---
ACTION_TYPE = "ekascribe-v2"
EXTRA_PARAMS = {
        "mode": "dictation",
        "patient": {
            "name": "John Doe",}
        }

def main():
    try:
        # 1. Initialize the client
        client = EkaCareClient(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        
        # 2. Authenticate
        AUTHENTICATE_CLIENT(client)
        
        # 3. Upload audio files
        audio_paths_list = AUDIO_FILE_LIST
        action_type = ACTION_TYPE  
        extra_params = EXTRA_PARAMS
        UPLOAD_AUDIO_FILES(client, audio_paths_list, TRANSACTION_ID, action_type, extra_params)
        
        # 4. Fetch transcription results
        GET_TRANSCRIPTION_RESULTS(client, TRANSACTION_ID)
        
    except Exception as e:
        print(f"Error: {str(e)}")

def AUTHENTICATE_CLIENT(client):
    print("=== Authentication Example ===")
    # Login to get tokens
    token_response = client.auth.login()
    print(f"Initial Access Token: {token_response['access_token']}")
    print(f"Initial Refresh Token: {token_response['refresh_token']}")

    # Set access token manually
    client.set_access_token(token_response["access_token"])

    # Refresh token
    refreshed_tokens = client.auth.refresh_token(token_response["refresh_token"])
    print(f"New Access Token: {refreshed_tokens['access_token']}")
    
    # Set the new access token
    client.set_access_token(refreshed_tokens["access_token"])

def UPLOAD_AUDIO_FILES(client, audio_file_paths, transaction_id, action, extra_data):
    print("\n=== File Upload Example ===")
    
    try:
        responses = client.files.upload(
            file_paths=audio_file_paths, 
            txn_id=transaction_id, 
            action=action, 
            extra_data=extra_data,
            output_format = {
                "input_language": ["en-IN"],
                "output_template": [{"template_id": "eka_emr_template"}]
            }
        )
        
        print("File upload API call successful. Responses:")
        if responses: # Check if responses is not None and not empty
            for i, response_item in enumerate(responses):
                print(f"  Response for file {i+1}:")
                # These keys are based on the Java example. Adjust if Python SDK uses different keys.
                print(f"    Key: {response_item.get('key', 'N/A')}") 
                print(f"    Content Type: {response_item.get('contentType', response_item.get('content_type', 'N/A'))}")
                print(f"    Size: {response_item.get('size', 'N/A')} bytes")
                # You can print the full response_item for debugging if keys are different:
                # print(f"    Full Response Item: {response_item}")
        else:
            print("     No detailed response items received from file upload, or upload failed silently at SDK level.")
            
        return responses
    except Exception as e:
        print(f"    Error during file upload: {str(e)}")
        return None

def GET_TRANSCRIPTION_RESULTS(client, session_id):
    print("=== V2RX Fetcher Example ===")
    try:
        session_status = client.v2rx.get_session_status(session_id, ACTION_TYPE)
        print(f"Session Status: {session_status}")

    except Exception as e:
        print(f"  Error fetching V2RX status for session_id {session_id}: {str(e)}")
        return None

if __name__ == "__main__":
    main()