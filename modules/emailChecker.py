# Krystian Szczech
# Queries an API to see if an email is disposable

from requests import get

# Exception
class HTTPStatusCodeException(Exception):
    pass

# Main function!!!
def getResult(emailAddress):
    
    # Formatting URL
    url = "https://www.disify.com/api/email/" + emailAddress
    response = None

    # Getting response
    response = get(url)
    
    # Checking that response was successful
    if(response.status_code != 200):
        raise HTTPStatusCodeException(False, "Status Code " + str(response.status_code))
    
    #Returning result
    return response.content.decode()
    
