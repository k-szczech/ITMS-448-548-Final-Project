# Nicholas Simpkis 2023-11-30
# Detects spam emails using the Disify API

import requests

def detect_spam_email(api_key, email_content):
    try:
        # Replace 'DISIFY_API_ENDPOINT' with the actual Disify API endpoint
        api_endpoint = 'DISIFY_API_ENDPOINT'
        
        # Make a POST request to the Disify API
        response = requests.post(api_endpoint, headers={'Authorization': f'Bearer {api_key}'}, json={'email_content': email_content})
        
        # Parse the JSON response
        result = response.json()

        # Check if the request was successful
        if response.status_code == 200 and result.get('spam'):
            print("Spam email detected!")
        else:
            print("Not a spam email.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with the actual API key provided by Disify
    api_key = 'YOUR_API_KEY'
    
    # Replace 'email_content' with the actual content of the email you want to check
    email_content = 'This is an example email content.'

    detect_spam_email(api_key, email_content)