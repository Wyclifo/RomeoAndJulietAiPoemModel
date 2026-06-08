import requests

def collect_data():
    url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"

    response = requests.get(url)

    with open("data/romeo_and_juliet.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

    return "Dataset Downloaded"