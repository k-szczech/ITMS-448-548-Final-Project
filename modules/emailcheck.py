import requests

def detect_spam_email(email_content):
    try:
        api_endpoint = 'https://disify.com/api/email/'  

        response = requests.post(api_endpoint, json={'email_content': email_content})
        print(response)
        result = response.json()
        print(result)
        if response.status_code == 200:
            print("Spam email address detected!")
            return("Spam email address detected!")
        else:
            print("Not a spam email.")
            return("Not a spam email.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return(f"An error occurred: {str(e)}")

if __name__ == "__main__":

    email_content = 'This is an example email content.'

    detect_spam_email(email_content)