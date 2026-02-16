import requests
import json

url = "https://graphql-prod-4843.edge.aws.worldathletics.org/graphql"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://worldathletics.org",
    "Referer": "https://worldathletics.org/",
    "x-api-key": "da2-kh7djqqqkjczfgysuw3b7hczoq"
}

query = """
query GetStreak($id: String!) {
  getSingleCompetitorWinningStreak(
    competitorId: $id
  ) {
    streaks {
      length
      results {
        date
        result
        venue
      }
    }
  }
}
"""

variables = {
    "id": "14201847"
}

response = requests.post(
    url,
    headers=headers,
    json={
        "query": query,
        "variables": variables
    }
)

print(response.status_code)

if response.status_code == 200:
    data = response.json()

    streaks = data["data"]["getSingleCompetitorWinningStreak"]["streaks"]
    for streak in streaks:
        for result in streak["results"]:
            if "Diamond League Meeting" in result["competition"]:
                print("Diamond League Date:", result["date"])
else:
    print(response.text)
