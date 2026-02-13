import requests
url = "https://graphql-prod-4843.edge.aws.worldathletics.org/graphql"
response = requests.get(url)
data= response.json()
print(data)