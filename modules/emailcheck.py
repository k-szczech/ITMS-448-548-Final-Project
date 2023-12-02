import requests

def detect_spam_email(email_content):
    try:
        api_endpoint = 'https://disify.com/api/email/'  

        response = requests.post(api_endpoint, json={'email_content': email_content})

        result = response.json()

        if response.status_code == 200 and result.get('spam'):
            print("Spam email detected!")
        else:
            print("Not a spam email.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":

    email_content = 'This is an example email content.'

    detect_spam_email(email_content)