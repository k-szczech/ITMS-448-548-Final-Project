# Krystian Szczech 2023-11-27
# Module which returns JSON-formatted geospatial
#    data for an IP address

from ipaddress import ip_address
from requests import get

# Exception
class HTTPStatusCodeException(Exception):
    pass

# Main function!!!
def getResult(input_ip):
    # Validating IP address
    ip_address(input_ip)
    
    # Formatting URL
    url = "https://get.geojs.io/v1/ip/geo/" + input_ip + ".json"
    response = None

    # Getting response
    response = get(url)
    
    # Checking that response was successful
    if(response.status_code != 200):
        raise HTTPStatusCodeException(False, "Status Code " + str(response.status_code))
    
    #Returning result
    return response.content.decode()
print(getResult("221.226.230.8"))
