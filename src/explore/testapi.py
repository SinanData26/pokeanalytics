import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

print(len(data))

parsed = []

for post in data:
    parsed.append({
        "post_id": post["id"],
        "user_id": post["userId"],
        "title": post["title"]
    })

print(parsed[:2])