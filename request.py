import requests
api_url="http://waterservices.usgs.gov/rest/Site-Service.html"

response=requests.get(api_url)
response.json()

print (response)