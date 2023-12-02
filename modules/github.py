import requests

def get_github_user_data(username):

    github_username = username

    api_url = f'https://api.github.com/users/{github_username}'

    try:
        # Make a GET request to the GitHub API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_data = response.json()
            # Print user data
            print(f"GitHub User Data for {github_username}:")
            print(f"Name: {user_data['name']}")
            print(f"Location: {user_data['location']}")
            print(f"Bio: {user_data['bio']}")
            print(f"Public Repositories: {user_data['public_repos']}")
            return True, user_data
        else:
            print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
            return False, (f"Error: Unable to fetch data. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False, (f"An error occurred: {str(e)}")
if __name__ == "__main__":
    # You could make this dynamic by asking the user for a username
    get_github_user_data('k-szczech')