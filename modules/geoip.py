# Krystian Szczech 2023-11-27
# Module which returns JSON-formatted geospatial
#    data for an IP address

from ipaddress import ip_address
from requests import get

# Main function!!!
def getResult(input_ip):
    # Validating IP address
    try:
        ip_address(input_ip)
    except ValueError as e:
        return (False, str(e))
    
    # Formatting URL
    url = "https://get.geojs.io/v1/ip/geo/" + input_ip + ".json"
    response = None

    # Getting response
    try:
        response = get(url)
    except Exception as e:
        return (False, str(e))
    
    # Checking that response was successful
    if(response.status_code != 200):
        return (False, "Status Code " + str(response.status_code))
    
    #Returning result
    return (True, response.content.decode()) 
    
