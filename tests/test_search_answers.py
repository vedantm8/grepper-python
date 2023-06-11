import requests

def search_code(query, api_key):
    url = "https://api.grepper.com/v1/answers/search"
    params = {
        "query": query
    }
    auth = requests.auth.HTTPBasicAuth(api_key, "")
    response = requests.get(url, params=params, auth=auth)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
query = "javascript loop array backwords"
api_key = "<YOUR API KEY HERE>"
results = search_code(query, api_key)
# print(results['data'][0])
for result in results['data']:
    print(f"By {result['author_name']}")
    print(result['title'])
    print('--------------------------------')
    print(result['content'])
    print('\n')