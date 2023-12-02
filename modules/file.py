# Nicholas Simpkins 2023-11-30
# Uploads a file to file.io and prints the download link


import requests

def upload_file(file_path):
    try:
        # Open the file to be uploaded
        with open(file_path, 'rb') as file:
            # Make a POST request to file.io API
            response = requests.post('https://file.io/', files={'file': file})
            print(response)
            # Parse the JSON response
            result = response.json()

            # Check if the upload was successful
            if result['success']:
                print(f"File uploaded successfully! Download link: {result['link']}")
                return(f"File uploaded successfully! Download link: {result['link']}")
            else:
                print(f"Failed to upload file. Error: {result['error']}")
                return(f"Failed to upload file. Error: {result['error']}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return(f"An error occurred: {str(e)}")
# Example usage
if __name__ == "__main__":
    file_to_upload = 'path/to/your/file.txt'
    upload_file(file_to_upload)