import requests
url = "https://graphql-prod-4843.edge.aws.worldathletics.org/graphql"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "da2-kh7djqqqkjczfgysuw3b7hczoq"
}
payload = {
    "operationName": "GetSingleCompetitorWinningStreak",
    "query": """
        query GetSingleCompetitorWinningStreak($id: Int, $winningStreaksDisciplineOption: String, $winningStreaksFinalOnly: Boolean) {
            getSingleCompetitorWinningStreak(
                id: $id,
                winningStreaksDisciplineOption: $winningStreaksDisciplineOption,
                winningStreaksFinalOnly: $winningStreaksFinalOnly
            ) {
                streaks {
                    length
                    results {
                        date
                        competition
                        venue
                        race
                        result
                        discipline
                    }
                }
            }
        }
    """,
    "variables": {
        "id": 14549089,
        "winningStreaksDisciplineOption": "all",
        "winningStreaksFinalOnly": False
    }
}
data = requests.post(url, headers=headers, json=payload).json()
for streak in data["data"]["getSingleCompetitorWinningStreak"]["streaks"]:
    print(f"\nWinning Streak Length: {streak['length']}")
    for r in streak["results"]:
        print(f"{r['date']} | {r['competition']} | {r['venue']} | {r['race']} | {r['result']}m | {r['discipline']}")
