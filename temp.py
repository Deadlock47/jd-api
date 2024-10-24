import requests
url = "https://r18.dev/videos/vod/movies/detail/-/dvd_id=dass164/json"
data = requests.get(url)
print(data.json())