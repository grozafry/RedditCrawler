import requests

def get_top_posts(search_query):
    url = 'https://www.reddit.com/search.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        'q': search_query,
        'sort': 'top',
        'limit': 10
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for i, post in enumerate(posts, start=1):
            title = post['data']['title']
            score = post['data']['score']
            print(f"{i}. Title: {title}, Score: {score}")
    else:
        print(f"Error: {response.status_code}")

# Example usage
search_input = input("Enter your search query: ")
get_top_posts(search_input)
