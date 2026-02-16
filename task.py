import requests
url = "https://uww.org/apiv4/getrankinglist/api/rankings/current/seniors/fs/57?page=1&season=2024"
data = requests.get(url).json()["content"]["hydramember"]
for p in data:
    print(f'{p["rank"]} | {p["person"]["fullname"]["firstname"]} {p["person"]["fullname"]["lastname"]} | {p["person"]["noc"]} | {p["uwwPoints"]}')
